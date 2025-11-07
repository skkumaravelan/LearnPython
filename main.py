import os
from dotenv import load_dotenv

from log_splitter_logics_modular import (
    firstSplitWith_ApplicationLogger_str_DynamicFileName,
    secondSplitWith_eventcodeAMH_str_DynamicFileName
)
from write_to_excel import write_all_dictionary_txts_to_single_excel
from console_logger import enable_console_logging  # ← ADD THIS IMPORT


# Load from .env file
load_dotenv()

if __name__ == "__main__":
    input_dir = os.getenv("INPUT_DIR", r"S:\LearnPython\inputs")
    middle_process_dir = os.getenv("MIDDLE_PROCESS_DIR", r"S:\LearnPython\middle-process")
    output_dir = os.getenv("OUTPUT_DIR", r"S:\LearnPython\outputs")

    # ===== ENABLE CONSOLE LOGGING (comment out to disable) =====
    logger = enable_console_logging(output_dir)  # ← ADD THIS LINE

    print("\n" + "*" * 20 + "\n")

    # Create folders if they don't exist
    for folder in [input_dir, middle_process_dir, output_dir]:
        os.makedirs(folder, exist_ok=True)
        print(f"Ensured folder exists: {folder}")

    print("\n" + "*" * 20 + "\n")


    # First split
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            firstSplitWith_ApplicationLogger_str_DynamicFileName(input_path, middle_process_dir)

    print("\n" + "*" * 20 + "\n")

    # Second split
    for filename in os.listdir(middle_process_dir):
        if filename.startswith("first_split_") and filename.endswith(".txt"):
            input_path = os.path.join(middle_process_dir, filename)
            orig_part = os.path.splitext(filename)[0].replace("first_split_", "")
            output_filename = f"dictionaryFormat_{orig_part}.txt"
            output_path = os.path.join(middle_process_dir, output_filename)
            secondSplitWith_eventcodeAMH_str_DynamicFileName(input_path, output_path)

    print("\n" + "*" * 20 + "\n")

    # Write all to one Excel
    output_excel_path = os.path.join(output_dir, "all_logs.xlsx")
    write_all_dictionary_txts_to_single_excel(middle_process_dir, output_excel_path)


#----------------------------------------------------------------
# Extract unique EventCodes and write to Sheet2 of the same file

from unique_excel_logic import extract_unique_eventcodes
unique_eventcodes, _ = extract_unique_eventcodes(output_excel_path, True)


#----------------------------------------------------------------
# Read Official SWIFT Guide and get Log Details and Write to Sheet3

from read_swift_guide import read_swift_guide_and_write_to_excel
from sheet_merger import  create_merged_sheet4

# Path to your HTML guide file (update as per your actual path)
html_guide_path = r"S:\LearnPython\inputs\AMHApplicationLogGuide.html"

# Call the method to read codes from Sheet2 of all_logs.xlsx and write details to Sheet3
read_swift_guide_and_write_to_excel(html_guide_path, output_excel_path)

# Create Sheet4 by merging Sheet2 and Sheet3
create_merged_sheet4(output_excel_path)
#----------------------------------------------------------------
from excel_formatting import (
    format_all_headers, auto_resize_all_columns, enable_autofilter_all_sheets,
    format_content_font_all_sheets, set_max_column_width, freeze_top_row_all_sheets,
    wrap_text_all_headers, rename_sheets
)

# ===== FORMATTING STEPS (apply to ALL sheets including Sheet4) =====
print(f"\nApplying formatting to: {output_excel_path}\n")

# Formatting step 1: Format headers (bold, yellow, Calibri 12)
format_all_headers(output_excel_path)

# Formatting step 1.5: Enable wrap text for all headers
wrap_text_all_headers(output_excel_path)

# Formatting step 2: Format content rows (Calibri 10)
format_content_font_all_sheets(output_excel_path, font_size=10)

# Formatting step 3: Auto-resize columns to fit content
auto_resize_all_columns(output_excel_path)

# Formatting step 3.5: Limit Event_Details column width (if exists in any sheet)
set_max_column_width(output_excel_path, column_name='Event_Details', max_width=50)

# Formatting step 4: Enable AutoFilter dropdowns on headers
enable_autofilter_all_sheets(output_excel_path)

# Formatting step 5: Freeze top row for easy scrolling
freeze_top_row_all_sheets(output_excel_path)

# Formatting step 6: Rename sheets to meaningful names
sheet_names = {
    'Sheet1': 'All_Logs',
    'Sheet2': 'Unique_EventCodes',
    'Sheet3': 'Log_Details_From_SWIFT',
    'Sheet4': 'Merged_Summary'
}
rename_sheets(output_excel_path, sheet_names)

print(f"\n{'*' * 20}\n")
print(f"✓ All processing complete!")
print(f"✓ Excel file ready: {output_excel_path}\n")
print(f"  📊 Sheets:")
print(f"     • All_Logs: All log entries")
print(f"     • Unique_EventCodes: Unique event codes extracted")
print(f"     • Log_Details_From_SWIFT: Log messages and descriptions from official guide")
print(f"     • Merged_Summary: Event codes with status, priority fields, and details\n")
print(f"  🎨 Formatting:")
print(f"     • Headers: Bold, Yellow, Calibri 12, Wrap Text Enabled")
print(f"     • Content: Calibri 10")
print(f"     • Columns: Auto-resized for readability")
print(f"     • Event_Details column: Limited to max width 50")
print(f"     • AutoFilter: Enabled for easy filtering")
print(f"     • Top row: Frozen for easy vertical scrolling")
#--------------------------------------------------------------------------------

# ===== STOP CONSOLE LOGGING AND GET RUNTIME =====
runtime = logger.stop()  # Returns runtime in seconds

# Format and display runtime
if runtime < 60:
    runtime_display = f"{runtime:.2f} seconds"
else:
    minutes = int(runtime // 60)
    seconds = runtime % 60
    runtime_display = f"{minutes} min {seconds:.2f} sec"

print(f"\n⏱️  Total runtime: {runtime_display}")
print(f"✓ Console output saved to: {os.path.join(output_dir, 'console_output.txt')}")
# ----------------------------------------------------------------