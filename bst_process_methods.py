from datapoint_class import Datapoint


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
