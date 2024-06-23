# Converting longitude to a float number
def convert_lon_to_float(longitude):
    return float(longitude[0:len(longitude)-1])


# Converting latitude to a float number
def convert_lat_to_float(latitude):
    return float(latitude[0:len(latitude) - 1])


# Based on given longitude, determine whether a storm is in the Arabian Sea or Bay of Bangal
def arb_or_bob(longitude):
    if longitude < 80:
        return "arb"
    else:
        return "bob"


# Based on given longitude, determine whether a storm is in the southwest Indian Ocean or South Pacific
def pac_or_indian(longitude):
    if longitude < 135:
        return "indian"
    else:
        return "pac"
