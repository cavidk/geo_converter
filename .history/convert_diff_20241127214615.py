import pandas as pd
import re

def dms_to_decimal(dms):
    try:
        match = re.match(r"(\d+)°(\d+)'([\d.]+)", dms.strip())
        if not match:
            raise ValueError(f"Invalid format: {dms}")
        
        degrees = int(match.group(1))  # Degrees
        minutes = int(match.group(2))  # Minutes
        seconds = float(match.group(3))  # Seconds
        
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return round(decimal, 6)  # Round to 6 decimal places
    except Exception as e:
        print(f"Error converting '{dms}': {e}")
        return None

# Input coordinates (paste coordinates as is, no need for extra quotes)
latitude_input = """

"""
longitude_input = """

"""

# Split the input strings into lists by lines
latitudes = latitude_input.strip().split("\n")
longitudes = longitude_input.strip().split("\n")

# Initialize lists for the converted values
converted_latitudes = []
converted_longitudes = []

# Loop through each pair of coordinates and convert
for lat, lon in zip(latitudes, longitudes):
    lat_decimal = dms_to_decimal(lat)
    lon_decimal = dms_to_decimal(lon)
    
    converted_latitudes.append(lat_decimal)
    converted_longitudes.append(lon_decimal)

# Create a DataFrame to store the results
df = pd.DataFrame({
    'Latitude': converted_latitudes,
    'Longitude': converted_longitudes
})

# Save the DataFrame to an Excel file
output_file_path = 'converted_diff.xlsx'
df.to_excel(output_file_path, index=False)

# Print converted DataFrame
print("\nConverted coordinates:")
print(df)

print(f"\nData saved to: {output_file_path}")