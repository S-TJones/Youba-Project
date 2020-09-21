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

# List of Availability Queues
a_queue_list = []

# Creates an Availability Queue
def make_availability_queue(location):
    a_queue = ("AvailabilityQueue", location, [])
    return a_queue

# Gets Availability Queue contents
def get_queue_contents(a_queue):
    return a_queue[2]

# Gets the Availability Queue from the list based on location
def get_a_queue(location_name):
    for a_queue in a_queue_list:
        if get_location(a_queue) == location_name:
            return a_queue
    print("\nThere are no Availability Queues for this location.\n")
    return make_availability_queue("")

# Check if an Availability Queue is empty/ doesn't exist...
# ... this is separate from an availability queue not having drivers
def is_a_queue(a_queue):
    if get_location(a_queue) == "":
        return False
    return True

# Gets the Availability Queue location name
def get_location(a_queue):
    return get_driver_info(a_queue)

# Returns the first Driver in the Availability Queue list
def a_queue_front(a_queue):
    if is_a_queue_empty(a_queue):
        print("\nThere are no Taxi Drivers present at the moment.\n")
        return make_availability_queue("")
    else:
        return get_queue_contents(a_queue)[0]

# Adds a driver to an Availability Queue list
def a_queue_enqueue(a_queue, driver):
    get_queue_contents(a_queue).append(driver)

# Removes a driver from an Availability Queue list
def a_queue_dequeue(a_queue):
    if is_a_queue_empty(a_queue):
        print("\nERROR.\nThere are no Drivers at this Location to remove.\n")
    else:
        get_queue_contents(a_queue).pop(0)

# Checks to see if an Availability Queue is Empty
def is_a_queue_empty(a_queue):
    if get_queue_contents(a_queue) == []:
        return True
    return False

# Adds an Availability Queue to the list of Availability Queues
def add_a_queue(a_queue):
    a_queue_list.append(a_queue)

# Removes an Availability Queue from the list of Availability Queues
def remove_a_queue(a_queue):
    x = -1
    for i in range(len(a_queue_list)):
        if a_queue_list[i] == a_queue:
            x = i
            break
    
    if x != -1:
        a_queue_list.pop(x)
    else:
        print("\nThere are no Availability Queues for this location.\n")

#################################################################################
# Global Availability Queue Section
#################################################################################

# Makes new Availability Queues
a_queue_UWI = make_availability_queue("UWI")
a_queue_Papine = make_availability_queue("Papine")
a_queue_Liguanea = make_availability_queue("Liguanea")
a_queue_HalfWayTree = make_availability_queue("Half-Way-Tree")

# Adds to the list of Available Queues
add_a_queue(a_queue_UWI)
add_a_queue(a_queue_Papine)
add_a_queue(a_queue_Liguanea)
add_a_queue(a_queue_HalfWayTree)
