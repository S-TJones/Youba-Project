#################################################################################

"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""

import a_queue as q
from driver import increase_trips_completed

lines = "********************************************************************"

#################################################################################
# Fair Calculation Section
#################################################################################

# Calculates the discount for a customer
def calculate_discount(phone_num, passengers):
    """
    Calculates the discount to be applied for a customer

    Args:
        phone_num: Customers telephone number
        passengers: Dictionary of Customers information

    Returns:
        failed_attempts: A float value of discounted price
    """
    
    for number, failed_attempts in passengers.items():
        if number == phone_num:
            return failed_attempts * 0.10

    passengers[phone_num] = 0
    return 0.00

# Calculates the final fare for the customer
def calculate_fare(phone_num, price, passengers):
    """
    Calculates the customers total fare after discount has been applied

    Args:
        phone_num: Customers telephone number
        price: The cost per taxi trip
        passengers: Dictionary of Customers information

    Returns:
        discounted_fare: Discounted price
    """

    discount = calculate_discount(phone_num, passengers)
        
    discounted_fare = price - (price*discount)
        
    if discounted_fare < 0.00:
        return 0.00
    return discounted_fare

#################################################################################
# Taxi Section
#################################################################################

# Moves a Driver from one location to the other
def move_taxi(start_location, end_location, a_queue_list):
    """
    Moves a taxi from one location to another with an Availability Queue list

    Args:
        start_location: Customers current location
        end_location: Customers desired destination
        a_queue_list: A list of Availability Queues

    Returns:
        None
    """
    if q.is_a_queue_empty( q.get_a_queue(start_location, a_queue_list) ):
        print("*   No driver at location.\n")
    else:
        driver = q.a_queue_front( q.get_a_queue(start_location, a_queue_list) )
        q.a_queue_dequeue( q.get_a_queue(start_location, a_queue_list) )
        q.a_queue_enqueue( q.get_a_queue(end_location, a_queue_list), driver)
        increase_trips_completed(driver)
            
def request_taxi(passenger_phone_num, passenger_location, passenger_destination, price, passengers, a_queue_list):
    """
    Requests a taxi for a customer at a specific location
    
    Args:
        passenger_phone_num: Customers telephone number
        passenger_location: Customers current location
        passenger_destination: Customers desired destination
        price: Cost per trip
        passengers: A dictionary of customers and their failed attempts
        a_queue_list: A list of Availability Queues
        
    Returns:
       None
    """
    if passenger_location == passenger_destination:
        print ("\n*\n*   Start and end locations are the same!\n*\n")
    else:
        # Fare for the trip is calculated
        trip_fare = calculate_fare(passenger_phone_num, price, passengers)
        print("*   Your final fare is ${}.".format(trip_fare))

        option = input("*   Enter \"Y\" to confirm the trip or \"N\" to cancel - ")
        if option == "Y" or option == "y":
            if q.is_a_queue_empty( q.get_a_queue(passenger_location, a_queue_list) ):
                passengers[passenger_phone_num] += 1
                print("\n*   Unfortunately, there are no drivers at that location.")
                print("*   We apologize for any inconvenience.")
                print("*   You will receive a 10% discount on your next trip.")
            else:
                print(lines)
                print("*   A Taxi is on the way.\n")
                print(lines)
                move_taxi(passenger_location, passenger_destination, a_queue_list)
        else:
            print(lines)
            print("*   Cancelling trip")
            print(lines)
