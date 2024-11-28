import pandas as pd

def dms_to_decimal(dms):
    try:
        parts = dms.split('°')
        degrees = int(parts[0].strip())  # Degrees
        minutes_seconds = parts[1].split("'")
        minutes = int(minutes_seconds[0].strip())  # Minutes
        seconds = float(minutes_seconds[1].strip()) if len(minutes_seconds) > 1 else 0  # Seconds

        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return round(decimal, 6)  # rounding to 6 decimal places
    except Exception as e:
        print(f"Error converting {dms}: {e}")
        return None

# Input coordinates (just copy and paste them as they are, no quotes or extra symbols needed)
latitude_input = """

"""

longitude_input = """

"""

latitudes = latitude_input.strip().split("\n")
longitudes = longitude_input.strip().split("\n")

converted_latitudes = []
converted_longitudes = []

for lat, lon in zip(latitudes, longitudes):
    lat_decimal = dms_to_decimal(lat)
    lon_decimal = dms_to_decimal(lon)
    
    converted_latitudes.append(lat_decimal)
    converted_longitudes.append(lon_decimal)

df = pd.DataFrame({
    'Latitude': converted_latitudes,
    'Longitude': converted_longitudes
})

df = df.applymap(lambda x: str(x).replace(",", "."))

print("\nConverted data (after conversion):")
print(df)

output_file_path = 'converted_coordinates.xlsx'
df.to_excel(output_file_path, index=False)

print(f"\nData converted and saved to: {output_file_path}")