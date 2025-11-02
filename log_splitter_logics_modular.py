def get_date_part_from_filename(filename):
    """
    Extract the date-like substring from the filename.
    e.g. from 'amh_application-2025-10-16-1.log' extract '2025-10-16-1'
    """
    base_name = os.path.splitext(os.path.basename(filename))[0]
    # Remove 'amh_application-' if present
    base_name = base_name.replace("amh_application-", "")
    # If still more prefix, strip all before first number (for generalization)
    match = re.search(r'(\d{4}-\d{2}-\d{2})(?:-\d+)?$', base_name)
    if match:
        return match.group(1)  # Returns only '2025-10-20'
    else:
        return base_name


import os

def firstSplitWith_ApplicationLogger_str_DynamicFileName(input_path, output_dir):
    # Use new method to extract date part for output filename
    date_part = get_date_part_from_filename(input_path)
    output_filename = f"first_split_{date_part}.txt"
    output_path = os.path.join(output_dir, output_filename)

    count = 0
    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            if 'chnl:ApplicationLogger' in line:
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