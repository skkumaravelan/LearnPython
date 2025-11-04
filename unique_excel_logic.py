import pandas as pd
import os

def extract_unique_eventcodes(input_excel_path):
    # Read input Excel
    df = pd.read_excel(input_excel_path)

    # Store unique EventCodes in a set for later use
    unique_eventcodes = set(df['Event_Code'])

    # For each unique Event_Code, keep only one (random) row
    unique_rows_df = df.groupby('Event_Code', as_index=False).first()

    # Output path for new Excel file
    folder = os.path.dirname(input_excel_path)
    output_excel_path = os.path.join(folder, 'uniqueEventCodes.xlsx')
    unique_rows_df.to_excel(output_excel_path, index=False)

    print(f"Unique EventCodes: {unique_eventcodes}")
    print(f"File written: {output_excel_path}")

    return unique_eventcodes, output_excel_path
