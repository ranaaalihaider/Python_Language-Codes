    if unit_to_convert == 1 and unit_to_convert_in == 2:  # Meter to Centimeter
            result = length * 100
        elif unit_to_convert == 1 and unit_to_convert_in == 3:  # Meter to Inch
            result = length * 39.3701
        elif unit_to_convert == 1 and unit_to_convert_in == 4:  # Meter to Kilometer
            result = length * 0.001
        elif unit_to_convert == 1 and unit_to_convert_in == 5:  # Meter to Miles
            result = length * 0.000621371
        elif unit_to_convert == 2 and unit_to_convert_in == 1:  # Centimeter to Meter
            result = length / 100
        elif unit_to_convert == 2 and unit_to_convert_in == 3:  # Centimeter to Inch
            result = length / 2.54
        elif unit_to_convert == 2 and unit_to_convert_in == 4:  # Centimeter to Kilometer
            result = length / 100000
        elif unit_to_convert == 2 and unit_to_convert_in == 5:  # Centimeter to Miles
            result = length / 160934.4
        elif unit_to_convert == 3 and unit_to_convert_in == 1:  # Inch to Meter
            result = length * 0.0254
        elif unit_to_convert == 3 and unit_to_convert_in == 2:  # Inch to Centimeter
            result = length * 2.54
        elif unit_to_convert == 3 and unit_to_convert_in == 4:  # Inch to Kilometer
            result = length * 0.0000254
        elif unit_to_convert == 3 and unit_to_convert_in == 5:  # Inch to Miles
            result = length * 0.0000157828
        elif unit_to_convert == 4 and unit_to_convert_in == 1:  # Kilometer to Meter
            result = length * 1000
        elif unit_to_convert == 4 and unit_to_convert_in == 2:  # Kilometer to Centimeter
            result = length * 100000
        elif unit_to_convert == 4 and unit_to_convert_in == 3:  # Kilometer to Inch
            result = length * 39370.1
        elif unit_to_convert == 4 and unit_to_convert_in == 5:  # Kilometer to Miles
            result = length * 0.621371
        elif unit_to_convert == 5 and unit_to_convert_in == 1:  # Miles to Meter
            result = length * 1609.34
        elif unit_to_convert == 5 and unit_to_convert_in == 2:  # Miles to Centimeter
            result = length * 160934
        elif unit_to_convert == 5 and unit_to_convert_in == 3:  # Miles to Inch
            result = length * 63360
        elif unit_to_convert == 5 and unit_to_convert_in == 4:  # Miles to Kilometer
            result = length * 1.60934    
        else:
            result = length  # Default to input length if units are the same
        
        print("Your Output is " ,result,"\n")
