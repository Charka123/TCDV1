from datapoint_class import Datapoint
import bst_process_methods

# Initialize the variable that contain a list of datapoints.
datapoint_list = []


def bst_read():
    with open("WP012024_Ewiniar.txt") as file:
        date = ""
        for line in file:
            if not date == line.split(",")[2].strip():
                datapoint_list.append(Datapoint(line.split(",")[-3].strip(),
                                                line.split(",")[2].strip(),
                                                line.split(",")[6].strip(),
                                                line.split(",")[7].strip(),
                                                line.split(",")[8].strip(),
                                                line.split(",")[9].strip(),
                                                line.split(",")[10].strip(),
                                                line.split(",")[0].strip()))
            date = line.split(",")[2].strip()


def bst_output(max_winds, min_pressure, active_time, ace_calc, cat_list):
    winds = max_winds
    pressure = min_pressure
    time = active_time
    ace = ace_calc
    cat = bst_process_methods.storm_categories_write(cat_list, datapoint_list[0].get_basin())
    return (cat + " " + datapoint_list[-1].get_name() + "\n" + "Maximum Winds: " + winds + "kt" + "\n"
            + "Minimum Pressure: " + pressure + "mb" + "\n" + "Active Time: " + time + "\n" + "ACE: " + str(ace))


bst_read()
print(bst_output(bst_process_methods.max_winds(datapoint_list), bst_process_methods.min_pressure(datapoint_list),
                 bst_process_methods.active_time(datapoint_list),
                 round(bst_process_methods.ace_calc(datapoint_list), 4),
                 bst_process_methods.list_of_categories(datapoint_list)))
