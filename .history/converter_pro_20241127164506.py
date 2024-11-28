import openly

def dms_to_decimal(degrees, minutes, seconds):
    """Converts DMS (Degrees, Minutes, Seconds) to Decimal Degrees."""
    return degrees + (minutes / 60) + (seconds / 3600)

def convert_coordinates(dms_latitudes, dms_longitudes):
    """Converts a list of DMS coordinates to Decimal Degrees."""
    decimal_coords = []

    for i in range(len(dms_latitudes)):
        # Parse the DMS format (degrees, minutes, seconds)
        lat_parts = dms_latitudes[i].split('°')
        lon_parts = dms_longitudes[i].split('°')

        lat_deg = int(lat_parts[0])
        lat_min_sec = lat_parts[1].split("'")
        lat_min = int(lat_min_sec[0])
        lat_sec = float(lat_min_sec[1].replace('"', ''))

        lon_deg = int(lon_parts[0])
        lon_min_sec = lon_parts[1].split("'")
        lon_min = int(lon_min_sec[0])
        lon_sec = float(lon_min_sec[1].replace('"', ''))

        # Convert to decimal
        lat_decimal = dms_to_decimal(lat_deg, lat_min, lat_sec)
        lon_decimal = dms_to_decimal(lon_deg, lon_min, lon_sec)

        decimal_coords.append([lat_decimal, lon_decimal])

    return decimal_coords

def write_to_excel(decimal_coords, filename='converted_coordinates.xlsx'):
    """Writes the converted coordinates to an Excel file."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Coordinates'

    # Write header
    ws['A1'] = 'Latitude (Decimal)'
    ws['B1'] = 'Longitude (Decimal)'

    # Write data
    for i, coord in enumerate(decimal_coords, start=2):
        ws[f'A{i}'] = coord[0]
        ws[f'B{i}'] = coord[1]

    # Save the Excel file
    wb.save(filename)

# Sample DMS coordinates
dms_latitudes = [
    "40°23'107.2\"",
    "40°24'212.4\"",
    "40°24'212.4\"", 
    "40°24'212.4\"", 
    "40°24'212.4\"", 
    "40°24'212.4\"",
    "40°24'212.4\"", 
    "40°23'102.7\"", 
    "40°22'180.9\"", 
    "04°02'260.7\"",
    "40°19'794.7\"", 
    "40°22'273.9\"", 
    "40°24'541.5\"", 
    "40°22'492.9\"", 
    "40°22'431.3\"",
    "40°25'708.3\"", 
    "40°25'515.5\"", 
    "40°25'511.8\"", 
    "40°25'469.7\""
]
dms_longitudes = [
    "49°49'687.5\"", 
    "49°52'359.2\"", 
    "49°57'672.7\"", 
    "49°57'697.4\"", 
    "50°01'896.8\"",
    "04°95'129.2\"", 
    "49°50'540.6\"", 
    "49°57'897.4\"", 
    "00°49'507.8\"", 
    "49°49'771.3\"",
    "49°49'107.2\"", 
    "49°50'138.1\"", 
    "49°55'533.9\"", 
    "49°50'996.5\"", 
    "49°51'445.1\"",
    "49°53'907.3\"", 
    "49°50'566.3\"", 
    "49°50'460.3\"", 
    "00°49'494.5\""
]

# Convert coordinates
decimal_coords = convert_coordinates(dms_latitudes, dms_longitudes)

# Write the result to an Excel file
write_to_excel(decimal_coords)

print("Conversion complete! Check 'converted_coordinates.xlsx' for the result.")