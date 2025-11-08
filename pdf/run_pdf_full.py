from pdf_full_extract import extract_pdf_full
from make_sdlxliff import build_sdlxliff
from write_mapping import write_mapping
import os

# Get the project root directory (parent of pdf directory)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pdf_path = os.path.join(project_root, "input", "sample.pdf")
sdlx_output = os.path.join(project_root, "output", "pdf", "sample_full.sdlxliff")
json_output = os.path.join(project_root, "output", "pdf", "sample_full_map.json")

segments, mapping = extract_pdf_full(pdf_path)

# Build SDLXLIFF
build_sdlxliff(segments, sdlx_output, original_filename=pdf_path, translatable=True)

# Write JSON mapping
write_mapping(mapping, json_output, source_file=pdf_path, scope="full_text")
