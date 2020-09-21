#################################################################################

"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""

import a_queue as q
from driver import increase_trips_completed

#################################################################################
# Fair Calculation Section
#################################################################################

# Calculates the discount for a customer
def calculate_discount(phone_num):
    for number, failed_attempts in known_passengers.items():
        if number == phone_num:
            return failed_attempts * 0.10

    known_passengers[phone_num] = 0
    return 0.00

# Calculates the final fare for the customer
def calculate_fare(phone_num):

    discount = calculate_discount(phone_num)
        
    discounted_fare = fare - (fare*discount)
        
    if discounted_fare < 0.00:
        return 0.00
    return discounted_fare

#################################################################################
# Taxi Section
#################################################################################

# Moves a Driver from one location to the other
def move_taxi(start_location, end_location):
    if q.is_a_queue_empty( q.get_a_queue(start_location) ):
        print("No driver at location.\n")
    else:
        driver = q.a_queue_front( q.get_a_queue(start_location) )
        q.a_queue_dequeue( q.get_a_queue(start_location) )
        q.a_queue_enqueue( q.get_a_queue(end_location), driver)
        increase_trips_completed(driver)
            
def request_taxi(passenger_phone_num, passenger_location, passenger_destination):
    if passenger_location == passenger_destination:
        print ("Start and end locations are the same!\n")
    else:
        # Fare for the trip is calculated
        trip_fare = calculate_fare(passenger_phone_num)
        print()
        print("Your fare is ${}.".format(trip_fare))
        print()

        option = input("\nEnter \"Y\" to confirm the trip or \"N\" to cancel - ")
        if option == "Y" or option == "y":
            if q.is_a_queue_empty( q.get_a_queue(passenger_location) ):
                known_passengers[passenger_phone_num] += 1
                print("Unfortunately, there are no drivers at that location.")
                print("We apologize for any inconvenience.")
                print("You will receive a 10% discount on your next trip.\n")
                print()
            else:
                print("A Taxi is on the way.\n")
                move_taxi(passenger_location, passenger_destination)
        else:
            print()
            print("Cancelling trip\n")
