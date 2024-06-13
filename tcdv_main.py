from cyclone_class import Cyclone
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

storm_list = []


def atcf_read():
    link = requests.get("https://www.nrlmry.navy.mil/tcdat/sectors/atcf_sector_file", verify=False)
    for line in link.text.splitlines():
        storm_list.append(Cyclone(line.split()[0], line.split()[1], line.split()[2], line.split()[3], line.split()[4],
                                  line.split()[5], line.split()[6], line.split()[7], line.split()[8]))
    return link.text


def show_all_info():
    if not storm_list:
        print("Currently, there is no tropical cyclone active globally.")
    else:
        print("Currently Active Tropical Cyclones and Invests: ")
        for i in range(0, len(storm_list)):
            print(storm_list[i].show_info())
            print("\n")


atcf_read()
show_all_info()
