import pandas as pd
import os

import pandas as pd
import os


def extract_unique_eventcodes(input_excel_path, output_to_same_file=True):
    """
    Extract unique EventCodes from an Excel file and write the results either
    to a new Excel file or to Sheet2 of the same input Excel file.

    Args:
        input_excel_path (str): Path to the input Excel file containing logs.
        output_to_same_file (bool): If True, writes to Sheet2 of the input file;
                                    if False, creates a new file with unique EventCodes.

    Returns:
        tuple: A set of unique EventCodes and the path to the Excel file where output is saved.
    """
    # Read the entire input Excel file into a DataFrame
    df = pd.read_excel(input_excel_path)

    # Extract unique Event_Code values from the DataFrame
    unique_eventcodes = set(df['AMH_Event_Log_Code'])

    # Keep only the first occurrence of each unique Event_Code in the DataFrame
    unique_rows_df = df.groupby('AMH_Event_Log_Code', as_index=False).first()

    if output_to_same_file:
        # If set to True , then control comes here to write in 'Sheet2' of the same excel file.
        # Append unique rows to Sheet2 of the existing input Excel file (overwrite if Sheet2 exists)
        with pd.ExcelWriter(input_excel_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            unique_rows_df.to_excel(writer, sheet_name='Sheet2', index=False)

        # Set the output path as the original input file path since it was updated in place
        output_excel_path = input_excel_path
        print(f"Unique EventCodes written to Sheet2 of: {output_excel_path}")
    else:
        # If not writing to the same file, create a new Excel file in the same folder
        folder = os.path.dirname(input_excel_path)
        output_excel_path = os.path.join(folder, 'uniqueEventCodes.xlsx')

        # Write unique rows DataFrame to new Excel file
        unique_rows_df.to_excel(output_excel_path, index=False)
        print(f"File written: {output_excel_path}")

    # Print count of unique EventCodes processed
    print(f"Unique EventCodes count: {len(unique_eventcodes)}")

    # Return the set of unique EventCodes and the path to the saved Excel file
    return unique_eventcodes, output_excel_path


def extract_unique_eventcodes_bkp(input_excel_path):
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
