

def max_winds(class_list):
    winds = 0
    for point in class_list:
        if int(point.get_wind()) > winds:
            winds = int(point.get_wind())
    return str(winds)


def min_pressure(class_list):
    pressure = 1040
    for point in class_list:
        if int(point.get_pressure()) < pressure:
            pressure = int(point.get_pressure())
    return str(pressure)


def active_time(class_list):
    first_time = (class_list[0].get_timestamp()[:4] + "." + class_list[0].get_timestamp()[4:6] + "."
                  + class_list[0].get_timestamp()[6:8])
    last_time = (class_list[-1].get_timestamp()[:4] + "." + class_list[-1].get_timestamp()[4:6] + "."
                 + class_list[-1].get_timestamp()[6:8])
    return first_time + "-" + last_time


def ace_calc(class_list):
    ace = 0
    for point in class_list:
        if (int(point.get_wind()) < 34 or point.get_category() == "DB" or point.get_category() == "WV"
                or point.get_category() == "EX" or point.get_category() == "LO" or point.get_category() == "MD"):
            ace += 0
        else:
            ace += int(point.get_wind()) ** 2 / 10000
    return ace


def list_of_categories(class_list):
    cat_list = []
    for point in class_list:
        cat_list.append(point.get_category())
    return cat_list


def storm_categories_write(cat_list, basin):
    if "ST" in cat_list:
        if basin == "IO" or basin == "SH":
            return "Cyclone"
        else:
            return "Super Typhoon"
    elif "TY" in cat_list:
        if basin == "IO" or basin == "SH":
            return "Cyclone"
        else:
            return "Typhoon"
    elif "HU" in cat_list:
        return "Hurricane"
    elif "TS" in cat_list:
        if basin == "IO":
            return "Cyclonic Storm"
        else:
            return "Tropical Storm"
    elif "TD" in cat_list:
        return "Tropical Depression"
