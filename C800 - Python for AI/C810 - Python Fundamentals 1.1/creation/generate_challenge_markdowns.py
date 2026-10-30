#!/usr/bin/env python3
"""
Create one Markdown file per Canvas challenge from a JSON export.

Expected JSON format: a list of objects with "name" and "url".
Other fields (such as "module") are ignored. Challenge descriptions are
deliberately NOT used, so no challenge content ends up in the Markdown files;
only the challenge name and a link back to it.

Output file names (no zero padding):
  challenge1.md, challenge2.md, ... challenge46.md
  challenge1-supplemental.md      (supplemental challenges)
  challenge12-discontinued.md     (DISCTD. / discontinued challenges)

Expected folder layout:
  Python Fundamentals 1.1/          <- Markdown files are written here
    creation/
      generate_challenge_markdowns.py
      challenge.md                  (template)
      <course>.json                 (Canvas export)

Usage (from anywhere; paths are relative to where you run it):
  python creation/generate_challenge_markdowns.py \
    --json "creation/Python_Fundamentals_1.1_Course_Challenges.json" \
    --template "creation/challenge.md"

Defaults if omitted:
  --template    challenge.md next to this script
  --json        the only .json file next to this script
  --output-dir  the folder that contains the creation folder (the course folder)

Optional metadata overrides (otherwise read from the template front matter):
  --stream "Python for AI" --stream-code c800
  --course "Python Fundamentals 1.1" --course-code c821
  --version 1.1 --author "Your Name" --output-dir "some/other/folder"

Existing files are skipped unless --overwrite is supplied.
"""

import argparse
import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
COURSE_DIR = SCRIPT_DIR.parent

HEADING_PLACEHOLDER = "# Challenge N"
LINK_PLACEHOLDER = "<!-- Link to challenge will be here -->"


def yaml_quote(value):
    """Quote a string safely for YAML double-quoted scalars."""
    return json.dumps(str(value), ensure_ascii=False)


def split_front_matter(template_text):
    """Return (front_matter, body). Front matter is the text between the first two --- lines."""
    match = re.match(r"^---[ \t]*\n(.*?)\n---[ \t]*\n(.*)$", template_text, flags=re.DOTALL)
    if not match:
        raise ValueError("Template must start with YAML front matter between --- lines.")
    return match.group(1), match.group(2)


def read_template_metadata(front_matter):
    """Read simple key: value entries from the template's YAML front matter."""
    metadata = {}
    for line in front_matter.splitlines():
        match = re.match(r"^\s*([A-Za-z_][\w-]*):\s*(.*?)\s*(?:#.*)?$", line)
        if not match:
            continue
        key, value = match.groups()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace(r'\"', '"')
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        metadata[key] = value
    return metadata


def set_front_matter_value(front_matter, key, value):
    """Replace a key's value in the front matter, keeping any trailing # comment.
    Adds the key at the end if the template doesn't have it."""
    pattern = re.compile(rf"^({re.escape(key)}:[ \t]*)[^#\n]*?([ \t]*#.*)?$", flags=re.MULTILINE)
    if pattern.search(front_matter):
        return pattern.sub(lambda m: m.group(1) + value + (m.group(2) or ""), front_matter, count=1)
    return front_matter.rstrip("\n") + f"\n{key}: {value}"


