from cyclone_class import Cyclone
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize the variable that contain a list of currently active storms
storm_list = []


# This method reads ATCF sector file and create storm objects based on attributes
def atcf_read():
    link = requests.get("https://www.nrlmry.navy.mil/tcdat/sectors/atcf_sector_file", verify=False)
    for line in link.text.splitlines():
        storm_list.append(Cyclone(line.split()[0], line.split()[1], line.split()[2], line.split()[3], line.split()[4],
                                  line.split()[5], line.split()[6], line.split()[7], line.split()[8]))
    return link.text


# This method utilize a method within the Cyclone class to output information about each storm
def show_all_info():
    if not storm_list:
        print("Currently, there is no tropical cyclone active globally.")
    else:
        print("Currently Active Tropical Cyclones and Invests: ")
        for i in range(0, len(storm_list)):
            print(storm_list[i].show_info())
            print("\n")


# This method allows the program to only show information for one storm based on the storm number that user inputted.
def show_one_info(number):
    function_value = False
    for i in range(0, len(storm_list)):
        if storm_list[i].get_number() == number:
            print(storm_list[i].show_info())
            function_value = True
    return function_value


# This is the main program and initialize the necessary variables
atcf_read()
print("Welcome to Tropical Cyclone Data Viewer!")
storm_number_select = ""
while_condition = None

# This while loop contains code structure for gathering user input. When storm info is being correctly outputted,
# the loops ends #
while not while_condition:
    storm_number_select = input("Please type the designation number (Example: WP012024) of a currently active tropical "
                                "cyclone or type \"ALL\" to show all tropical cyclones that are currently active: ")
    if storm_number_select == "ALL":
        show_all_info()
        while_condition = True
    else:
        if not show_one_info(storm_number_select):
            print("Invalid input. Please try again.")
            while_condition = False
        else:
            show_one_info(storm_number_select)
            while_condition = True
