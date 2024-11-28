import pandas as pd

# Function to convert DMS (Degrees, Minutes, Seconds) to Decimal
def dms_to_decimal(dms):
    # Split the DMS value into degrees, minutes, and seconds
    parts = dms.split('°')
    degrees = float(parts[0])
    minutes, seconds = parts[1].split("'")
    minutes = float(minutes)
    seconds = float(seconds.replace('"', ''))  # Remove any double quotes

    # Calculate the decimal value
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    return decimal

# Load the Excel file
file_path = 'format.xlsx'
df = pd.read_excel(file_path)

# Check the first few rows to understand the structure of the file
print("Initial data:")
print(df.head())

# Assume the columns containing latitude and longitude are named "Latitude" and "Longitude"
# Apply the DMS to decimal conversion for both Latitude and Longitude
df['Latitude'] = df['Latitude'].apply(dms_to_decimal)
df['Longitude'] = df['Longitude'].apply(dms_to_decimal)

# Display the cleaned data
print("\nCleaned data (after conversion):")
print(df.head())

# Optionally, save the cleaned data back to a new Excel file
output_file_path = 'formatted_coordinates.xlsx'
df.to_excel(output_file_path, index=False)

# Notify the user that the process is complete
print(f"\nData cleaned and saved to: {output_file_path}")