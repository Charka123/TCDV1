import geographic_methods


# Gather information and return the storm number
def number_process(basin, lon, number, date):
    processed_number_basin = ""

    # Determine the basin part of the str #
    if basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "L":
        processed_number_basin = "AL"
    elif basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "E":
        processed_number_basin = "EP"
    elif basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "C":
        processed_number_basin = "CP"
    elif basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "W":
        processed_number_basin = "WP"
    elif (basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "S"
          or basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "P"):
        processed_number_basin = "SH"
    elif (basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "A"
          or basin_letter_process(basin, geographic_methods.convert_lon_to_float(lon)) == "B"):
        processed_number_basin = "IO"

    # Determine the number part of the str #
    processed_number_number = number[0:2]

    # Determine the year part of the str #
    processed_number_date = "20" + date[0:2]

    # Final concatenation #
    processed_number = processed_number_basin + processed_number_number + processed_number_date
    return processed_number


# Gather information and return the desired date format
def date_process(date):
    # Determine the year part #
    year = "20" + date[0:2]

    # Determine the month part #
    month = date[2:4]

    # Determine the day part #
    day = date[4:]

    # Final concatenation #
    processed_date = month + "-" + day + "-" + year
    return processed_date


# Gather information and return the desired time format
def time_process(time):
    processed_time = time[0:2] + ":" + time[2:] + " UTC"
    return processed_time


# Determining the basin letter depending on the basin (sub-basin is also considered)
def basin_letter_process(basin, longitude):
    if basin == "ATL":
        return "L"
    elif basin == "EPAC":
        return "E"
    elif basin == "CPAC":
        return "C"
    elif basin == "WPAC":
        return "W"
    elif basin == "IO" and geographic_methods.arb_or_bob(longitude) == "arb":
        return "A"
    elif basin == "IO" and geographic_methods.arb_or_bob(longitude) == "bob":
        return "B"
    elif basin == "SHEM" and geographic_methods.pac_or_indian(longitude) == "pac":
        return "P"
    elif basin == "SHEM" and geographic_methods.pac_or_indian(longitude) == "indian":
        return "S"
