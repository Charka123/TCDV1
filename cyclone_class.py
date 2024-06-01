import process_methods
import storm_methods
import geographic_methods


class Cyclone:
    def __init__(self, number, name, date, time, lat, lon, basin, wind, pressure):
        self.__number = process_methods.number_process(basin, lon, number, date)
        self.__name = name
        self.__date = process_methods.time_process(time) + ", " + process_methods.date_process(date)
        self.__lat = lat
        self.__lon = lon
        self.__basin = basin
        self.__wind = wind
        self.__pressure = pressure
        if (storm_methods.storm_class_write(self.get_number().lower(), self.get_basin(), self.get_year())
                == "Invest"):
            self.__name = (self.__number[2:4] +
                           process_methods.basin_letter_process(self.get_basin(),
                                                                geographic_methods.convert_lon_to_float(self.get_lon()))
                           )

    def get_number(self):
        return self.__number

    def get_basin(self):
        return self.__basin

    def get_year(self):
        return self.__date[len(self.__date)-4:]

    def get_lon(self):
        return self.__lon

    def get_lat(self):
        return self.__lat

    def show_info(self):
        coordinate = (self.__lat[:-1] + "°" + self.__lat[-1] + " " + self.__lon[:-1] + "°" + self.__lon[-1])
        show_info_str = (storm_methods.storm_class_write(self.get_number().lower(), self.get_basin(), self.get_year())
                         + " " + self.__name + " (" + self.__number + ") " + "\n" + "Location: " + coordinate + "\n"
                         + "Maximum Winds: " + self.__wind + " kt" + "\n" + "Minimum Central Pressure: "
                         + self.__pressure + " mb" + "\n" + "Last Updated: " + self.__date)
        return show_info_str
