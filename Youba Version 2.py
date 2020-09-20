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

#################################################################################

"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""

        
#################################################################################
# Driver Section
#################################################################################

def driver_make(firstName, lastName, carMakeAndModel1):
    numberOfTripsCompleted = 0
    return ("Driver", [firstName, lastName, carMakeAndModel1, \
            numberOfTripsCompleted] )

def getDriverInfo(ADT):
    return ADT[1]

def driver_getFirstName(Driver):
    return getDriverInfo(Driver)[0]

def driver_getLastName(Driver):
    return getDriverInfo(Driver)[1]

def driver_getCarMakeAndModel(Driver):
    return getDriverInfo(Driver)[2]

def driver_getNumberOfTripsCompleted(Driver):
    return getDriverInfo(Driver)[3]

def driver_increaseTripsCompleted(Driver):
    getDriverInfo(Driver)[3] = driver_getNumberOfTripsCompleted(Driver) + 1

def driver_isNewDriver(Driver):
    num = driver_getNumberOfTripsCompleted(Driver)
    if num == 0:
        return True
    return False

#################################################################################
# Availability Queue Section
#################################################################################

def availabilityQueue_make(Location):
    return ("AvailabilityQueue", Location, [])

def aQueueContents(AvailabilityQueue):
    return AvailabilityQueue[2]

def getAvailabilityQueue(LocationName):
    for availabilityQueue in  availabilityQueue_LIST:
        if availabilityQueue_getLocationName(availabilityQueue) == LocationName:
            return availabilityQueue
            
    return availabilityQueue_make("")

def availabilityQueue_getLocationName(A_Queue):
    return getDriverInfo(A_Queue)

def availabilityQueue_front(A_Queue):
    if availabilityQueue_isEmpty(A_Queue):
        return "There are no Taxi Drivers present at the moment."
    else:
        return aQueueContents(A_Queue)[0]
    
def availabilityQueue_enqueue(A_Queue, Driver):
    aQueueContents(A_Queue).append(Driver)
            
def availabilityQueue_dequeue(A_Queue):
    if availabilityQueue_isEmpty(A_Queue):
        print("ERROR.\nThere are no Drivers at this Location to remove.")
    else:
        aQueueContents(A_Queue).pop(0)

def availabilityQueue_isEmpty(A_Queue):
    if aQueueContents(A_Queue) == []:
        return True
    return False

#################################################################################
# Global Queue Section
#################################################################################

availabilityQueue_UWI = availabilityQueue_make('UWI')
availabilityQueue_Papine = availabilityQueue_make('Papine')
availabilityQueue_Liguanea = availabilityQueue_make('Liguanea')
availabilityQueue_HalfWayTree = availabilityQueue_make('Half-Way-Tree')

# Creates a list of Available Locations
availabilityQueue_LIST = [availabilityQueue_UWI, availabilityQueue_Papine, availabilityQueue_Liguanea, \
                              availabilityQueue_HalfWayTree]

#################################################################################
# Fair Calculation Section
#################################################################################
        
def calculateDiscount(PassengerTelephoneNumber):
    for Number, Failed_Attempts in knownPassengers.items():
        if Number == PassengerTelephoneNumber:
            return Failed_Attempts * 0.10

    knownPassengers[PassengerTelephoneNumber] = 0
    return 0.00

def calculateFare(PassengerTelephoneNumber):

    Discount = calculateDiscount(PassengerTelephoneNumber)
        
    Discounted_Fare = fare - (fare*Discount)
        
    if Discounted_Fare < 0.00:
        return 0.00
    return Discounted_Fare

#################################################################################
# Taxi Section
#################################################################################
        
def moveTaxi(startLocation, endLocation):
    if availabilityQueue_isEmpty( getAvailabilityQueue(startLocation) ):
        print("No driver at location.")
    else:
        Driver = availabilityQueue_front( getAvailabilityQueue(startLocation) )
        availabilityQueue_dequeue( getAvailabilityQueue(startLocation) )
        availabilityQueue_enqueue( getAvailabilityQueue(endLocation), Driver)
        driver_increaseTripsCompleted(Driver)
            
def requestTaxi(PassengerTelephoneNumber, PassengerLocation, PassengerDestination):
    if PassengerLocation == PassengerDestination:
        print ("Start and end locations are the same!")
    else:
        # Fare for the trip is calculated
        trip_fare = calculateFare(PassengerTelephoneNumber)
        print()
        print("Your fare is ${}.".format(trip_fare))
        print()

        option = input('Enter "Y" to confirm the trip or "N" to cancel - ')
        if option == "Y" or option == "y":
            if availabilityQueue_isEmpty( getAvailabilityQueue(PassengerLocation) ):
                knownPassengers[PassengerTelephoneNumber] += 1
                print("Unfortunately, there are no drivers at that location.")
                print("We apologize for any inconvenience.")
                print("You will receive a 10% discount on your next trip.")
                print()
            else:
                print("\nA Taxi is on the way.\n")
                moveTaxi(PassengerLocation, PassengerDestination)
        else:
            print()
            print("")

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
        driver = driver_make(driver_info[0], driver_info[1], driver_info[2]) # Driver ADT is created
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
