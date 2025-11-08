from excel_process import process_excel
from excel_mapping import excel_mapping
from excel_to_sdlxliff import excel_to_sdlxliff
import os

# Get the project root directory (parent of excel directory)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_excel = os.path.join(project_root, "input", "sample.xlsx")
output_excel = os.path.join(project_root, "output", "xlsx", "translated.xlsx")
json_output = os.path.join(project_root, "output", "xlsx", "sample_map.json")
sdlxliff_output = os.path.join(project_root, "output", "xlsx", "sample.sdlxliff")

# Step 1: Process Excel (D → E)
process_excel(input_excel, output_excel)

# Step 2: Build mapping JSON
excel_mapping(output_excel, json_output)

# Step 3 (optional): Build SDLXLIFF for Column D
excel_to_sdlxliff(input_excel, sdlxliff_output)
