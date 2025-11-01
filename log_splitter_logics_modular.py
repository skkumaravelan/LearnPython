from collections import defaultdict
import re
import os

# def firstSplitWith_ApplicationLogger_str(input_filename, output_filename):
#     entries = []
#     with open(input_filename, "r", encoding="utf-8") as infile:
#         for line in infile:
#             if 'chnl:ApplicationLogger' in line:
#                 parts = line.split('chnl:ApplicationLogger', 1)
#                 if len(parts) > 1:
#                     extracted = parts[1].strip()
#                     entries.append(extracted)
#
#     result_tuple = tuple(entries)
#
#     with open(output_filename, "w", encoding="utf-8") as outfile:
#         for entry in result_tuple:
#             outfile.write(entry + "\n")
#
#     print(f"Extraction complete. {len(result_tuple)} entries written to {output_filename}")


import os

import os

def firstSplitWith_ApplicationLogger_str_DynamicFileName(input_path, output_dir):
    base_name = os.path.basename(input_path)
    name_without_ext = os.path.splitext(base_name)[0]
    output_filename = f"first_split_{name_without_ext}.txt"
    output_path = os.path.join(output_dir, output_filename)

    count = 0
    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            if 'chnl:ApplicationLogger' in line:
                # Only write the portion after the marker, if any
                parts = line.split('chnl:ApplicationLogger', 1)
                if len(parts) > 1:
                    extracted = parts[1].strip()
                    outfile.write(extracted + "\n")
                    count += 1

    print(f"Extraction complete. {count} entries written to {output_path}")




import re

def secondSplitWith_eventcodeAMH_str_DynamicFileName(input_filename, output_filename):
    log_level_pattern = re.compile(r'\b(INFO|WARN|ERROR|DEBUG|TRACE|FATAL|CRIT|WARNING)\b', re.IGNORECASE)
    amh_code_pattern = re.compile(r'(\[AMH-[^\]]+\])')

    count = 0
    with open(input_filename, "r", encoding="utf-8") as infile, \
         open(output_filename, "w", encoding="utf-8") as outfile:
        for line in infile:
            if 'eventcode.AMH' in line:
                key_match = log_level_pattern.search(line)
                log_level = key_match.group(1).upper() if key_match else "UNKNOWN"

                parts = line.split('eventcode.AMH', 1)
                value_full = parts[1].strip() if len(parts) > 1 else ''

                amh_match = amh_code_pattern.search(value_full)
                if amh_match:
                    amh_code = amh_match.group(1)
                    message = value_full.replace(amh_code, "").strip()
                else:
                    amh_code = "No_AMH_Log_Code"
                    message = value_full

                combined = f"{amh_code}:::::{log_level}:::::{message}"
                outfile.write(combined + "\n")
                count += 1

    print(f"Extraction complete. {count} lines written to {output_filename}")


