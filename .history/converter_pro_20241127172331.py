import pandas as pd

# Function to convert raw coordinates (like 40242124) to decimal format
def raw_to_decimal(coord):
    try:
        # Ensure the value is numeric and convert it to a string to split
        if isinstance(coord, (int, float)):
            coord = str(int(coord))  # Ensure it's a string and strip decimal if present
            if len(coord) > 4:  # Assuming the first 2 digits are degrees
                degrees = int(coord[:2])  # First 2 digits are degrees
                minutes = int(coord[2:4])  # Next 2 digits are minutes
                seconds = int(coord[4:]) if len(coord) > 4 else 0  # Remaining part is seconds

                # Convert to decimal degrees
                decimal = degrees + (minutes / 60) + (seconds / 3600)
                return round(decimal, 6)  # rounding to 6 decimal places
            else:
                return None  # Return None if the coordinate is not valid
        else:
            return None  # In case the value is not numeric, return None
    except Exception as e:
        print(f"Error converting {coord}: {e}")
        return None

# Load the Excel file
file_path = 'format.xlsx'
df = pd.read_excel(file_path)

# Check the first few rows to understand the structure of the file
print("Initial data:")
print(df.head())

# Apply the raw_to_decimal conversion for both Latitude and Longitude
df['Latitude'] = df['Latitude'].apply(raw_to_decimal)
df['Longitude'] = df['Longitude'].apply(raw_to_decimal)

# Display the cleaned data
print("\nCleaned data (after conversion):")
print(df.head())

# Optionally, save the cleaned data back to a new Excel file
output_file_path = 'formatted_coordinates.xlsx'
df.to_excel(output_file_path, index=False)

# Notify the user that the process is complete
print(f"\nData cleaned and saved to: {output_file_path}")