

def get_lines():
    lines = "********************************************************************"
    return lines

def intro():
    print("\n" + get_lines())
    print("*   Are you an Admin or Customer?\n*")
    print("*   Enter \'Y\' for Admin.")
    print("*   Enter \'N\' for Customer.\n*")

def welcome(user):
    print(get_lines() + "\n*")
    print("*   Welcome to the " + user + " side.\n*")
    print(get_lines())

def admin_options():
    print(get_lines() + "\n*")
    print("*   Wold you like to:")
    print("*\t\t1 - ")
    print("*\t\t2 - ")
    print("*\t\t3 - ")
    print("*\t\t4 - ")
    print(get_lines())

def customer_options():
    print(get_lines() + "\n*")
    print("*   Wold you like to:")
    print("*\t\t1 - Request a Taxi")
    print("*\t\t2 - View our Locations")
    print("*\t\t3 - Check for Discount")
    print("*\t\t4 - Exit")
    print(get_lines())