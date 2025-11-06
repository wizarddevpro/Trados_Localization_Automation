from extract_docx_yellow import extract_yellow_sentences
from make_sdlxliff import build_sdlxliff
from write_mapping import write_mapping

docx_input = "../input/sample.docx"
sdlx_output = "../output/docx/sample.sdlxliff"
json_output = "../output/docx/sample_map.json"

# 1. Extract yellow-highlight text
sentences = extract_yellow_sentences(docx_input)

# 2. Build SDLXLIFF
build_sdlxliff(sentences, sdlx_output, original_filename=docx_input)

# 3. Write mapping JSON
write_mapping(sentences, json_output)