def parse_challenge_number(name):
    match = re.search(r"challenge\s*#?\s*(\d+)", name, flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def strip_leading_zeros(name):
    """'Challenge #01: ...' -> 'Challenge #1: ...' (keeps '#0' and '#1000' as-is)."""
    return re.sub(r"#0+(\d)", r"#\1", name)


def challenge_type_for(name):
    if re.search(r"\bsupplemental\b", name, flags=re.IGNORECASE):
        return "supplemental"
    if re.search(r"\bdisctd\b|\bdiscontinued\b", name, flags=re.IGNORECASE):
        return "discontinued"
    return "regular"


def filename_for(name, index):
    """challenge1.md, challenge1-supplemental.md, challenge12-discontinued.md (no leading zeros)."""
    number = parse_challenge_number(name)
    number_text = str(number) if number is not None else str(index)
    ctype = challenge_type_for(name)
    suffix = "" if ctype == "regular" else f"-{ctype}"
    return f"challenge{number_text}{suffix}.md"


def render_markdown(template_text, challenge, metadata):
    name = strip_leading_zeros(str(challenge.get("name") or "Untitled Challenge").strip())
    url = str(challenge.get("url") or "").strip()
    number = parse_challenge_number(name)

    front_matter, body = split_front_matter(template_text)

    string_values = {
        "title": name,
        "stream": metadata["stream"],
        "stream_code": metadata["stream_code"],
        "course": metadata["course"],
        "course_code": metadata["course_code"],
        "version": metadata["version"],
        "author": metadata["author"],
        "challenge_type": challenge_type_for(name),
    }
    for key, value in string_values.items():
        front_matter = set_front_matter_value(front_matter, key, yaml_quote(value))

    # Numeric challenge value (no zero padding); null if the name has no number.
    front_matter = set_front_matter_value(front_matter, "challenge", str(number) if number is not None else "null")

    # Heading
    if HEADING_PLACEHOLDER in body:
        body = body.replace(HEADING_PLACEHOLDER, f"# {name}", 1)

    # Challenge Brief: link only (no description)
    link_text = url if url else "<!-- No link was supplied in the JSON export. -->"
    if LINK_PLACEHOLDER in body:
        body = body.replace(LINK_PLACEHOLDER, link_text, 1)
    else:
        body = re.sub(
            r"(## Challenge Brief[ \t]*\n)",
            lambda m: m.group(1) + "\n" + link_text + "\n",
            body,
            count=1,
        )

    return f"---\n{front_matter}\n---\n{body}".rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate one Markdown file per challenge in a Canvas JSON export.")
    parser.add_argument("--json", dest="json_path", help="Path to the Canvas JSON export (default: the only .json next to this script)")
    parser.add_argument("--template", default=str(SCRIPT_DIR / "challenge.md"), help="Path to the Markdown template (default: challenge.md next to this script)")
    parser.add_argument("--output-dir", default=str(COURSE_DIR), help="Directory for generated Markdown files (default: the course folder, one level above this script)")
    parser.add_argument("--stream", help="Override stream name from template")
    parser.add_argument("--stream-code", help="Override stream code from template")
    parser.add_argument("--course", help="Override course name from template")
    parser.add_argument("--course-code", help="Override course code from template")
    parser.add_argument("--version", help="Override course version from template")
    parser.add_argument("--author", help="Override author from template")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing generated Markdown files")
    args = parser.parse_args()

    if args.json_path:
        json_path = Path(args.json_path)
    else:
        candidates = sorted(SCRIPT_DIR.glob("*.json"))
        if len(candidates) != 1:
            parser.error(f"Found {len(candidates)} .json files in {SCRIPT_DIR}; pass --json to choose one.")
        json_path = candidates[0]
    template_path = Path(args.template)
    if not json_path.is_file():
        parser.error(f"JSON file not found: {json_path}")
    if not template_path.is_file():
        parser.error(f"Template file not found: {template_path}")

    with json_path.open("r", encoding="utf-8-sig") as handle:
        challenges = json.load(handle)
    if not isinstance(challenges, list):
        parser.error("Expected the JSON root to be a list of challenge objects.")

    template_text = template_path.read_text(encoding="utf-8")
    template_metadata = read_template_metadata(split_front_matter(template_text)[0])
    metadata = {
        "stream": args.stream or template_metadata.get("stream", "Unknown stream"),
        "stream_code": args.stream_code or template_metadata.get("stream_code", "unknown"),
        "course": args.course or template_metadata.get("course", json_path.stem),
        "course_code": args.course_code or template_metadata.get("course_code", "unknown"),
        "version": args.version or template_metadata.get("version", "unspecified"),
        "author": args.author or template_metadata.get("author", "Your Name"),
    }

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    written = skipped = 0
    used_names = set()

    for index, challenge in enumerate(challenges, start=1):
        if not isinstance(challenge, dict):
            print(f"Skipping JSON entry {index}: expected an object.")
            skipped += 1
            continue

        name = str(challenge.get("name") or f"Untitled Challenge {index}").strip()
        filename = filename_for(name, index)

        # Guard against duplicate names in the source export.
        if filename.casefold() in used_names:
            filename = f"{Path(filename).stem}-duplicate{index}.md"
        used_names.add(filename.casefold())

        destination = output_dir / filename
        if destination.exists() and not args.overwrite:
            print(f"SKIP (already exists; use --overwrite to replace): {destination}")
            skipped += 1
            continue

        destination.write_text(render_markdown(template_text, challenge, metadata), encoding="utf-8")
        written += 1

    print(f"Done. Created {written} Markdown file(s); skipped {skipped}.")
    print(f"Output folder: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
