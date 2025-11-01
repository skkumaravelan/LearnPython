import os
from dotenv import load_dotenv

from log_splitter_logics_modular import (
    firstSplitWith_ApplicationLogger_str_DynamicFileName,
    secondSplitWith_eventcodeAMH_str_DynamicFileName
)
from write_to_excel import write_all_dictionary_txts_to_single_excel

# Load from .env file
load_dotenv()

if __name__ == "__main__":
    input_dir = os.getenv("INPUT_DIR", r"S:\LearnPython\inputs")
    middle_process_dir = os.getenv("MIDDLE_PROCESS_DIR", r"S:\LearnPython\middle-processes")
    output_dir = os.getenv("OUTPUT_DIR", r"S:\LearnPython\output")

    # Create directories if not exist
    for folder in [input_dir, middle_process_dir, output_dir]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

    # Proceed with your existing pipeline:
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            firstSplitWith_ApplicationLogger_str_DynamicFileName(input_path, middle_process_dir)

    for filename in os.listdir(middle_process_dir):
        if filename.startswith("first_split_") and filename.endswith(".txt"):
            input_path = os.path.join(middle_process_dir, filename)
            orig_part = os.path.splitext(filename)[0].replace("first_split_", "")
            output_filename = f"dictionaryFormat_{orig_part}.txt"
            output_path = os.path.join(middle_process_dir, output_filename)
            secondSplitWith_eventcodeAMH_str_DynamicFileName(input_path, output_path)

    output_excel_path = os.path.join(output_dir, "all_logs.xlsx")
    write_all_dictionary_txts_to_single_excel(middle_process_dir, output_excel_path)
