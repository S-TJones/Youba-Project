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
import driver
import a_queue
import taxi


#################################################################################
# Youba Section
#################################################################################

def youba():
    print("\nWould you like to Request our services?")
    print("Enter Y for Yes")
    print("Enter N for No\n")
    request = input()
    
    while (request == 'Y' or request == 'y'):

        print("What is your phone number?:")
        PassengerTelephoneNumber = int(input())
        print("What is your Location?:")
        PassengerLocation = input()
        print("What is your Destination?:")
        PassengerDestination = input()

        requestTaxi(PassengerTelephoneNumber, PassengerLocation, PassengerDestination)
        
        print()
        print("Would you like to Request our services again?")
        print("Enter Y for Yes")
        print("Enter N for No")
        request = input()
                         
    print()
    print("Thank you for trying Youba. Please come again.")
    print()
    print("A list will be printed upon exit.")
    print('List of Drivers and Number of Jobs Completed :')
    for availabilityQueue in availabilityQueue_LIST:
        for driver in aQueueContents(availabilityQueue):
            print(driver_getFirstName(driver) + ' ' + driver_getLastName(driver) + ' ' + \
                  str(driver_getNumberOfTripsCompleted(driver)))
    print()
    print('List of Locations and Priority Driver :')
    for availabilityQueue in availabilityQueue_LIST:
        if not availabilityQueue_isEmpty(availabilityQueue):
            driver = availabilityQueue_front(availabilityQueue)
            print(availabilityQueue_getLocationName(availabilityQueue) + ' - ' + driver_getFirstName(driver) + ' ' + \
                  driver_getLastName(driver) + ' ' + driver_getCarMakeAndModel(driver))

#################################################################################
# Main Section
#################################################################################

if __name__ == '__main__':
    print("\nWelcome to the Admin side.")
    print("Please setup the Youba data with the neccesary information.\n")
    # Represent the number of Drivers to create
    print("\nPlease enter the number of Drivers you hired: \n")
    no_of_drivers = int(input())

    # Creates the Drivers with input
    for i in range(no_of_drivers):
        print("\nEnter the Drivers information.\nIn the format - \"FirstName, LastName, CarMake&Model, LocationDestination\"")
        print("Currently, there are only 4 Destinations that we cover. There will be more in the Future.")
        print("They are: UWI, Papine, Liguanea & Half-Way-Tree.\n")
        driver_info = input().strip().split(',')
        driver = Driver.driver_make(driver_info[0], driver_info[1], driver_info[2]) # Driver ADT is created
        availabilityQueue_enqueue(getAvailabilityQueue(driver_info[3]), driver) # Driver gets added to a location


    print("\nEnter the number of Previous Passengers that did use our Service.")
    print("Passengers that have used our services before.")
    print("Known passengers get a 10% discount per trip they have failed to take before.\n")
    
    no_of_knownpassengers = int(input())
    knownPassengers = {}

    for i in range(no_of_knownpassengers):
        print("\nIn the format \"####### Failed-trips\"\n")
        print("Please enter the 7-digit phone number for Passenger {} and the number of Failed Attempts: ".format(i+1))
        print()
        knownpassenger = list(map(int, input().strip().split()))
        key = knownpassenger[0]
        value = knownpassenger[1]
        knownPassengers[key] = value

    # Cost price per travel
    print("Please enter the price for a single travel: \n")
    fare = int(input())

    print("Setup now completed.")
    print("Moving on into the User side.")
    youba()

#################################################################################
#################################################################################
