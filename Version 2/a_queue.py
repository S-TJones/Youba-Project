#################################################################################

"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""

import os
from driver import get_driver_info

#################################################################################
# Availability Queue Section
#################################################################################

def make_availability_queue(location):
    """
    Creates an Availability Queue

    Args:
        location: A location

    Returns:
        a_queue: An Availability Queue ADT
    """
    a_queue = ("AvailabilityQueue", location, [])
    return a_queue

def get_queue_contents(a_queue):
    """
    Gets Availability Queue contents

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        queue_contents: The list of Drivers at an Availability Queue
    """
    queue_contents = a_queue[2]
    return queue_contents

def get_a_queue(location_name, a_queue_list):
    """
    Gets the Availability Queue from the list based on location

    Args:
        location_name: A location
        a_queue_list: A list of Availability Queues

    Returns:
        a_queue: An Availability Queue ADT
    """
    for a_queue in a_queue_list:
        if get_location(a_queue) == location_name:
            return a_queue
    print("There are no Availability Queues for this location.")
    return make_availability_queue("")

def is_a_queue(a_queue):
    """
    Check if an Availability Queue is empty/ doesn't exist.
    This is separate from an availability queue not having drivers.

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        boolean: True or False
    """
    if get_location(a_queue) == "":
        return False
    return True

def get_location(a_queue):
    """
    Gets the Availability Queue location name

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        location: The location of an Availability Queue
    """
    location = get_driver_info(a_queue)
    return location

def a_queue_front(a_queue):
    """
    Returns the first Driver in the Availability Queue list

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        driver: An ADT representing a Driver
    """
    if is_a_queue_empty(a_queue):
        print("\nThere are no Taxi Drivers present at the moment.\n")
        return make_availability_queue("")
    else:
        return get_queue_contents(a_queue)[0]

def a_queue_enqueue(a_queue, driver):
    """
    Adds a driver to an Availability Queue list

    Args:
        a_queue: An Availability Queue ADT
        driver: A Driver ADT

    Returns:
        None
    """
    get_queue_contents(a_queue).append(driver)

def a_queue_dequeue(a_queue):
    """
    Removes a driver from an Availability Queue list

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        None
    """
    if is_a_queue_empty(a_queue):
        print("\nERROR.\nThere are no Drivers at this Location to remove.\n")
    else:
        get_queue_contents(a_queue).pop(0)

def is_a_queue_empty(a_queue):
    """
    Checks to see if an Availability Queue is Empty

    Args:
        a_queue: An Availability Queue ADT

    Returns:
        boolean: True or False
    """
    if get_queue_contents(a_queue) == []:
        return True
    return False

def add_a_queue(a_queue, a_queue_list):
    """
    Adds an Availability Queue to the list of Availability Queues

    Args:
        a_queue: An Availability Queue ADT
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    a_queue_list.append(a_queue)

def remove_a_queue(a_queue, a_queue_list):
    """
    Removes an Availability Queue from the list of Availability Queues

    Args:
        a_queue: An Availability Queue ADT
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    x = -1
    for i in range(len(a_queue_list)):
        if a_queue_list[i] == a_queue:
            x = i
            break
    
    if x != -1:
        a_queue_list.pop(x)
    else:
        print("There are no Availability Queues for this location.\n")

#################################################################################
# Driver Files Section
#################################################################################

# File with all the Driver Information
file_name = "Youba_Locations.txt"
folder_name = "./Text-Files/"

def add_location(a_queue):
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
