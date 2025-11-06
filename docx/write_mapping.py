import json
import os


def write_mapping(sentences, json_path):
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(json_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    data = {"segments": []}

    for idx, text in enumerate(sentences, start=1):
        seg = {
            "seg_id": f"docx_s{idx}",
            "page": "docx",  # DOCX has no true pages
            "section": "highlight",  # Optional but useful
            "text_preview": text[:50],
        }
        data["segments"].append(seg)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"JSON mapping written → {json_path}")
