#################################################################################

"""
 This assignment is worth 15% of your course mark.
 You are to work in pairs - Shemar Jones and Neisha Brown.
 Ensure both team member's ID numbers are included in the submitted code - 620117968 and 620117112
 Submit well documented, original code using the container on OurVLE.
 Name your file by concatenating the last four (4) digits of each member's ID# and prefix...
 ... the concatenated digits with the characters "A1127".
 The deadline for submission is midnight Sunday, December 2, 2018.
 Late assignments are not encouraged. However, these are accepted and graded then...
 ... 10% deducted for each day of late submission.
"""

"""#from Driver import *"""
# My code editor told me not to import with wildcard; LOL
import driver as d
import a_queue as q
import taxi as t


#################################################################################
# Youba Section
#################################################################################

def youba():
    """
    Handles the Customer side of the service

    Args:
        None

    Returns:
        None
    """
    print(lines)
    print("*   Currently, there are only 4 Destinations that we cover.\n*   There will be more in the Future.")
    print("*   They are: UWI, Papine, Liguanea & Half-Way-Tree.")
    print("*   The price per trip is ${}\n*   Discounts will be added where neccessary.".format(fare))
    print(lines)
    print("*   Would you like to Request our services?")
    print("*   Enter Y for Yes")
    print("*   Enter N for No\n")
    request = input()
    
    while (request == "Y" or request == "y"):
        print(lines)
        print("*   What is your phone number?:")
        passenger_phone_num = int(input())
        print("*   What is your Location?:")
        passenger_location = input()
        print("*   What is your Destination?:")
        passenger_destination = input()

        t.request_taxi(passenger_phone_num, passenger_location, \
            passenger_destination, fare, known_passengers, a_queue_list)
 
        print("\n*   Would you like to Request our services again?")
        print("*   Enter Y for Yes")
        print("*   Enter N for No")
        request = input()
    
    print(lines)
    print("Thank you for trying Youba. Please come again.\n")
    print("A list will be printed upon exit.")
    print("List of Drivers and Number of Jobs Completed.")
    
    for a_queue in a_queue_list:
        for driver in q.get_queue_contents(a_queue):
            print(d.get_first_name(driver) + "\t" + d.get_last_name(driver) + "\t" + \
                    str(d.get_trips_completed(driver)))
    print(lines)
    print("*   List of Locations and Drivers for those that worked today.")
    print("* Current Location\tDriver Name\tCar Make & Model")
    
    for a_queue in a_queue_list:
        if not q.is_a_queue_empty(a_queue):
            driver = q.a_queue_front(a_queue)
            print("* " + q.get_location(a_queue) + "\t\t" + d.get_first_name(driver) + " " + \
                  d.get_last_name(driver) + "\t\t" + d.get_make_and_model(driver))

#################################################################################
# Main Section
#################################################################################

if __name__ == '__main__':
    lines = "********************************************************************"
    print(lines)
    print("*   Welcome to the Admin side.")
    print("*   Please setup the Youba data with the neccesary information.")
    print(lines + "\n")

    # Makes new Availability Queues
    a_queue_UWI = q.make_availability_queue("UWI")
    a_queue_Papine = q.make_availability_queue("Papine")
    a_queue_Liguanea = q.make_availability_queue("Liguanea")
    a_queue_HalfWayTree = q.make_availability_queue("Half-Way-Tree")

    # A list of queues
    a_queue_list = list() # TODO Generate a list of Availability Queues
    # A dictionary of customers and their failed attempts
    known_passengers = dict() # Generate a dictionary of customer info

    # Adds to the list of Available Queues
    q.add_a_queue(a_queue_UWI, a_queue_list) # TODO Automate this or allow user to customize
    q.add_a_queue(a_queue_Papine, a_queue_list)
    q.add_a_queue(a_queue_Liguanea, a_queue_list)
    q.add_a_queue(a_queue_HalfWayTree, a_queue_list)

    # Represent the number of Drivers to create
    print(lines)
    print("*   Please enter the number of new Drivers you hired.")
    print("*   Our travel locations are: UWI, Papine, Liguanea & Half-Way-Tree.")
    # TODO Read from file all travel locations and display - replace the line above
    no_of_drivers = int(input())

    # Creates the Drivers with input information
    for i in range(no_of_drivers):
        print("*   Enter the Drivers information.\n*   In the format - \"FirstName, LastName, CarMake|Model, LocationDestination\"")
        
        driver_info = input().strip().split(",")
        driver = d.make_new_driver(driver_info[0], driver_info[1], driver_info[2]) # Driver ADT is created
        q.a_queue_enqueue(q.get_a_queue(driver_info[3], a_queue_list), driver) # Driver gets added to a location

    print("\n" + lines)
    print("*   Enter the number of Previous Passengers that did use our Service.")
    print("*   Passengers that have used our services before.")
    print("*   Known passengers get a 10% discount per trip they have failed to take before.")
    
    no_of_known_passengers = int(input())

    for i in range(no_of_known_passengers):
        print("\n*   In the format \"#######,Failed-trips\"")
        print("*   Please enter the 7-digit phone number for Passenger {} and the number of Failed Attempts: ".format(i+1))
        passenger = list(map(int, input().strip().split(",")))
        key = passenger[0]
        value = passenger[1]
        known_passengers[key] = value

    # Cost price per travel
    fare = float(input("\n*   Please enter the price for a single travel: $"))

    print("\n" + lines + "\n" + lines)
    print("*   Setup now completed.")
    print("*   Moving on into the User side.")
    print(lines + "\n")
    youba()

#################################################################################
#################################################################################
