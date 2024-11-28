import pandas as pd
import re

# Function to convert DMS to Decimal Degrees
def dms_to_decimal(dms):
    try:
        if not dms or dms.strip() == "":
            return ""  # Return empty for empty input
        
        # Extract degrees, minutes, and seconds
        match = re.match(r"(\d+)°(\d+)'([\d.]+)", dms.strip())
        if not match:
            return ""  # Return empty for invalid format
        
        degrees = int(match.group(1))  # Degrees
        minutes = int(match.group(2))  # Minutes
        seconds = float(match.group(3))  # Seconds
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return round(decimal, 6)  # Round to 6 decimal places
    except Exception:
        return ""  # Return empty for any errors

# Input coordinates
latitude_input = """

"""

longitude_input = """

"""

# Split input strings into lists by lines
latitudes = latitude_input.strip().split("\n")
longitudes = longitude_input.strip().split("\n")

# Ensure both lists are the same length
max_length = max(len(latitudes), len(longitudes))
latitudes += [""] * (max_length - len(latitudes))
longitudes += [""] * (max_length - len(longitudes))

# Convert to decimal degrees
converted_latitudes = [dms_to_decimal(lat) for lat in latitudes]
converted_longitudes = [dms_to_decimal(lon) for lon in longitudes]

# Combine data into a DataFrame
df = pd.DataFrame({
    "Latitude": converted_latitudes,
    "Longitude": converted_longitudes
})

# Save to an Excel file using pandas
output_file_path = "convert_diff.xlsx"
df.to_excel(output_file_path, index=False)

print("\nConverted coordinates saved to:", output_file_path)