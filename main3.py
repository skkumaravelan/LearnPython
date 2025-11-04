from read_swift_guide import extract_log_details_to_excel

# Input paths
# html_path = r"AMHApplicationLogGuide.html"
# input_path = r"F:\logsanalyser\uniqueEventLogCodes.txt"
# output_excel_path = r"F:\logsanalyser\LogCodeMessageDescriptions.xlsx"
html_path = r"P:\AMHApplicationLogGuide.html"
input_path = r"P:\uniqueEventLogCodes.txt"

output_excel_path =  r"P:\output_from_swift_guide.xlsx"


extract_log_details_to_excel(html_path, input_path, output_excel_path)
