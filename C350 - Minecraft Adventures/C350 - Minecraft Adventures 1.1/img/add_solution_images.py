#!/usr/bin/env python3
"""
Add screenshot references under "## Solutions" in the challenge Markdown files.

Folder layout:
  Minecraft Adventures 2.1/         <- challenge1.md, challenge9-1.md, sub-challenge1-1.md, ...
    creation/
    code-solutions/
    img/
      add_solution_images.py        <- this script
      challenge1.png                -> challenge1.md
      challenge9-1.png              -> challenge9-1.md
      challenge22_2.png             -> challenge22.md, labelled "Alternative solution"
      challenge22 alt.png           -> same (any name containing "alt")
      sub-challenge1-1.png          -> sub-challenge1-1.md

Image names can also be the challenge title, e.g.
  "Challenge #9.1 Coordinates - Afraid of Heights.png" -> challenge9-1.md
using the same naming rules as generate_challenge_markdowns.py.

Each image is added as:
  ![Challenge #9.1: Coordinates - Afraid of Heights](img/challenge9-1.png)
below whatever is already in the Solutions section (e.g. the code block),
and above "## Explanation". If the Solutions section still only has the
template's empty "# your code here" block, that block is removed. Images already referenced are not added twice,
so it is safe to rerun after adding more screenshots.

Usage (preview first, then apply):
  python3 img/add_solution_images.py
  python3 img/add_solution_images.py --apply
"""

import argparse
import re
from pathlib import Path
from urllib.parse import quote

SCRIPT_DIR = Path(__file__).resolve().parent
IMG_DIR = SCRIPT_DIR
MARKDOWN_DIR = SCRIPT_DIR.parent
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


# --- Same naming rules as generate_challenge_markdowns.py -------------------

def parse_challenge_number(name):
    match = re.search(r"challenge\s*#?\s*(\d+(?:\.\d+)*)", name, flags=re.IGNORECASE)
    if not match:
        return None
    return ".".join(str(int(part)) for part in match.group(1).split("."))


def challenge_type_for(name):
    if re.search(r"\bsupplemental\b", name, flags=re.IGNORECASE):
        return "supplemental"
    if re.search(r"\(old\)|\bdisctd\b|\bdiscontinued\b", name, flags=re.IGNORECASE):
        return "discontinued"
    if re.match(r"^\s*sub[\s-]*challenge", name, flags=re.IGNORECASE):
        return "sub"
    if re.match(r"^\s*super[\s-]*challenge", name, flags=re.IGNORECASE):
        return "super"
    return "regular"


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "untitled"


def md_stem_from_title(name):
    number = parse_challenge_number(name)
    if number is None:
        return slugify(name)
    ctype = challenge_type_for(name)
    prefix = {"sub": "sub-challenge", "super": "super-challenge"}.get(ctype, "challenge")
    suffix = f"-{ctype}" if ctype in ("supplemental", "discontinued") else ""
    return f"{prefix}{number.replace('.', '-')}{suffix}"

# ---------------------------------------------------------------------------


def is_alternative(path):
    """Second screenshots: challenge22_2.png, challenge22 alt.png, challenge22-alt.png ..."""
    match = re.search(r"_(\d+)$", path.stem)
    return bool(re.search(r"\balt", path.stem, re.IGNORECASE) or (match and int(match.group(1)) >= 2))


def image_sort_key(path):
    """Main screenshot first, then alternatives (_2, _3 ... / alt)."""
    match = re.search(r"_(\d+)$", path.stem)
    order = int(match.group(1)) if match else (2 if is_alternative(path) else 1)
    return (order, path.name.lower())


def md_stem_for_image(image, md_stems):
    stem = image.stem.strip()
    base = re.sub(r"_\d+$", "", stem)        # drop _2, _3 ... for extra screenshots

    for candidate in (stem, base):
        if candidate.lower() in md_stems:
            return md_stems[candidate.lower()]

    derived = md_stem_from_title(base).lower()
    return md_stems.get(derived)


def get_title(markdown, fallback):
    match = re.search(r'(?m)^title:\s*"(.*)"\s*$', markdown)
    return match.group(1).replace('\\"', '"') if match else fallback


def add_images(markdown, image_lines):
    heading = re.search(r"(?m)^##\s+Solutions?\b.*$", markdown)
    if not heading:
        raise ValueError("No ## Solutions section found")

    rest = markdown[heading.end():]
    explanation = re.search(r"(?m)^##\s+Explanation\b.*$", rest)
    end = heading.end() + (explanation.start() if explanation else len(rest))

    section = markdown[heading.end():end].rstrip()
    # Screenshot is the solution: drop the template's empty placeholder code block.
    section = re.sub(r"\n*```\w*\n#\s*your code here\s*\n```", "", section).rstrip()
    new_section = section + "\n\n" + "\n\n".join(image_lines) + "\n\n"
    return markdown[:heading.end()] + new_section + markdown[end:]


def main():
    parser = argparse.ArgumentParser(description="Add screenshot references under ## Solutions.")
    parser.add_argument("--apply", action="store_true", help="Actually modify Markdown files")
    args = parser.parse_args()

    md_stems = {p.stem.lower(): p for p in MARKDOWN_DIR.glob("*.md") if p.is_file()}
    images = sorted(
        (p for p in IMG_DIR.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS),
        key=image_sort_key,
    )

    if not md_stems:
        print(f"No Markdown files found in {MARKDOWN_DIR}")
        return
    if not images:
        print(f"No images found in {IMG_DIR}")
        return

    by_md = {}
    unmatched = []
    for image in images:
        md_path = md_stem_for_image(image, md_stems)
        if md_path:
            by_md.setdefault(md_path, []).append(image)
        else:
            unmatched.append(image)

    print("Mode:", "APPLY" if args.apply else "PREVIEW")
    print(f"Images: {len(images)}  Markdown files: {len(md_stems)}\n")

    updated = 0
    for md_path in sorted(by_md, key=lambda p: p.name.lower()):
        original = md_path.read_text(encoding="utf-8")
        title = get_title(original, md_path.stem)
        rel_dir = IMG_DIR.relative_to(MARKDOWN_DIR).as_posix()

        new_lines = []
        for image in by_md[md_path]:
            ref = quote(f"{rel_dir}/{image.name}")   # spaces, # etc. made URL-safe
            if f"]({ref})" in original:
                continue
            line = f"![{title}]({ref})"
            if is_alternative(image):
                line = f"### Alternative solution\n\n{line}"
            new_lines.append(line)

        if not new_lines:
            print(f"UNCHANGED: {md_path.name} (images already added)")
            continue

        try:
            changed = add_images(original, new_lines)
        except ValueError as error:
            print(f"SKIP: {md_path.name} — {error}")
            continue

        names = ", ".join(i.name for i in by_md[md_path])
        print(f"{'UPDATED' if args.apply else 'WOULD UPDATE'}: {md_path.name} <- {names}")
        if args.apply:
            md_path.write_text(changed, encoding="utf-8")
        updated += 1

    for image in unmatched:
        print(f"NO MATCHING .md: {image.name}")

    print(f"\nSummary: {updated} file(s) {'updated' if args.apply else 'to update'}, "
          f"{len(unmatched)} image(s) unmatched.")
    if not args.apply:
        print("Preview only. Run again with --apply to make the changes.")


if __name__ == "__main__":
    main()
