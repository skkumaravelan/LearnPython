# import pandas as pd
# from openpyxl import load_workbook
# from openpyxl.styles import Font
#
#
# def create_merged_sheet4(excel_path):
#     """
#     Create Sheet4 by merging Sheet2 and Sheet3 on the Event_Code column.
#
#     Sheet4 columns order:
#     1. AMH_Event_Log_Code (common key)
#     2. Status (from Sheet2)
#     3. Priority (empty - to be configured manually)
#     4. Impact (empty - to be configured manually)
#     5. Urgency (empty - to be configured manually)
#     6. Threshold (empty - to be configured manually)
#     7. Log Message (from Sheet3)
#     8. Description (from Sheet3)
#
#     Args:
#         excel_path (str): Path to the Excel file containing Sheet2 and Sheet3.
#     """
#     # Read Sheet2 and Sheet3 using pandas
#     sheet2_df = pd.read_excel(excel_path, sheet_name='Sheet2')
#     sheet3_df = pd.read_excel(excel_path, sheet_name='Sheet3')
#
#     # Merge on the common column (inner join to keep only matching codes)
#     merged_df = pd.merge(
#         sheet2_df[['AMH_Event_Log_Code', 'Status']],
#         sheet3_df[['AMH_Event_Log_Code', 'Log Message', 'Description']],
#         on='AMH_Event_Log_Code',
#         how='inner'
#     )
#
#     # Add new empty columns for manual configuration
#     merged_df['Priority'] = ''
#     merged_df['Impact'] = ''
#     merged_df['Urgency'] = ''
#     merged_df['Threshold'] = ''
#
#     # Reorder columns as specified
#     merged_df = merged_df[[
#         'AMH_Event_Log_Code',
#         'Status',
#         'Priority',
#         'Impact',
#         'Urgency',
#         'Threshold',
#         'Log Message',
#         'Description'
#     ]]
#
#     # Write to Excel
#     with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#         merged_df.to_excel(writer, sheet_name='Sheet4', index=False)
#
#     # Now format the headers with guidance text using openpyxl
#     wb = load_workbook(excel_path)
#     ws = wb['Sheet4']
#
#     # Define header guidance mapping (column name -> guidance text)
#     header_guidance = {
#         'Priority': 'Priority\n(High, Low, Medium)',
#         'Impact': 'Impact\n(High, Low, Medium)',
#         'Urgency': 'Urgency\n(High, Low, Medium)',
#         'Threshold': 'Threshold\n(<10, <50)'
#     }
#
#     # Apply guidance text and formatting to specific headers
#     for col_idx, cell in enumerate(ws[1], start=1):
#         col_name = cell.value
#         if col_name in header_guidance:
#             # Set the header text with guidance
#             cell.value = header_guidance[col_name]
#             # Enable text wrapping (will be handled by existing formatting)
#             cell.alignment = cell.alignment.copy(wrapText=True)
#
#     # Save the workbook
#     wb.save(excel_path)
#
#     print(f"✓ Sheet4 created by merging Sheet2 and Sheet3: {excel_path}")
#     print(f"  Total merged rows: {len(merged_df)}")
#     print(f"  Columns: AMH_Event_Log_Code, Status, Priority, Impact, Urgency, Threshold, Log Message, Description")
