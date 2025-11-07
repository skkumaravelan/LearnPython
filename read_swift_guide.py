from bs4 import BeautifulSoup
from numpy.testing.print_coercion_tables import print_new_cast_table
from openpyxl import Workbook


from bs4 import BeautifulSoup
from openpyxl import load_workbook


def read_swift_guide_and_write_to_excel(html_file_path, input_excel_path):
    """
    Reads event codes from Sheet2 column A (from A2 down to last non-empty),
    extracts details from HTML file, and writes results to Sheet3 of same Excel file.

    Args:
        html_file_path (str): Path to the HTML guide file.
        input_excel_path (str): Path to the Excel file with event codes and output target.
    """
    # Load workbook and select Sheet2 for reading event codes
    wb = load_workbook(input_excel_path)
    ws1 = wb["Sheet2"]

    # Read event codes from column A starting at row 2 until blank or None
    event_codes = []
    row = 2
    while True:
        cell_value = ws1[f"A{row}"].value
        if cell_value is None or str(cell_value).strip() == "":
            break
        event_codes.append(str(cell_value).strip())
        row += 1

    # ===== FIXED: Parse the HTML file with robust matching =====
    with open(html_file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    code_map = {}

    for table in soup.find_all("table"):
        log_code = None
        log_message = None
        description = None

        for tr in table.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) >= 2:
                key = tds[0].get_text(strip=True)
                value = tds[1].get_text(strip=True)

                # Make matching case-insensitive and more flexible
                key_lower = key.lower()
                value_lower = value.lower()

                # Match log code (flexible: looks for "code" in key AND "amh" in value)
                if (("code" in key_lower and "amh" in value_lower) or
                        ("event" in key_lower and "code" in key_lower) or
                        ("id" in key_lower and "amh" in value_lower)):
                    log_code = value.strip()

                # Match log message
                elif "message" in key_lower:
                    log_message = value.strip()

                # Match description
                elif "description" in key_lower:
                    description = value.strip()

        # Only add to map if we found a log_code
        if log_code:
            code_map[log_code] = (log_message or "", description or "")

    # ✅ DEBUG: Print the code_map to verify it's populated
    print(f"\n✓ Parsed {len(code_map)} codes from HTML file")
    if len(code_map) > 0:
        print(f"  Sample codes: {list(code_map.keys())[:3]}")
    else:
        print("  ⚠ WARNING: No codes found in HTML file!")
        print("  Debugging first table structure...")
        # Print first table structure for debugging
        first_table = soup.find("table")
        if first_table:
            print("\n  First 5 rows of first table:")
            for i, tr in enumerate(first_table.find_all("tr")[:5]):
                tds = tr.find_all("td")
                if tds:
                    print(f"    Row {i}: {[td.get_text(strip=True)[:50] for td in tds]}")

    # ===== END FIX =====

    # Gather output data for found codes
    output_data = []
    placeholder = "Data not available in Official SWIFT Log Guide"

    for code in event_codes:
        # Clean the code by removing brackets for lookup
        clean_code = code.replace("[", "").replace("]", "").strip()

        # Get message and description from code_map, use placeholder if not found
        if clean_code in code_map:
            message, desc = code_map[clean_code]
            # If either message or description is empty/missing, use placeholder
            message = message if message else placeholder
            desc = desc if desc else placeholder
        else:
            # Code not found in HTML at all
            message = placeholder
            desc = placeholder

        # ✅ Use clean_code (without brackets) in output
        output_data.append((clean_code, message, desc))

    # Write data to Sheet3 (overwrite if exists)
    if "Sheet3" in wb.sheetnames:
        ws3 = wb["Sheet3"]
        wb.remove(ws3)
    ws3 = wb.create_sheet("Sheet3")
    ws3.append(["AMH_Event_Log_Code", "Log Message", "Description"])
    for row_data in output_data:
        ws3.append(row_data)

    # Save workbook
    wb.save(input_excel_path)
    print(f"Wrote {len(output_data)} Log Code details to Sheet3 of {input_excel_path}")
