import json
import os


def write_mapping(mapping, json_path, source_file, scope):
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(json_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    data = {"source_file": source_file, "scope": scope, "segments": mapping}

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
