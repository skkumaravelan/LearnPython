from collections import defaultdict
import re

def firstSplitWith_ApplicationLogger_str(input_filename, output_filename):
    entries = []
    with open(input_filename, "r", encoding="utf-8") as infile:
        for line in infile:
            if 'chnl:ApplicationLogger' in line:
                parts = line.split('chnl:ApplicationLogger', 1)
                if len(parts) > 1:
                    extracted = parts[1].strip()
                    entries.append(extracted)

    result_tuple = tuple(entries)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        for entry in result_tuple:
            outfile.write(entry + "\n")

    print(f"Extraction complete. {len(result_tuple)} entries written to {output_filename}")




# def secondSplitWith_eventcodeAMH_str_ALL(input_filename, output_filename):
#     event_dict = defaultdict(list)
#     log_level_pattern = re.compile(r'\b(INFO|WARN|ERROR|DEBUG|TRACE|FATAL|CRIT|WARNING)\b', re.IGNORECASE)
#     amh_pattern = re.compile(r'\[AMH-.*')  # Match substring starting with [AMH-
#
#
#     with open(input_filename, "r", encoding="utf-8") as infile:
#         for line in infile:
#             if 'eventcode.AMH' in line:
#                 key_match = log_level_pattern.search(line)
#                 if key_match:
#                     key = key_match.group(1).upper()
#                 else:
#                     key = "UNKNOWN"
#
#                 parts = line.split('eventcode.AMH', 1)
#                 value_full = parts[1].strip() if len(parts) > 1 else ''
#                 # Extract only the part starting from '[AMH-'
#                 amh_match = amh_pattern.search(value_full)
#                 if amh_match:
#                     value = amh_match.group()
#                 else:
#                     # If no '[AMH-' substring, keep the full trimmed value or skip
#                     value = value_full
#                 event_dict[key].append(value)
#
#     with open(output_filename, "w", encoding="utf-8") as outfile:
#         for key, values in event_dict.items():
#             for value in values:
#                 outfile.write(f"{key} : {value}\n")
#
#     total_entries = sum(len(v) for v in event_dict.values())
#     print(f"Extraction complete. {total_entries} key-value pairs written to {output_filename}")

def secondSplitWith_eventcodeAMH_str_MOD(input_filename, output_filename):
    event_dict = defaultdict(list)
    log_level_pattern = re.compile(r'\b(INFO|WARN|ERROR|DEBUG|TRACE|FATAL|CRIT|WARNING)\b', re.IGNORECASE)
    amh_code_pattern = re.compile(r'(\[AMH-[^\]]+\])')

    with open(input_filename, "r", encoding="utf-8") as infile:
        for line in infile:
            if 'eventcode.AMH' in line:
                # Extract log level key
                key_match = log_level_pattern.search(line)
                log_level = key_match.group(1).upper() if key_match else "UNKNOWN"

                # Extract part after eventcode.AMH
                parts = line.split('eventcode.AMH', 1)
                value_full = parts[1].strip() if len(parts) > 1 else ''

                # Extract [AMH-xxxx] code if exists
                amh_match = amh_code_pattern.search(value_full)
                if amh_match:
                    amh_code = amh_match.group(1)
                    # Remove the amh_code part from the message text to avoid duplication
                    message = value_full.replace(amh_code, "").strip()
                else:
                    amh_code = "No_AMH_Log_Code"
                    message = value_full

                # Construct combined string with triple parts joined by ':::::'
                combined = f"{amh_code}:::::{log_level}:::::{message}"
                event_dict[log_level].append(combined)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        for _, combined_values in event_dict.items():
            for combined in combined_values:
                outfile.write(combined + "\n")

    total_entries = sum(len(v) for v in event_dict.values())
    print(f"Extraction complete. {total_entries} lines written to {output_filename}")


