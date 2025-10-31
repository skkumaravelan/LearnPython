import pandas as pd

def write_dictionary_txt_to_excel(input_txt_path, output_excel_path):
    event_codes = []
    statuses = []
    contents = []

    with open(input_txt_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(":::::")
            if len(parts) == 3:
                event_code, status, content = parts
            else:
                # Handle malformed lines gracefully by filling empty or default values
                event_code = parts[0] if len(parts) > 0 else "UNKNOWN"
                status = parts[1] if len(parts) > 1 else "UNKNOWN"
                content = parts[2] if len(parts) > 2 else ""

            event_codes.append(event_code)
            statuses.append(status)
            contents.append(content)

    # Create DataFrame for easy Excel export
    df = pd.DataFrame({
        "Event Code": event_codes,
        "Status": statuses,
        "Content": contents
    })

    # Write to Excel file
    df.to_excel(output_excel_path, index=False)

    print(f"Excel file '{output_excel_path}' created successfully with {len(df)} records.")

# Example usage:
# write_dictionary_txt_to_excel(r"S:\LearnPython\txt_files_inventory\dictionary.txt",
#                               r"S:\LearnPython\txt_files_inventory\log_output.xlsx")
