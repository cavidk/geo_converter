import pandas as pd
import re

# Function to convert DMS to Decimal Degrees
def dms_to_decimal(dms):
    try:
        # Check if the input is empty or contains only whitespace
        if not dms or dms.strip() == "":
            return ""  # Return empty for empty input
        
        # Use regex to extract degrees, minutes, and seconds
        match = re.match(r"(\d+)°(\d+)'([\d.]+)", dms.strip())
        if not match:
            return ""  # Return empty for invalid format
        
        # Parse the components
        degrees = int(match.group(1))  # Degrees
        minutes = int(match.group(2))  # Minutes
        seconds = float(match.group(3))  # Seconds
        
        # Convert to decimal degrees
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return round(decimal, 6)  # Round to 6 decimal places
    except Exception:
        return ""  # Return empty for any errors

# Input coordinates (paste coordinates as is)
latitude_input = """

"""

longitude_input = """

"""

# Split the input strings into lists by lines
latitudes = latitude_input.strip().split("\n")
longitudes = longitude_input.strip().split("\n")

# Ensure both lists have the same length by appending empty values if necessary
max_length = max(len(latitudes), len(longitudes))
latitudes += [""] * (max_length - len(latitudes))
longitudes += [""] * (max_length - len(longitudes))

# Convert each latitude and longitude
converted_latitudes = [dms_to_decimal(lat) for lat in latitudes]
converted_longitudes = [dms_to_decimal(lon) for lon in longitudes]

# Combine into a formatted output
output = [
    f"{lat or ''}  {lon or ''}"
    for lat, lon in zip(converted_latitudes, converted_longitudes)
]

# Save the results to a text file and print them
output_file_path = "convert_diff.xlsx"
with open(output_file_path, "w") as f:
    f.write("\n".join(output))

print("\nConverted coordinates:")
print("\n".join(output))
print(f"\nData saved to: {output_file_path}")