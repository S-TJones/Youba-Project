#################################################################################

"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""


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