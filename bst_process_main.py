from datapoint_class import Datapoint
import bst_process_methods

# Initialize the variable that contain a list of datapoints.
datapoint_list = []


def bst_read():
    with open("WP012024_Ewiniar.txt") as file:
        date = ""
        for line in file:
            if not date == line.split(",")[2].strip():
                datapoint_list.append(Datapoint(line.split(",")[-2].strip(),
                                                line.split(",")[2].strip(),
                                                line.split(",")[6].strip(),
                                                line.split(",")[7].strip(),
                                                line.split(",")[8].strip(),
                                                line.split(",")[9].strip(),
                                                line.split(",")[10].strip(),
                                                line.split(",")[0].strip()))
            date = line.split(",")[2].strip()


bst_read()
print(bst_process_methods.max_winds(datapoint_list))
print(bst_process_methods.min_pressure(datapoint_list))
