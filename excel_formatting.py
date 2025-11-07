from openpyxl import load_workbook

from openpyxl.styles import Font, PatternFill, Alignment


def enable_autofilter_all_sheets(excel_path):
    """
    Enable AutoFilter (dropdown arrows) for the header row in all sheets.

    Args:
        excel_path (str): Path to the Excel file to format.
    """
    # Load the workbook
    wb = load_workbook(excel_path)

    # Iterate through all sheets
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Enable AutoFilter on the entire data range starting from row 1
        # This automatically detects the data range and applies filter to headers
        if ws.max_row > 0 and ws.max_column > 0:
            ws.auto_filter.ref = ws.dimensions

    # Save the workbook
    wb.save(excel_path)
    print(f"✓ AutoFilter enabled for all sheets in: {excel_path}")


def format_all_headers(excel_path):
    """
    Format the header row (row 1) of all sheets in an Excel file.
    - Bold text
    - Yellow background
    - Calibri font, size 14
    - Center alignment

    Args:
        excel_path (str): Path to the Excel file to format.
    """
    # Load the workbook
    wb = load_workbook(excel_path)

    # Define header styling
    header_font = Font(name='Calibri', size=12, bold=True)
    header_fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')  # Yellow
    header_alignment = Alignment(horizontal='center', vertical='center')

    # Iterate through all sheets
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Apply formatting to all cells in row 1 (header row)
        for cell in ws[1]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment

    # Save the workbook
    wb.save(excel_path)
    print(f"✓ All headers formatted (bold, yellow, Calibri 14) in: {excel_path}")


def auto_resize_all_columns(excel_path):
    """
    Auto-resize all columns in all sheets of an Excel file to fit content width.

    Args:
        excel_path (str): Path to the Excel file to format.
    """
    # Load the workbook
    wb = load_workbook(excel_path)

    # Iterate through all sheets in the workbook
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Auto-resize each column based on content
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter  # Get the column letter (A, B, C, etc.)

            for cell in column:
                try:
                    # Calculate the maximum length of content in this column
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except:
                    pass

            # Set column width (add extra padding for readability)
            adjusted_width = max_length + 2
            ws.column_dimensions[column_letter].width = adjusted_width

    # Save the workbook with resized columns
    wb.save(excel_path)
    print(f"✓ All columns auto-resized in: {excel_path}")


def format_content_font_all_sheets(excel_path, font_name='Calibri', font_size=10):
    """
    Format the content (all rows except header row 1) in all sheets.
    Sets font to Calibri size 10 by default.

    Args:
        excel_path (str): Path to the Excel file to format.
        font_name (str): Font name (default: 'Calibri').
        font_size (int): Font size (default: 8).
    """
    # Load the workbook
    wb = load_workbook(excel_path)

    # Define content font
    content_font = Font(name=font_name, size=font_size)

    # Iterate through all sheets
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Apply font to all data rows (starting from row 2, skipping header)
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
            for cell in row:
                cell.font = content_font

    # Save the workbook
    wb.save(excel_path)
    print(f"✓ Content font set to {font_name} {font_size} in all sheets: {excel_path}")


def set_max_column_width(excel_path, column_name='Event_Details', max_width=50):
    """
    Set a maximum width for a specific column across all sheets.
    Useful for columns with long text content to prevent excessive stretching.

    Args:
        excel_path (str): Path to the Excel file to format.
        column_name (str): Name of the column to limit (default: 'Event_Details').
        max_width (int): Maximum width in Excel units (default: 50).
    """
    # Load the workbook
    wb = load_workbook(excel_path)

    # Iterate through all sheets
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Find the column letter for the target column name
        column_letter = None
        for cell in ws[1]:  # Header row
            if cell.value == column_name:
                column_letter = cell.column_letter
                break

        # If column found, set maximum width
        if column_letter:
            current_width = ws.column_dimensions[column_letter].width
            if current_width and current_width > max_width:
                ws.column_dimensions[column_letter].width = max_width

    # Save the workbook
    wb.save(excel_path)
    print(f"✓ Column '{column_name}' width limited to {max_width} in all sheets: {excel_path}")


def freeze_top_row_all_sheets(excel_path):
    """
    Freeze the top row (header row) in all sheets so it stays visible when scrolling vertically.

    Args:
        excel_path (str): Path to the Excel file to format.
    """
    # Load the workbook
    wb = load_workbook(excel_path)

    # Iterate through all sheets
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Freeze the top row by setting freeze_panes to A2
        ws.freeze_panes = 'A2'

    # Save the workbook
    wb.save(excel_path)
    print(f"✓ Top row frozen in all sheets: {excel_path}")


from openpyxl.styles import Alignment


def wrap_text_all_headers(excel_path):
    """
    Enable wrap text for all header rows (row 1) in all sheets.

    Args:
        excel_path (str): Path to the Excel file to format.
    """
    # Load the workbook
    wb = load_workbook(excel_path)

    # Iterate through all sheets
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Apply wrap text to all cells in row 1 (header row)
        for cell in ws[1]:
            cell.alignment = Alignment(
                horizontal=cell.alignment.horizontal if cell.alignment else 'center',
                vertical=cell.alignment.vertical if cell.alignment else 'center',
                wrapText=True
            )

    # Save the workbook
    wb.save(excel_path)
    print(f"✓ Wrap text enabled for all headers in: {excel_path}")
