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

def make_new_driver(first_name, last_name, car_make_and_model):
    """
    Constructs an ADT for a new Driver

    Args:
        first_name: Drivers first name
        last_name: Drivers last name
        car_make_and_model: Drivers car make and model

    Returns:
        driver: A Driver ADT
    """
    trips_completed = 0
    return ("Driver", [first_name, last_name, car_make_and_model, \
            trips_completed] )

def make_driver(first_name, last_name, car_make_and_model, trips_completed):
    """
    Constructs an ADT for an existing Driver

    Args:
        first_name: Drivers first name
        last_name: Drivers last name
        car_make_and_model: Drivers car make and model
        trips_completed: Number of trips made per day

    Returns:
        driver: A Driver ADT
    """
    return ("Driver", [first_name, last_name, car_make_and_model, \
            trips_completed] )

def is_driver(driver):
    """
    Determines whether an object is a Driver

    Args:
        driver: A Driver ADT

    Returns:
        boolean: True or False
    """
    if len(driver) == 2 and driver[0] == "Driver":
        driver_info = get_driver_info(driver)
        if type(driver_info) == type([]) and len(driver_info) == 4:
            return True
    return False

def get_driver_info(driver):
    """
    Gets the list of Driver details

    Args:
        driver: A Driver ADT

    Returns:
        driver_info: list of Driver information
    """
    driver_info = driver[1]
    return driver_info

# Gets the Drivers first name
def get_first_name(driver):
    """


    Args:
        driver: A Driver ADT

    Returns:
        f_name: Drivers first name
    """
    f_name = get_driver_info(driver)[0]
    return f_name

def get_last_name(driver):
    """
    Gets the Drivers last name

    Args:
        driver: A Driver ADT

    Returns:
        l_name: Drivers last name
    """
    l_name = get_driver_info(driver)[1]
    return l_name

def get_make_and_model(driver):
    """
    Gets the Drivers car make and model

    Args:
        driver: A Driver ADT

    Returns:
        make_model: Drivers care make and model
    """
    make_model = get_driver_info(driver)[2]
    return make_model

def change_make_and_model(driver, new_make_model):
    """
    Updates the Drivers car make and model

    Args:
        driver: A Driver ADT

    Returns:
        None
    """
    if is_driver(driver):
        driver_info = get_driver_info(driver)
        driver_info[2] = new_make_model
    else:
        print("*\n*   ERROR: ")
        print("*   Didn't receive a Driver\n")

def get_trips_completed(driver):
    """
    Gets the Drivers number of trips completed for the day

    Args:
        driver: A Driver ADT

    Returns:
        trips: Drivers total trips completed
    """
    trips = get_driver_info(driver)[3]
    return trips

def increase_trips_completed(driver):
    """
    Increases the number of trips a Driver makes

    Args:
        driver: A Driver ADT

    Returns:
        None
    """
    driver_info = get_driver_info(driver)
    driver_info[3] = get_trips_completed(driver) + 1

def is_driver_new(driver):
    """
    Determines whether a Driver is new or not

    Args:
        driver: A Driver ADT

    Returns:
        boolean: True or False
    """
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

def add_driver(driver):
    """
    Appends Drivers to the file in a specified format
    
    Args:
        driver: ADT of a Driver
        
    Returns:
       None
    """
    
    try:
        # Makes a folder if it doesn't exist
        os.makedirs(folder_name)
    except FileExistsError:
        # directory already exists
        pass
    
    
    try:
        # Checks to see if path exists
        if os.path.exists(folder_name + file_name):
            # append if the file already exists
            append_write = "a"
        else:
            # make a new file and write
            append_write = "w"
    except IOError as e:
        print("\nThere is an IO Error\n", e)

    first_name = get_first_name(driver)
    last_name = get_last_name(driver)
    make_model = get_make_and_model(driver)
    trips = get_trips_completed(driver)

    file = open(os.path.join(folder_name, file_name), append_write)
    file.write(first_name + "," + last_name + "," \
               + make_model + "," + str(trips) + "\n")
    file.close()

def read_drivers():
    """
    """

    # A list to store the Drivers
    driver_list = list()

    with open( os.path.join(folder_name, file_name), "r") as reader:
        for line in reader.readlines():
            file_line = line.strip().split(",")
            
            f_name = file_line[0]
            l_name = file_line[1]
            make_model = file_line[2]
            trips = int(file_line[3])
            
            driver = make_driver(f_name, l_name, make_model, trips)
            driver_list.append(driver)
            
    reader.close()
    return driver_list

# Adds a Driver to the file
def remove_driver(driver):
    """


    Args:


    Returns:
        None
    """
    # TODO: complete this, currently not urgent
    driver_list = read_drivers()
    position = -1

    if driver in driver_list:
        position = driver_list.index(driver)
    else:
        print("*   This Driver doesn't work with us.")

    if position != -1:
        driver_list.pop(position)
        
        with open(os.path.join(folder_name, file_name), "w") as file:
            for drivers in driver_list:
                first_name = get_first_name(drivers)
                last_name = get_last_name(drivers)
                make_model = get_make_and_model(drivers)
                trips = get_trips_completed(drivers)

                file.write(first_name + "," + last_name + "," \
                           + make_model + "," + str(trips) + "\n")
        print("*   Driver has been removed.")
    file.close()
