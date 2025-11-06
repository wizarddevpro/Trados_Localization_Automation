from lxml import etree
import os

SDL_NS = "http://sdl.com/FileTypes/SdlXliff/1.0"
NSMAP = {"sdl": SDL_NS}


def build_sdlxliff(sentences, output_path, original_filename):
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    root = etree.Element("xliff", version="1.2", nsmap=NSMAP)
    file_el = etree.SubElement(
        root,
        "file",
        original=original_filename,
        datatype="x-sdlfilterframework2",
        **{"source-language": "en-US", "target-language": "en-US"},
    )
    body = etree.SubElement(file_el, "body")

    for idx, text in enumerate(sentences, start=1):
        seg_id = f"docx_s{idx}"

        tu = etree.SubElement(
            body, "trans-unit", id=seg_id, translate="yes"
        )  # translatable

        src = etree.SubElement(tu, "source")
        src.text = text

    tree = etree.ElementTree(root)
    tree.write(output_path, pretty_print=True, encoding="utf-8", xml_declaration=True)

    print(f"SDLXLIFF written → {output_path}")
