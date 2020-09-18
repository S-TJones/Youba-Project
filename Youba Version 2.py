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
    return 0.00

def calculateFare(StartLocation, EndLocation, PassengerTelephoneNumber):

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
        return
    else:
        Driver = availabilityQueue_front( getAvailabilityQueue(startLocation) )
        availabilityQueue_dequeue( getAvailabilityQueue(startLocation) )
        availabilityQueue_enqueue( getAvailabilityQueue(endLocation), Driver)
        driver_increaseTripsCompleted(Driver)
            
def requestTaxi(PassengerTelephoneNumber, PassengerLocation, PassengerDestination):
    if PassengerLocation == PassengerDestination:
        print ("Start and end locations are the same!")
    else:
        Fare = calculateFare(PassengerLocation, PassengerDestination, \
                PassengerTelephoneNumber)
        
        print(Fare)
        
        Option = input('Enter "Y" to confirm the trip or "N" to cancel -')
        if Option == "Y":
            if availabilityQueue_isEmpty( getAvailabilityQueue(PassengerLocation) ):
                knownPassengers[PassengerTelephoneNumber] += 1
                print('No driver available')
                return
            else:
                moveTaxi(PassengerLocation, PassengerDestination)
                knownPassengers[PassengerTelephoneNumber] = 0
        else:
            return

#################################################################################
# Youba Section
#################################################################################        

def youba():
    Option = input('Enter "Y" to request a taxi or "N" to end use of the service for that period')
    count = 0
    while Option == "Y":
        # Reply Format is: number, start, end
        x = list( passenger_list[count].strip().split() )
        requestTaxi( int(x[0]), x[1], x[2])
        count += 1
        Option = input('Enter "Y" to request a taxi or "N" to end use of the service for that period')
    
    print()
    if Option == "N":
        for A_Queue in availabilityQueue_LIST:
            if availabilityQueue_isEmpty(A_Queue):
                pass
            else:
                Driver_List = aQueueContents(A_Queue)
                for Driver in Driver_List:
                    print(driver_getFirstName(Driver)+" "+driver_getLastName(Driver)+" "+ str(driver_getNumberOfTripsCompleted(Driver) ) )
        for A_Queue in availabilityQueue_LIST:
            if availabilityQueue_isEmpty(A_Queue):
                pass
            else:
                n = 0
                Driver_List = aQueueContents(A_Queue)
                print(availabilityQueue_getLocationName(A_Queue) + " - " + driver_getFirstName(Driver_List[n]) + " " + driver_getLastName(Driver_List[n]) + " " + driver_getCarMakeAndModel(Driver_List[n]))

#################################################################################
# Youba Executer Section
#################################################################################  

def youba_main():
    request = input()
    n = -1
    while (request == 'Y'):
        n += 1
        passenger = passenger_list[n].split()
        PassengerTelephoneNumber = int(passenger[0])
        PassengerLocation = passenger[1]
        PassengerDestination = passenger[2]
        requestTaxi(PassengerTelephoneNumber, PassengerLocation, PassengerDestination)
        request = input()
                         
    print()
    print()
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
    # Represent the number of Drivers to create
    print("Please enter the number of Drivers you hired: \n")
    no_of_drivers = int(input())

    # Creates the Drivers with input
    for i in range(no_of_drivers):
        print("Enter the Drivers information.\nIn the format - \"FirstName, LastName, CarMake&Model, LocationDestination\"")
        driver_info = input().strip().split(',')
        driver = driver_make(driver_info[0], driver_info[1], driver_info[2])
        availabilityQueue_enqueue(getAvailabilityQueue(driver_info[3]), driver)
    no_of_passengers = int(input())
    passenger_list = []

    for i in range(no_of_passengers):
        passenger = input()
        passenger_list += [passenger]
    no_of_knownpassengers = int(input())

    knownPassengers = {}
    for i in range(no_of_knownpassengers):
        knownpassenger = list(map(int, input().strip().split()))
        key = knownpassenger[0]
        value = knownpassenger[1]
        knownPassengers[key] = value

    # Cost price per travel
    print("Please enter the price for a single travel: \n")
    fare = int(input())

    youba_main()

#################################################################################
#################################################################################
