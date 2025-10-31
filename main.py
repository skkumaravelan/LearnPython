from log_splitter_logics_modular import firstSplitWith_ApplicationLogger_str,secondSplitWith_eventcodeAMH_str_MOD
from write_to_excel import write_dictionary_txt_to_excel

if __name__ == "__main__":
    input_filename = r"S:\LearnPython\txt_files_inventory\input.txt"
    output_filename = r"S:\LearnPython\txt_files_inventory\output.txt"
    dictionary_format_output_filename = r"S:\LearnPython\txt_files_inventory\dictionary.txt"
    excel_format_output_filename = r"S:\LearnPython\log_output.xlsx"


    firstSplitWith_ApplicationLogger_str(input_filename, output_filename)
    secondSplitWith_eventcodeAMH_str_MOD(output_filename, dictionary_format_output_filename)
    write_dictionary_txt_to_excel(dictionary_format_output_filename,excel_format_output_filename)

