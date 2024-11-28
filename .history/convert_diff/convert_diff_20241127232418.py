import pandas as pd
import re

# Enhanced function to convert DMS to Decimal Degrees
def dms_to_decimal(dms):
    try:
        # Check if the input is empty or contains only whitespace
        if not dms or dms.strip() == "":
            return None  # Skip empty or invalid entries
        
        # Use regex to extract degrees, minutes, and seconds
        match = re.match(r"(\d+)°(\d+)'([\d.]+)", dms.strip())
        if not match:
            return None  # Skip invalid format
        
        # Parse the components
        degrees = int(match.group(1))  # Degrees
        minutes = int(match.group(2))  # Minutes
        seconds = float(match.group(3))  # Seconds
        
        # Convert to decimal degrees
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return round(decimal, 6)  # Round to 6 decimal places
    except Exception as e:
        return None  # Skip errors

# Input coordinates (paste coordinates as is)
latitude_input = """
49°48'418.6
49°49'687.5

49°52'359.2
"""

longitude_input = """
40°23'107.2

40°24'212.4
40°24'212.4
"""

# Split the input strings into lists by lines
latitudes = latitude_input.strip().split("\n")
longitudes = longitude_input.strip().split("\n")

# Initialize lists for the valid coordinates
valid_latitudes = []
valid_longitudes = []

# Loop through each pair of coordinates and convert
for lat, lon in zip(latitudes, longitudes):
    lat_decimal = dms_to_decimal(lat)
    lon_decimal = dms_to_decimal(lon)
    
    # Skip rows where either value is invalid or empty
    if lat_decimal is not None and lon_decimal is not None:
        valid_latitudes.append(lat_decimal)
        valid_longitudes.append(lon_decimal)

# Create a DataFrame to store the results
df = pd.DataFrame({
    'Latitude': valid_latitudes,
    'Longitude': valid_longitudes
})

# Save the DataFrame to an Excel file
output_file_path = 'converted_coordinates.xlsx'
df.to_excel(output_file_path, index=False)

# Print converted DataFrame
print("\nConverted coordinates:")
print(df)

print(f"\nData saved to: {output_file_path}")