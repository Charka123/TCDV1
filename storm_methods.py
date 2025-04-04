import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Goes into the best track file and locate the storm classification
def find_storm_class(number, basin, year):
    if basin == "ATL" or basin == "EPAC":
        url = "https://ftp.nhc.noaa.gov/atcf/btk/b" + number + ".dat"
    else:
        url = "https://www.ssd.noaa.gov/PS/TROP/DATA/ATCF/JTWC/" + "/b" + number + ".dat"
    try:
        link = requests.get(url, verify=False, timeout=10)
        for line in link.text.splitlines():
            pass
        last_line = line
        storm_class = ""
        for i in range(0, 11):
            if i == 10:
                storm_class = last_line.split(",")[i].strip()
        return storm_class
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        return "No Data Found"


# Based on the storm classification found, process it into a word/phrase
def storm_class_write(number, basin, year):
    storm_class_word = find_storm_class(number, basin, year)
    if storm_class_word == "TS":
        if basin == "IO":
            return "Cyclonic Storm"
        else:
            return "Tropical Storm"
    elif storm_class_word == "DB" or storm_class_word == "LO":
        if "TD" in best_track_line_number(number, basin, year) or "TS" in best_track_line_number(number, basin, year):
            return "Remnants of"
        elif (number[2:4] not in ["90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
              and (basin == "ATL" or basin == "EPAC")):
            return "Potential Tropical Cyclone"
        else:
            return "Invest"
    elif storm_class_word == "TD":
        if basin == "IO" or basin == "SHEM":
            return "Invest"
        else:
            return "Tropical Depression"
    elif storm_class_word == "TY":
        if basin == "IO" or basin == "SHEM":
            return "Cyclone"
        else:
            return "Typhoon"
    elif storm_class_word == "HU":
        return "Hurricane"
    elif storm_class_word == "ST":
        if basin == "IO" or basin == "SHEM":
            return "Cyclone"
        else:
            return "Super Typhoon"
    elif storm_class_word == "EX":
        return "Post-Tropical Cyclone"
    else:
        return ""


# This method is used to determine whether a disturbance is an invest or a PTC
def best_track_line_number(number, basin, year):
    storm_index_list = []
    if basin == "ATL" or basin == "EPAC":
        url = "https://ftp.nhc.noaa.gov/atcf/btk/b" + number + ".dat"
    else:
        url = "https://www.nrlmry.navy.mil/atcf_web/docs/tracks/" + year + "/b" + number + ".dat"
    try:
        link = requests.get(url, verify=False, timeout=10)
        for line in link.text.splitlines()[0:len(link.text.splitlines())-1]:
            for i in range(0, 11):
                if i == 10:
                    storm_index_list.append(line.split(",")[i].strip())
        return storm_index_list
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        return None
