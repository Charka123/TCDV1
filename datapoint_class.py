class Datapoint:
    def __init__(self, name, timestamp, lat, lon, wind, pressure, category, basin):
        self.name = name
        self.__timestamp = timestamp
        self.lat = lat
        self.lon = lon
        self.__wind = wind
        self.__pressure = pressure
        self.__category = category
        self.basin = basin

    def get_wind(self):
        return self.__wind

    def get_pressure(self):
        return self.__pressure

    def get_timestamp(self):
        return self.__timestamp

    def get_category(self):
        return self.__category

    def get_name(self):
        return self.name

    def get_basin(self):
        return self.basin

