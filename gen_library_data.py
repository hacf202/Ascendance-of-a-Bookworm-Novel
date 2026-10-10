import codecs
import json
import os

volumes = [
    {
        "id": "p4vol4",
        "title": "Phần 4 - Tập 4 (Tiếng Anh: Part 4 Vol 4)",
        "dir": r"d:\novel\p4vol4",
        "chapters": [
            {"file": "translated_01_50.txt", "label": "Trang 1-50"},
            {"file": "translated_51_100.txt", "label": "Trang 51-100"},
            {"file": "translated_101_150.txt", "label": "Trang 101-150"},
            {"file": "translated_151_200.txt", "label": "Trang 151-200"},
            {"file": "translated_201_250.txt", "label": "Trang 201-250"},
            {"file": "translated_251_300.txt", "label": "Trang 251-300"},
            {"file": "translated_301_350.txt", "label": "Trang 301-350"},
            {"file": "translated_351_400.txt", "label": "Trang 351-400"},
        ]
    },
    {
        "id": "p4vol5",
        "title": "Phần 4 - Tập 5 (Tiếng Anh: Part 4 Vol 5)",
        "dir": r"d:\novel\Ascendance of a Bookworm Part 4 Volume 5",
        "chapters": [
            {"file": "translated_01_50.txt", "label": "Trang 1-50"},
            {"file": "translated_51_100.txt", "label": "Trang 51-100"},
            {"file": "translated_101_150.txt", "label": "Trang 101-150"},
            {"file": "translated_151_200.txt", "label": "Trang 151-200"},
            {"file": "translated_201_250.txt", "label": "Trang 201-250"},
            {"file": "translated_251_300.txt", "label": "Trang 251-300"},
            {"file": "translated_301_350.txt", "label": "Trang 301-350"},
            {"file": "translated_351_400.txt", "label": "Trang 351-400"},
        ]
    },
    {
        "id": "p4vol6",
        "title": "Phần 4 - Tập 6 (Tiếng Anh: Part 4 Vol 6)",
        "dir": r"d:\novel\p4vol5",
        "chapters": [
            {"file": "translated_01_50.txt", "label": "Trang 1-50"},
            {"file": "translated_51_100.txt", "label": "Trang 51-100"},
            {"file": "translated_101_150.txt", "label": "Trang 101-150"},
            {"file": "translated_151_200.txt", "label": "Trang 151-200"},
            {"file": "translated_201_250.txt", "label": "Trang 201-250"},
            {"file": "translated_251_300.txt", "label": "Trang 251-300"},
            {"file": "translated_301_350.txt", "label": "Trang 301-350"},
            {"file": "translated_351_400.txt", "label": "Trang 351-400"},
        ]
    },
]

result = []
for vol in volumes:
    vol_data = {"id": vol["id"], "title": vol["title"], "chapters": []}
    for ch in vol["chapters"]:
        fpath = os.path.join(vol["dir"], ch["file"])
        content = ""
        if os.path.exists(fpath):
            with codecs.open(fpath, 'r', 'utf-8') as f:
                content = f.read()
        vol_data["chapters"].append({
            "label": ch["label"],
            "content": content
        })
    result.append(vol_data)

# Write to a JS file that can be included
out = "const LIBRARY_DATA = " + json.dumps(result, ensure_ascii=False, indent=2) + ";\n"

with codecs.open(r'd:\novel\text-splitter-web\library_data.js', 'w', 'utf-8') as f:
    f.write(out)

print("Done! library_data.js created.")
total_chars = sum(len(ch["content"]) for vol in result for ch in vol["chapters"])
print(f"Total characters: {total_chars:,}")
