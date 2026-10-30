#!/usr/bin/env python3
"""
Create one Markdown file per Canvas challenge from a JSON export.

Expected JSON format: a list of objects with "name", "description", and optionally
"links". Other fields (such as "module") are intentionally ignored.

Usage:
  python3 creation/generate_challenge_markdowns.py \
    --json creation/"Introduction_to_AI_Course_Challenges.json" \
    --template creation/"challenge.md"

By default, files are written directly to the current directory (no folders are created).

Optional metadata overrides:
  --stream "Python for AI" --stream-code C800
  --course "Python Fundamentals 1.1" --course-code C821
  --version 1.1 --output-dir ./challenge_markdowns

The defaults below are read from the template front matter. The script does not
delete or overwrite existing Markdown files unless --overwrite is supplied.
"""

import argparse
import json
import re
import shutil
from pathlib import Path


def yaml_quote(value):
    """Quote a string safely for YAML double-quoted scalars."""
    return json.dumps(str(value), ensure_ascii=False)


def slugify(value):
    value = value.strip()
    value = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-_.") or "untitled"


def read_template_metadata(template_text):
    """Read simple key: value entries from the template's YAML front matter."""
    parts = template_text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Template must start with YAML front matter between --- lines.")
    metadata = {}
    for line in parts[1].splitlines():
        match = re.match(r"^\s*([A-Za-z_][\w-]*):\s*(.*?)\s*(?:#.*)?$", line)
        if not match:
            continue
        key, value = match.groups()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace(r'\"', '"')
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        metadata[key] = value
    return metadata


def parse_challenge_number(name):
    match = re.search(r"challenge\s*#?\s*(\d+)", name, flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def filename_for(name, index):
    """Use the challenge number, marking supplemental/discontinued entries clearly."""
    number = parse_challenge_number(name)
    number_text = f"{number:02d}" if number is not None else f"{index:02d}"
    if re.search(r"\bsupplemental\b", name, flags=re.IGNORECASE):
        return f"Challenge {number_text} - supplemental.md"
    if re.search(r"\bdisctd\b|\bdiscontinued\b", name, flags=re.IGNORECASE):
        return f"Challenge {number_text} - discontinued.md"
    return f"Challenge {number_text}.md"


def replace_front_matter_value(template_text, key, value, quote=True):
    pattern = re.compile(rf"^({re.escape(key)}:\s*).*$", flags=re.MULTILINE)
    replacement = f"{key}: {yaml_quote(value) if quote else value}"
    if pattern.search(template_text):
        return pattern.sub(lambda m: m.group(1) + replacement.split(": ", 1)[1], template_text, count=1)
    return template_text


def render_markdown(template_text, challenge, metadata):
    name = str(challenge.get("name") or "Untitled Challenge").strip()
    description = str(challenge.get("description") or "").strip()
    number = parse_challenge_number(name)
    title = name

    output = template_text
    values = {
        "title": title,
        "stream": metadata["stream"],
        "stream_code": metadata["stream_code"],
        "course": metadata["course"],
        "course_code": metadata["course_code"],
        "version": metadata["version"],
        "language": metadata["language"],
        "author": metadata["author"],
        "status": metadata["status"],
    }
    for key, value in values.items():
        output = replace_front_matter_value(output, key, value, quote=True)

    # Challenge number is numeric when available; keep null for unusual unnumbered entries.
    challenge_value = str(number) if number is not None else "null"
    output = replace_front_matter_value(output, "challenge", challenge_value, quote=False)

    # Preserve the template's tags field; add a challenge_type field to distinguish
    # regular challenges from supplemental/discontinued entries with repeated numbers.
    supplemental = bool(re.search(r"\bsupplemental\b", name, flags=re.IGNORECASE))
    discontinued = bool(re.search(r"\bdisctd\b|\bdiscontinued\b", name, flags=re.IGNORECASE))
    challenge_type = "supplemental" if supplemental else ("discontinued" if discontinued else "regular")
    output = output.replace("---\n\n# Challenge N", f'challenge_type: {yaml_quote(challenge_type)}\n---\n\n# {title}', 1)

    problem_marker = "<!-- Paste the challenge prompt here. -->"
    if problem_marker in output:
        output = output.replace(problem_marker, description or "<!-- No description was supplied in the JSON export. -->", 1)
    else:
        output = re.sub(
            r"(?s)(## Problem\s*\n).*?(?=\n## Solution)",
            lambda m: m.group(1) + (description or "<!-- No description was supplied in the JSON export. -->") + "\n",
            output,
            count=1,
        )

    # Keep one plural Solutions section; multiple approaches can be added within it.
    solution_start = output.find("## Solution")
    explanation_start = output.find("## Explanation")
    if solution_start != -1 and explanation_start != -1 and explanation_start > solution_start:
        scaffold = (
            "## Solutions\n\n"
            f"```{metadata['language']}\n# Add solution(s) here\n```\n\n"
            "You can include multiple approaches in this section if needed.\n\n"
        )
        output = output[:solution_start] + scaffold + output[explanation_start:]
    else:
        # If a custom template has no expected headings, leave its structure alone.
        pass

    links = challenge.get("links") or []
    links = [str(link).strip() for link in links if str(link).strip()]
    if links:
        resource_block = "\n".join(f"- {link}" for link in links)
        marker = "## Additional Resources (optional)"
        if marker in output:
            output = output.replace(marker, marker + "\n\n" + resource_block, 1)

    return output.rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate one Markdown file per challenge in a Canvas JSON export.")
    parser.add_argument("--json", required=True, dest="json_path", help="Path to the Canvas JSON export")
    parser.add_argument("--template", required=True, help="Path to the Markdown template")
    parser.add_argument("--output-dir", default=".", help="Directory for generated Markdown files (default: current directory; no course folders are created)")
    parser.add_argument("--stream", help="Override stream name from template")
    parser.add_argument("--stream-code", help="Override stream code from template")
    parser.add_argument("--course", help="Override course name from template")
    parser.add_argument("--course-code", help="Override course code from template")
    parser.add_argument("--version", help="Override course version from template")
    parser.add_argument("--author", help="Override author from template")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing generated Markdown files")
    args = parser.parse_args()

    json_path = Path(args.json_path)
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
    template_metadata = read_template_metadata(template_text)
    metadata = {
        "stream": args.stream or template_metadata.get("stream", "Unknown stream"),
        "stream_code": args.stream_code or template_metadata.get("stream_code", "unknown"),
        "course": args.course or template_metadata.get("course", json_path.stem),
        "course_code": args.course_code or template_metadata.get("course_code", "unknown"),
        "version": args.version or template_metadata.get("version", "unspecified"),
        "language": template_metadata.get("language", "text"),
        "author": args.author or template_metadata.get("author", "Your Name"),
        "status": template_metadata.get("status", "draft").split()[0],
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
            stem = Path(filename).stem
            filename = f"{stem} - duplicate-{index:02d}.md"
        used_names.add(filename.casefold())

        destination = output_dir / filename
        if destination.exists() and not args.overwrite:
            print(f"SKIP (already exists; use --overwrite to replace): {destination}")
            skipped += 1
            continue

        markdown = render_markdown(template_text, challenge, metadata)
        destination.write_text(markdown, encoding="utf-8")
        written += 1

    print(f"Done. Created {written} Markdown file(s); skipped {skipped}.")
    print(f"Output folder: {output_dir.resolve()}")
    print("Module names from the JSON are intentionally ignored; no course/module folder hierarchy is created.")


if __name__ == "__main__":
    main()
