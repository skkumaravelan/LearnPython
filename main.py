import os
from log_splitter_logics_modular import (
    firstSplitWith_ApplicationLogger_str_DynamicFileName,
    secondSplitWith_eventcodeAMH_str_DynamicFileName
)
from write_to_excel import write_all_dictionary_txts_to_single_excel

if __name__ == "__main__":
    input_dir = r"S:\LearnPython\inputs"
    middle_process_dir = r"S:\LearnPython\middle-process"
    output_dir = r"S:\LearnPython\output"

    # 1. First split loop
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            firstSplitWith_ApplicationLogger_str_DynamicFileName(input_path, middle_process_dir)

    # 2. Second split loop
    for filename in os.listdir(middle_process_dir):
        if filename.startswith("first_split_") and filename.endswith(".txt"):
            input_path = os.path.join(middle_process_dir, filename)
            base_name = os.path.splitext(filename)[0]
            orig_part = base_name.replace("first_split_", "")
            output_filename = f"dictionaryFormat_{orig_part}.txt"
            output_path = os.path.join(middle_process_dir, output_filename)
            secondSplitWith_eventcodeAMH_str_DynamicFileName(input_path, output_path)

    # 3. Write all dictionaryFormat files to a single Excel
    output_excel_path = os.path.join(output_dir, "all_logs.xlsx")
    write_all_dictionary_txts_to_single_excel(middle_process_dir, output_excel_path)
