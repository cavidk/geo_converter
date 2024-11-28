import pandas as pd

# Function to convert DMS (Degrees, Minutes, Seconds) format to Decimal Degrees
def dms_to_decimal(dms):
    try:
        # Split the input by the degree symbol and apostrophe
        parts = dms.split('°')
        degrees = int(parts[0].strip())  # Degrees
        minutes_seconds = parts[1].split("'")
        minutes = int(minutes_seconds[0].strip())  # Minutes
        seconds = float(minutes_seconds[1].strip()) if len(minutes_seconds) > 1 else 0  # Seconds

        # Convert to Decimal Degrees
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return round(decimal, 6)  # rounding to 6 decimal places
    except Exception as e:
        print(f"Error converting {dms}: {e}")
        return None

# Input coordinates (just copy and paste them as they are, no quotes or extra symbols needed)
latitude_input = """

"""

longitude_input = """
40°23'107.2
40°24'212.4
40°24'212.4
40°24'212.4
40°24'212.4
40°24'212.4
40°24'212.4
40°23'102.7
40°19'794.7
"""

# Convert the input strings into lists (splitting by line breaks)
latitudes = latitude_input.strip().split("\n")
longitudes = longitude_input.strip().split("\n")

# Initialize lists to hold the converted values
converted_latitudes = []
converted_longitudes = []

# Convert all latitudes and longitudes
for lat, lon in zip(latitudes, longitudes):
    lat_decimal = dms_to_decimal(lat)
    lon_decimal = dms_to_decimal(lon)
    
    # Add the converted coordinates to the lists
    converted_latitudes.append(lat_decimal)
    converted_longitudes.append(lon_decimal)

# Create a DataFrame with the converted coordinates
df = pd.DataFrame({
    'Latitude': converted_latitudes,
    'Longitude': converted_longitudes
})

# Display the cleaned data
print("\nConverted data (after conversion):")
print(df)

# Optionally, save the cleaned data to a new Excel file
output_file_path = 'converted_coordinates.xlsx'
df.to_excel(output_file_path, index=False)

# Notify the user that the process is complete
print(f"\nData converted and saved to: {output_file_path}")