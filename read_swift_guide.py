from bs4 import BeautifulSoup
from openpyxl import Workbook

def extract_log_details_to_excel(html_file_path, log_code_txt_path, output_excel_path):
    # Read log codes from txt and clean brackets
    with open(log_code_txt_path, "r", encoding="utf-8") as f:
        event_codes = [line.strip().replace("[", "").replace("]", "") for line in f if line.strip()]

    # 2. Parse the HTML just once into a dict for fast lookup
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
                if "Log Code" in key:
                    log_code = value
                elif "Log Message" in key:
                    log_message = value
                elif "Description" in key:
                    description = value
        if log_code:
            code_map[log_code] = (log_message, description)

    # 3. Gather output rows for the codes in txt
    output_data = []
    for code in event_codes:
        message, desc = code_map.get(code, ("", ""))
        output_data.append((code, message, desc))

    # 4. Write to Excel in one go
    wb = Workbook()
    ws = wb.active
    ws.title = "LogCodeDetails"
    ws.append(["Log Code", "Log Message", "Description"])
    for row in output_data:
        ws.append(row)
    wb.save(output_excel_path)
    print(f"Wrote {len(output_data)} Log Code details to {output_excel_path}")

# Usage:
# extract_log_details_to_excel(
#     "AMHApplicationLogGuide.html",
#     "codes.txt",
#     "LogCodeMessageDescriptions.xlsx"
# )
