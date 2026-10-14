import codecs
import json
import os
import re

VOLUMES_CONFIG = [
    {
        "id": "p4vol4",
        "title": "Phần 4 - Tập 4 (Part 4 Vol 4)",
        "dir": r"d:\novel\p4vol4",
    },
    {
        "id": "p4vol5",
        "title": "Phần 4 - Tập 5 (Part 4 Vol 5)",
        "dir": r"d:\novel\p4vol5",
    },
    {
        "id": "p4vol6",
        "title": "Phần 4 - Tập 6 (Part 4 Vol 6)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 4 Volume 6",
    },
    {
        "id": "p4vol7",
        "title": "Phần 4 - Tập 7 (Part 4 Vol 7)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 4 Volume 7",
    },
    {
        "id": "p4vol8",
        "title": "Phần 4 - Tập 8 (Part 4 Vol 8)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 4 Volume 8",
    },
    {
        "id": "p4vol9",
        "title": "Phần 4 - Tập 9 (Part 4 Vol 9)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 4 Volume 9",
    },
    {
        "id": "p5vol1",
        "title": "Phần 5 - Tập 1 (Part 5 Vol 1)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 Volume 1",
    },
    {
        "id": "p5vol2",
        "title": "Phần 5 - Tập 2 (Part 5 Vol 2)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 volume 2",
    },
    {
        "id": "p5vol3",
        "title": "Phần 5 - Tập 3 (Part 5 Vol 3)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 volume 3",
    },
    {
        "id": "p5vol4",
        "title": "Phần 5 - Tập 4 (Part 5 Vol 4)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 volume 4",
    },
    {
        "id": "p5vol5",
        "title": "Phần 5 - Tập 5 (Part 5 Vol 5)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 volume 5",
    },
    {
        "id": "p5vol6",
        "title": "Phần 5 - Tập 6 (Part 5 Vol 6)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 volume 6",
    },
    {
        "id": "p5vol7",
        "title": "Phần 5 - Tập 7 (Part 5 Vol 7)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 volume 7",
    },
    {
        "id": "p5vol8",
        "title": "Phần 5 - Tập 8 (Part 5 Vol 8)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 5 volume 8",
    },
]

def clean_text(text: str) -> str:
    """Normalize transliterations to match quy_tac_dich.md"""
    text = re.sub(r'\bRozemyne\b', 'Ro se mai', text, flags=re.IGNORECASE)
    text = re.sub(r'\bRosemy\b', 'Ro se mai', text, flags=re.IGNORECASE)
    return text

def build_library():
    result = []
    total_chapters = 0
    total_chars = 0

    for vol in VOLUMES_CONFIG:
        vdir = vol["dir"]
        if not os.path.exists(vdir):
            print(f"Warning: Directory not found: {vdir}")
            continue

        chapter_files = []
        for fname in os.listdir(vdir):
            if fname.startswith("translated") and fname.endswith(".txt"):
                m = re.search(r'(\d+)_(\d+)', fname)
                if m:
                    start_page = int(m.group(1))
                    end_page = int(m.group(2))
                    label = f"Trang {start_page}-{end_page}"
                    chapter_files.append((start_page, end_page, label, fname))

        # Sort chapters sequentially by starting page
        chapter_files.sort(key=lambda x: x[0])

        vol_data = {
            "id": vol["id"],
            "title": vol["title"],
            "chapters": []
        }

        for start_p, end_p, label, fname in chapter_files:
            fpath = os.path.join(vdir, fname)
            try:
                with codecs.open(fpath, 'r', 'utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {fpath}: {e}")
                content = ""

            content = clean_text(content.strip())
            if content:
                vol_data["chapters"].append({
                    "label": label,
                    "content": content
                })
                total_chapters += 1
                total_chars += len(content)

        result.append(vol_data)
        print(f"Loaded {vol['id']}: {len(vol_data['chapters'])} chapters")

    # Serialize to library_data.js
    out = "const LIBRARY_DATA = " + json.dumps(result, ensure_ascii=False, indent=2) + ";\n"

    target_paths = [
        r'd:\novel\library_data.js',
        r'd:\novel\text-splitter-web\library_data.js'
    ]

    for p in target_paths:
        target_dir = os.path.dirname(p)
        if os.path.exists(target_dir):
            with codecs.open(p, 'w', 'utf-8') as f:
                f.write(out)
            print(f"Saved: {p} ({len(out):,} bytes)")

    print(f"\nSuccessfully generated library data!")
    print(f"Total Volumes: {len(result)}")
    print(f"Total Chapters: {total_chapters}")
    print(f"Total Characters: {total_chars:,}")

if __name__ == "__main__":
    build_library()
