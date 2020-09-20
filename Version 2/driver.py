#################################################################################

"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""

import os
        
#################################################################################
# Driver Section
#################################################################################

# Makes a new Driver
def make_new_driver(first_name, last_name, car_make_and_model):
    trips_completed = 0
    return ("Driver", [first_name, last_name, car_make_and_model, \
            trips_completed] )

# Creates an existing Driver
def make_driver(first_name, last_name, car_make_and_model, trips_completed):
    return ("Driver", [first_name, last_name, car_make_and_model, \
            trips_completed] )

# Determines whether an object is a Driver
def is_driver(driver):
    if len(driver) == 2 and driver[0] == "Driver":
        driver_info = get_driver_info(driver)
        if type(driver_info) == type([]) and len(driver_info) == 4:
            return True
    return False

# Gets the list of Driver details
def get_driver_info(driver):
    return driver[1]

# Gets the Drivers first name
def get_first_name(driver_info):
    return get_driver_info(driver_info)[0]

# Gets the Drivers last name
def get_last_name(driver_info):
    return get_driver_info(driver_info)[1]

# Gets the Drivers car make and model
def get_make_and_model(driver_info):
    return get_driver_info(driver_info)[2]

# Updates the Drivers car make and model
def change_make_and_model(driver, new_make_model):
    if is_driver(driver):
        driver_info = get_driver_info(driver)
        driver_info[2] = new_make_model
    else:
        print("\nERROR: ")
        print("\nDidn't receive a Driver\n")

# Gets the Drivers number of trips completed
def get_trips_completed(driver):
    return get_driver_info(driver)[3]

# Increases the number of trips a Driver makes
def increase_trips_completed(driver):
    driver_info = get_driver_info(driver)
    driver_info[3] = get_trips_completed(driver) + 1

# Determines if a Driver is new or not
def is_driver_new(driver):
    num = get_trips_completed(driver)
    if num == 0:
        return True
    return False

#################################################################################
# Driver Files Section
#################################################################################

# File with all the Driver Information
file_name = "Youba_Drivers.txt"
folder_name = "./Text-Files/"

# Adds a Driver to the file
def add_driver(driver):

    try:
        if os.path.exists(folder_name + file_name):
            # append if the file already exists
            append_write = "a"
        else:
            # make a new file and write
            append_write = "w"
    except IOError as e:
        print("Not allowed", e)

    first_name = get_first_name(driver)
    last_name = get_last_name(driver)
    make_model = get_make_and_model(driver)
    trips = get_trips_completed(driver)

    file = open(file_name, append_write)
    file.write(first_name + "," + last_name + "," \
               + make_model + "," + str(trips) + "\n")
    file.close()

# Adds a Driver to the file
def remove_driver(driver):
    pass
    #driver2 = make_driver("Delano","Thompson","Nissan,Sunny",7)
