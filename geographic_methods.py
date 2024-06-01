def convert_lon_to_float(longitude):
    return float(longitude[0:len(longitude)-1])


def convert_lat_to_float(latitude):
    return float(latitude[0:len(latitude) - 1])


def arb_or_bob(longitude):
    if longitude < 80:
        return "arb"
    else:
        return "bob"


def pac_or_indian(longitude):
    if longitude < 135:
        return "indian"
    else:
        return "pac"
