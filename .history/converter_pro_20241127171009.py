import pandas as pd
import re

def dms_to_decimal(dms):
    """
    Convert DMS (Degrees, Minutes, Seconds) to Decimal Degrees (DD).
    DMS format: 40°23'107.2
    Decimal Degree format: 40.385333 (example)
    """
    # Match DMS format (degrees, minutes, seconds)
    pattern = r'(\d+)[°](\d+)[\'](\d+(\.\d+)?)'
    match = re.match(pattern, dms)
    
    if match:
        degrees = float(match.group(1))
        minutes = float(match.group(2))
        seconds = float(match.group(3))
        # Convert to decimal degrees: DD = degrees + (minutes/60) + (seconds/3600)
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return decimal
    else:
        return None  # If not in valid DMS format

def process_file(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(format.xlsx)
    
    # Convert Latitude and Longitude from DMS to Decimal Degrees
    df['Latitude'] = df['Latitude'].apply(dms_to_decimal)
    df['Longitude'] = df['Longitude'].apply(dms_to_decimal)
    
    # Save the updated DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

# Input and output file paths
input_file = 'format.xlsx'  # Replace with your input file name
output_file = 'output_file.xlsx'  # Replace with your desired output file name

# Process the file
process_file(input_file, output_file)