class Datapoint:
    def __init__(self, name, timestamp, lat, lon, wind, pressure, category, basin):
        self.name = name
        self.timestamp = timestamp
        self.lat = lat
        self.lon = lon
        self.__wind = wind
        self.__pressure = pressure
        self.category = category
        self.basin = basin

    def get_wind(self):
        return self.__wind

    def get_pressure(self):
        return self.__pressure

