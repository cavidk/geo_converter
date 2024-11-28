# Coordinate Converter

This Python script converts geographic coordinates from **DMS (Degrees, Minutes, Seconds)** format to **Decimal Degrees** format. It handles both latitude and longitude values, skipping empty inputs, and outputs the results in an Excel file with proper headers.

## Features
- Converts DMS format (e.g., `49°48'418.6`) to Decimal Degrees (e.g., `49.805167`).
- Handles empty values, leaving them unchanged in the output.
- Ensures the decimal separator is `.` instead of `,` for compatibility.
- Outputs results in a user-friendly Excel file with `Latitude` and `Longitude` headers.

## Requirements
- Python 3.8 or higher
- Libraries:
  - `pandas`

## Installation
1. Install Python (if not already installed).
2. Install required libraries by running:
   ```bash
   pip install pandas


## Usage

	- Clone or download this repository.
	- Update the latitude_input and longitude_input variables in the script with your coordinates. For example:

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

## Run the script
 ```bash
 python coordinate_converter.py

The converted coordinates will be saved in an Excel file named converted_coordinates.xlsx in the same directory.



   
