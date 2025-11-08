from lxml import etree
import os

SDL_NS = "http://sdl.com/FileTypes/SdlXliff/1.0"
NSMAP = {"sdl": SDL_NS}


def build_sdlxliff(segments, output_path, original_filename, translatable=True):
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
        **{"source-language": "en-CA", "target-language": "fr-CA"}
    )
    body = etree.SubElement(file_el, "body")

    for seg_id, text in segments:
        tu = etree.SubElement(
            body, "trans-unit", id=seg_id, translate="yes" if translatable else "no"
        )

        src = etree.SubElement(tu, "source")
        src.text = text

    etree.ElementTree(root).write(
        output_path, pretty_print=True, encoding="utf-8", xml_declaration=True
    )
