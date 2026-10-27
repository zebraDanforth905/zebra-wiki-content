#!/usr/bin/env python3

from pathlib import Path
import re
import argparse


# The script is inside code-solutions.
SCRIPT_DIR = Path(__file__).resolve().parent
MARKDOWN_DIR = SCRIPT_DIR.parent
SOLUTIONS_DIR = SCRIPT_DIR

SOURCE_PATTERN = re.compile(
    r"^challenge\s*#?\s*0*(\d+)"
    r"(?:\s*[-_ ]*\s*(supplemental|discontinued))?"
    r".*\.py$",
    re.IGNORECASE,
)


def get_metadata(text):
    """Read simple YAML front matter from a Markdown file."""
    match = re.match(
        r"\A---\s*\n(.*?)\n---\s*\n",
        text,
        re.DOTALL,
    )

    metadata = {}

    if not match:
        return metadata

    for line in match.group(1).splitlines():
        item = re.match(
            r"^\s*([\w-]+):\s*(.*?)\s*$",
            line,
        )

        if item:
            key, value = item.groups()
            value = re.sub(r"\s+#.*$", "", value).strip()
            value = value.strip("\"'")
            metadata[key] = value

    return metadata


def get_challenge_number(path, metadata):
    value = metadata.get("challenge", "")

    if value.isdigit():
        return int(value)

    match = re.search(
        r"challenge\s*#?\s*0*(\d+)",
        path.stem,
        re.IGNORECASE,
    )

    return int(match.group(1)) if match else None


def get_challenge_type(path, metadata):
    name = path.stem.lower()

    if "supplemental" in name:
        return "supplemental"

    if "discontinued" in name:
        return "discontinued"

    return "regular"


def get_source_info(path):
    name = path.stem.strip()

    # Supplemental files: Supplemental1.py, Supplemental2.py, etc.
    match = re.fullmatch(r"Supplemental\s*0*(\d+)", name, re.IGNORECASE)

    if match:
        return int(match.group(1)), "supplemental"

    # Regular and discontinued challenge files: challenge1.py, etc.
    match = re.match(
        r"^challenge\s*#?\s*0*(\d+)"
        r"(?:\s*[-_ ]*\s*(discontinued))?$",
        name,
        re.IGNORECASE,
    )

    if match:
        number = int(match.group(1))
        kind = (match.group(2) or "regular").lower()
        return number, kind

    return None


def replace_solutions(markdown, code, language="python"):
    """Replace the Solutions section while preserving later sections."""

    heading = re.search(
        r"(?m)^##\s+Solutions?\b.*$",
        markdown,
    )

    if not heading:
        raise ValueError("No ## Solutions section found")

    explanation = re.search(
        r"(?m)^##\s+Explanation\b.*$",
        markdown[heading.end():],
    )

    if explanation:
        suffix_start = heading.end() + explanation.start()
        suffix = markdown[suffix_start:]
    else:
        suffix = ""

    section = (
        "## Solutions\n\n"
        f"```{language}\n"
        f"{code.rstrip()}\n"
        "```\n\n"
    )

    return (
        markdown[:heading.start()]
        + section
        + suffix.lstrip("\n")
    )


def main():
    parser = argparse.ArgumentParser(
        description="Fill Markdown challenge files with Python solutions."
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually modify Markdown files",
    )

    parser.add_argument(
        "--backup",
        action="store_true",
        help="Save original Markdown files as .bak",
    )

    args = parser.parse_args()

    markdown_files = sorted(
        path for path in MARKDOWN_DIR.glob("Challenge *.md")
        if path.is_file()
    )

    source_files = sorted(
        path for path in SOLUTIONS_DIR.glob("*.py")
        if path.is_file()
    )

    sources = {}

    for path in source_files:
        info = get_source_info(path)

        if info:
            sources.setdefault(info, []).append(path)

    if not markdown_files:
        print(f"No Markdown challenge files found in {MARKDOWN_DIR}")
        return

    if not sources:
        print(f"No challenge solution files found in {SOLUTIONS_DIR}")
        return

    updated = missing = ambiguous = skipped = 0

    print("Mode:", "APPLY" if args.apply else "PREVIEW")
    print(f"Markdown files: {len(markdown_files)}")
    print(f"Python solution files: {sum(map(len, sources.values()))}\n")

    for md_path in markdown_files:
        original = md_path.read_text(encoding="utf-8")
        metadata = get_metadata(original)

        number = get_challenge_number(md_path, metadata)
        kind = get_challenge_type(md_path, metadata)

        if number is None:
            print(f"SKIP: {md_path.name} — challenge number not found")
            skipped += 1
            continue

        candidates = sources.get((number, kind), [])

        if not candidates:
            print(f"MISSING: {md_path.name}")
            missing += 1
            continue

        if len(candidates) > 1:
            names = ", ".join(p.name for p in candidates)
            print(f"AMBIGUOUS: {md_path.name} — {names}")
            ambiguous += 1
            continue

        source = candidates[0]

        try:
            code = source.read_text(encoding="utf-8-sig")
            language = metadata.get("language", "python") or "python"

            changed = replace_solutions(
                original,
                code,
                language,
            )

        except (OSError, UnicodeDecodeError, ValueError) as error:
            print(f"SKIP: {md_path.name} — {error}")
            skipped += 1
            continue

        if changed == original:
            print(f"UNCHANGED: {md_path.name}")
            skipped += 1
            continue

        print(f"{'UPDATED' if args.apply else 'WOULD UPDATE'}: "
              f"{md_path.name} <- {source.name}")

        if args.apply:
            if args.backup:
                backup = md_path.with_suffix(".md.bak")

                if not backup.exists():
                    backup.write_text(original, encoding="utf-8")

            md_path.write_text(changed, encoding="utf-8")

        updated += 1

    print("\nSummary:")
    print(f"Updated / matched: {updated}")
    print(f"Missing: {missing}")
    print(f"Ambiguous: {ambiguous}")
    print(f"Skipped: {skipped}")

    if not args.apply:
        print("\nPreview only. No files were changed.")
        print("Run again with --apply to make the changes.")


if __name__ == "__main__":
    main()