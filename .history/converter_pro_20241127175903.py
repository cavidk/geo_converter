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
40°23'107.2
40°24'212.4
40°24'212.4
40°24'212.4
40°24'212.4
40°24'212.4
40°24'212.4
40°23'102.7
40°19'794.7
40°22'273.9
40°24'541.5
40°22'492.9
40°22'431.3
40°25'708.3
40°25'515.5
40°25'511.8
40°26'540.2
40°24'291.7
40°24'296.7
40°25'103.4
40°24'359.1
40°22'510.9
40°24'332.8
40°23'917.9
40°24'385.9
40°24'303.6
40°22'787.6
40°23'168.1
40°22'554.8
40°29'183.7
40°22'737.5
40°24'723.4
40°26'540.2
40°23'894.4
40°24'796.5
40°26'467.3
40°29'224.2
40°27'331.7
40°27'794.1
40°22'578.9
40°25'562.1
40°21'702.2
40°22'723.6
40°22'393.6
40°22'702.9
40°24'128.8
40°24'270.9
40°22'514.1
40°22'625.3
40°23'401.7
40°24'211.1
40°25'666.6
40°23'904.9
40°26'984.1
40°22'485.6
40°18'108.6
40°22'805.2
40°23'759.8
40°23'117.4
40°22'473.5
40°22'769.4
40°24'726.7
40°22'675.8
40°24'135.5
40°22'708.6
40°22'761.8
40°23'875.8
40°23'899.6
40°22'756.7
40°24'591.5
40°22'463.3
40°22'595.9
40°22'788.3
40°23'488.1
40°24'208.2
40°23'956.5
40°24'200.7
40°24'163.1
40°23'339.4
40°22'792.7
40°23'626.6
40°24'404.4
40°24'208.8
40°23'483.8
40°24'576.6
40°24'150.6
40°23'505.2
04°02'445.1
40°24'516.1
40°23'963.5
40°22'319.1
40°22'833.5
40°22'958.7
40°22'652.1
40°22'573.6
40°23'289.4
40°22'926.6
40°23'631.7
40°22'492.1
40°22'912.9
40°22'107.4
40°22'677.5
40°21'910.9
40°23'631.8
40°22'368.9
40°20'789.7
40°22'808.6
40°22'761.2
40°23'898.8
40°23'745.7
40°22'641.7
40°22'620.2
40°22'760.5
40°22'885.9
40°22'782.4
40°24'335.3
40°27'950.5
40°25'120.8
40°25'501.1
40°23'806.7
40°23'867.6
40°28'714.9
40°25'417.2
40°24'536.4
40°24'185.7
40°29'207.2
40°24'402.5
40°25'177.7
40°29'770.2
40°23'153.7
40°30'718.6
40°24'572.7
40°24'926.4
40°27'316.8
40°31'443.5
40°22'820.2
40°25'133.2
40°25'105.6
40°25'574.5
40°31'146.4
40°34'226.4
40°22'573.5
40°27'386.1
40°22'670.9
40°24'644.5
40°31'407.8
40°25'968.6
40°25'724.2
40°29'829.5
40°26'699.4
40°25'609.4
40°32'619.4
40°22'846.5
40°20'307.7
40°24'177.1
40°23'366.9
40°34'573.9
40°24'506.3
40°23'109.6
40°24'500.1
40°21'656.9
40°24'964.9
40°23'248.6
40°33'719.8
40°23'666.8
40°04'333.4
40°29'494.2
40°23'762.4
40°34'206.1
40°21'959.5
40°29'775.5
40°21'603.8
40°23'669.1
40°22'120.9
40°24'487.9
40°23'174.2
40°22'867.7
40°25'824.5
40°22'257.7
40°32'193.2
40°22'813.5
40°27'957.9
40°19'742.1
40°23'368.7
40°21'983.5
40°22'776.8
40°20'572.9
40°23'486.8
40°22'523.7
40°25'225.3
40°22'210.2
40°23'355.8
40°35'270.6
40°22'526.8
40°24'598.9
40°21'625.3
40°25'316.7
40°23'603.5
40°18'309.2
40°25'189.6
40°23'222.7
40°29'134.5
40°24'529.8
40°21'555.8
40°24'781.4
40°22'890.8
40°32'416.8
40°22'902.4
40°25'993.8
40°16'593.5
40°23'385.5
40°22'958.1
40°23'184.8
40°25'411.4
40°29'568.4
40°26'813.7
40°26'904.6
40°27'236.2
40°25'610.1
40°25'207.3
40°25'147.7
40°25'143.7
40°22'297.7
40°22'293.9
40°23'954.1
40°24'520.1
40°23'918.8
40°22'276.1
40°23'170.5
40°20'473.9
40°22'933.4
40°22'790.5
40°26'903.4
40°22'624.9
40°29'481.6
40°25'172.2
40°23'928.6
40°19'817.3
40°23'443.8
40°22'977.8
40°22'710.2
40°24'116.9
40°22'744.2
40°23'448.7
40°22'461.4
40°21'497.4
40°23'102.1
40°22'836.9
40°29'198.3
40°25'188.9
40°20'671.1
40°22'608.9
40°23'690.2
40°24'119.7
40°22'851.3
40°23'270.9
40°23'642.6
40°24'111.6
40°23'747.3
40°25'155.3
40°23'730.8
40°22'516.1
40°29'508.2
40°24'161.1
40°23'151.7
40°23'107.6
40°28'847.9
40°23'104.6
40°31'629.8
40°29'481.5
40°28'806.7
40°27'378.8
40°22'624.8
40°32'451.6
40°24'196.3
40°22'066.2
40°22'180.8
40°23'796.5
40°24'599.4
40°23'174.6
40°22'331.2
40°22'781.4
40°24'067.8
40°24'591.3
40°22'360.4
40°22'817.3
40°23'967.7
40°24'067.8
40°22'583.1
40°23'149.3
40°22'574.1
40°23'764.2
40°23'252.5
40°23'109.6
40°22'356.5
40°25'364.5
40°23'557.7
40°33'706.5
40°33'705.7
40°24'066.1
40°34'296.3
40°24'557.7
40°25'516.7
40°23'637.1
40°22'996.2
40°28'314.1
40°23'703.2
40°24'637.5
40°20'923.4
40°25'926.5
40°26'462.1
40°26'521.5
40°28'060.5
40°22'158.1
40°26'186.1
40°31'023.7
40°22'450.8
40°28'234.9
40°20'938.2
40°22'005.6
40°23'437.6
40°32'283.6
40°22'209.1
40°24'065.1
40°24'876.5
40°24'564.1
40°22'269.8
40°23'883.8
40°23'608.7
40°28'809.1
40°29'056.4
40°25'360.9
40°24'218.5
40°20'252.3
40°22'933.8
40°25'541.4
40°28'197.4
40°22'059.5
40°24'688.7
40°24'555.9
40°25'509.5
40°23'627.2
40°22'819.4
40°31'948.1
40°31'491.4
40°22'570.2
40°24'976.8
40°21'594.7
40°25'023.9
40°28'489.9
40°23'573.4
40°25'659.6
40°25'544.7
40°30'146.4
40°24'848.7
40°22'788.6
40°22'790.1
40°23'754.1
40°22'986.3
40°32'019.6
40°25'959.3
40°27'759.5
40°26'462.9
40°27'733.5
40°27'946.3
40°25'454.5
40°23'731.6
40°22'140.1
40°24'138.1
40°24'439.9
40°22'174.2
40°24'806.2
40°35'453.4
40°31'115.2
40°32'152.2
40°24'041.1
40°24'825.9
40°23'107.9
40°35'284.9
40°22'803.9
40°23'107.6
04°02'486.8
"""

longitude_input = """
49°49'687.5
49°52'359.2
49°57'672.7
49°57'697.4
50°01'896.8
04°95'129.2
49°50'540.6
49°57'897.4
49°49'107.2
49°50'138.1
49°55'533.9
49°50'996.5
49°51'445.1
49°53'907.3
49°50'566.3
49°50'460.3
49°46'381.4
49°56'815.8
49°48'486.4
49°55'913.2
49°52'161.2
49°55'473.6
49°48'442.9
49°57'118.7
49°48'403.5
49°48'395.9
49°50'839.2
49°57'247.5
49°49'953.2
50°07'820.4
49°49'822.4
49°48'897.4
49°46'381.4
49°50'329.9
49°50'898.1
49°50'698.7
50°09'875.6
50°04'125.1
50°04'958.8
49°49'509.5
49°50'626.3
49°56'817.9
49°52'746.9
49°50'854.6
49°50'696.1
49°49'207.4
49°48'383.8
49°48'721.9
49°50'910.6
49°53'859.2
49°52'316.5
49°52'984.5
49°49'930.3
50°05'260.6
49°50'779.3
49°45'783.6
49°50'831.4
49°49'200.6
04°95'025.1
49°50'599.9
49°50'741.2
49°48'272.1
49°50'875.1
49°52'210.8
49°50'819.9
49°50'831.2
49°49'962.6
49°49'863.2
49°51'123.3
49°48'892.3
49°50'566.6
49°49'909.6
49°49'812.8
49°48'162.9
49°48'426.3
49°50'158.7
49°48'451.7
49°48'418.6
49°48'158.6
49°48'671.2
49°47'644.1
49°48'339.7
49°52'339.4
49°48'137.5
49°51'981.8
49°52'126.8
49°50'497.4
49°51'900.6
49°48'879.1
49°52'601.3
49°57'184.1
49°51'814.8
49°52'349.3
49°48'736.4
49°57'663.7
49°52'295.4
49°48'247.9
49°48'929.4
49°50'476.4
49°48'409.9
49°49'825.2
04°94'997.7
49°56'916.6
49°51'578.1
49°50'235.5
49°48'612.6
49°48'642.5
49°51'416.3
49°52'570.5
49°49'156.3
49°51'294.3
49°50'197.9
49°51'418.8
49°57'897.5
49°50'617.6
49°57'314.1
50°04'883.6
49°48'660.2
49°50'526.5
49°52'741.2
49°48'852.1
49°45'198.4
49°58'126.8
49°52'109.4
49°56'195.3
50°10'212.1
49°48'785.1
49°55'505.8
49°51'344.5
49°48'501.4
49°56'486.9
49°50'800.8
49°49'736.7
49°44'524.2
49°41'235.2
49°57'254.6
49°56'148.7
49°55'910.6
49°49'685.9
50°05'620.9
49°41'342.5
49°48'695.5
49°45'458.6
49°51'129.9
49°48'837.4
50°05'991.8
49°50'972.5
49°51'148.8
49°56'992.1
49°56'622.3
49°50'975.8
49°39'777.4
49°51'436.2
49°48'441.7
49°52'705.2
49°51'453.8
49°40'154.7
49°57'485.5
49°50'677.7
49°57'494.7
50°04'672.6
49°50'363.9
49°47'254.2
49°41'622.5
49°52'566.2
49°24'692.5
49°51'310.3
49°52'540.8
49°40'519.5
49°57'321.3
50°11'909.8
49°56'822.2
49°57'151.5
49°57'766.6
49°48'599.7
49°57'951.2
49°57'916.9
04°95'138.4
04°94'975.9
49°46'958.3
49°48'660.7
49°49'766.5
49°49'122.1
49°57'475.8
49°56'681.7
49°57'901.6
49°50'333.4
49°48'131.3
49°48'321.7
49°50'357.8
49°49'232.5
49°50'490.7
49°40'175.8
49°58'656.5
49°56'277.8
49°58'244.5
49°47'918.9
49°55'642.8
49°46'823.2
49°48'473.6
49°50'858.2
50°07'787.3
49°52'233.3
49°57'456.8
49°56'736.7
49°57'228.1
50°00'495.2
49°52'718.4
49°51'605.7
49°40'745.3
49°47'563.3
49°57'820.3
49°50'125.4
49°50'233.8
49°44'627.3
49°44'961.1
49°48'104.8
49°44'330.2
50°06'670.9
49°49'112.2
50°06'380.6
50°06'382.1
49°50'123.1
49°50'131.6
49°51'527.1
49°50'843.6
49°50'225.6
49°50'974.8
49°48'639.1
49°48'611.9
49°49'637.4
49°48'367.2
49°48'104.1
49°51'308.5
49°57'254.7
50°15'650.7
49°50'161.3
49°49'122.6
49°50'707.8
49°49'542.1
49°48'284.8
49°50'242.6
49°52'524.1
49°50'706.2
49°50'107.5
49°50'267.3
49°49'683.6
49°50'497.7
50°09'998.9
49°50'808.2
49°50'328.3
49°50'154.6
49°50'310.9
49°50'241.3
49°48'537.8
49°52'463.3
49°47'703.5
49°50'264.1
49°49'165.5
49°51'290.1
49°49'161.7
49°51'544.5
49°57'186.4
49°52'270.3
49°57'249.6
49°49'687.7
49°45'312.1
49°57'908.4
50°05'879.6
49°57'259.8
49°45'304.4
50°04'789.8
49°51'230.2
49°46'997.5
49°52'248.5
49°50'329.2
49°50'209.9
49°57'173.8
49°56'575.1
49°51'320.5
49°50'266.5
49°51'926.8
49°51'144.4
49°48'898.7
49°56'731.2
49°49'868.2
49°52'604.4
49°51'144.3
49°48'303.9
49°57'804.2
49°48'933.9
49°57'623.8
49°50'851.3
49°49'688.3
49°57'868.5
49°50'112.9
49°51'476.9
49°55'396.2
49°55'400.8
49°47'829.7
49°57'471.4
49°48'904.8
49°49'691.4
49°50'553.6
49°50'530.1
50°04'682.7
49°57'530.1
49°58'108.3
49°59'890.7
49°48'487.7
49°49'919.5
49°48'553.5
49°50'539.3
49°56'218.8
49°57'521.9
50°06'124.1
49°51'621.9
49°37'499.1
49°50'126.4
49°57'736.6
49°47'630.1
49°50'918.2
49°57'107.7
49°49'311.1
49°46'123.8
49°52'195.6
49°55'863.8
49°49'765.7
49°50'587.2
49°45'476.5
49°51'292.6
49°50'125.3
49°52'348.9
49°46'995.5
49°58'670.2
49°49'121.3
49°37'613.3
49°56'411.6
49°56'479.2
49°56'575.6
49°49'695.6
49°50'364.7
49°49'616.1
49°47'107.3
49°46'712.6
49°51'613.1
49°56'365.4
49°58'201.6
49°56'127.6
50°06'589.8
49°58'650.4
49°50'717.2
49°50'638.8
49°58'474.5
49°56'528.2
49°50'355.2
49°50'369.7
49°49'203.6
49°50'538.3
50°00'130.5
49°47'112.4
49°43'374.6
49°45'951.8
49°44'849.8
49°56'664.6
50°13'750.9
49°49'162.6
04°94'965.4
49°51'624.9
49°50'720.1
49°50'261.6
49°49'324.5
49°40'550.5
50°06'265.2
49°46'977.1
49°49'954.8
49°49'319.8
49°49'688.5
49°40'408.4
49°50'377.4
49°49'687.8
49°58'146.9
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

# Replace commas with periods in the DataFrame (if you want this behavior for display or saving as CSV)
df = df.applymap(lambda x: str(x).replace(",", "."))

# Display the cleaned data
print("\nConverted data (after conversion):")
print(df)

# Optionally, save the cleaned data to a new Excel file
output_file_path = 'converted_coordinates.xlsx'
df.to_excel(output_file_path, index=False)

# Notify the user that the process is complete
print(f"\nData converted and saved to: {output_file_path}")