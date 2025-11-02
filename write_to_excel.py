import pandas as pd
import os
# def write_dictionary_txt_to_excel(input_txt_path, output_excel_path, logdate_val):
#     rows = []
#
#     with open(input_txt_path, "r", encoding="utf-8") as file:
#         for line in file:
#             parts = line.strip().split(":::::")
#             if len(parts) == 3:
#                 event_code, status, content = parts
#             else:
#                 event_code = parts[0] if len(parts) > 0 else "UNKNOWN"
#                 status = parts[1] if len(parts) > 1 else "UNKNOWN"
#                 content = parts[2] if len(parts) > 2 else ""
#
#             row = {
#                 "LogDate": logdate_val,
#                 "Matching_Scenario": "",
#                 "Event_Code": event_code,
#                 "Status": status,
#                 "Event_Details": content
#             }
#             rows.append(row)
#
#     df = pd.DataFrame(rows)
#     df.to_excel(output_excel_path, index=False)
#
#     print(f"Excel file '{output_excel_path}' created successfully with {len(df)} records.")

import os
import pandas as pd

def write_all_dictionary_txts_to_single_excel(middle_process_dir, output_excel_path):
    all_rows = []

    # Loop through all relevant txt files in middle_process_dir
    for filename in os.listdir(middle_process_dir):
        if filename.startswith("dictionaryFormat_") and filename.endswith(".txt"):
            input_txt_path = os.path.join(middle_process_dir, filename)
            logdate_val = os.path.splitext(filename)[0].replace("dictionaryFormat_", "")

            with open(input_txt_path, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(":::::")
                    if len(parts) == 3:
                        event_code, status, content = parts
                    else:
                        event_code = parts[0] if len(parts) > 0 else "UNKNOWN"
                        status = parts[1] if len(parts) > 1 else "UNKNOWN"
                        content = parts[2] if len(parts) > 2 else ""

                    row = {
                        "LogDate": logdate_val,
                        "Matching_Scenario": "",
                        "Event_Code": event_code,
                        "Status": status,
                        "Event_Details": content
                    }
                    all_rows.append(row)

    df = pd.DataFrame(all_rows)

    # Remove trailing '-N' from LogDate and convert to pandas date type (datetime64[ns])
    df['LogDate'] = df['LogDate'].str.extract(r'(\d{4}-\d{2}-\d{2})')
    df['LogDate'] = pd.to_datetime(df['LogDate'], format='%Y-%m-%d') # TRUE date type for SNOW/Excel

    # Export to Excel (Excel will keep LogDate as a date value with time omitted visually)
    df.to_excel(output_excel_path, index=False)
    print(f"Combined Excel file '{output_excel_path}' created with {len(df)} records.")

