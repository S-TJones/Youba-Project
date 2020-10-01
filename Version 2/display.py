

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
    print("*\t\t1 - Hire a NEW Driver")
    print("*\t\t2 - View Drivers")
    print("*\t\t3 - Assign Drivers to Locations")
    print("*\t\t4 - Exit")
    print(get_lines())

def customer_options():
    print(get_lines() + "\n*")
    print("*   Wold you like to:")
    print("*\t\t1 - Request a Taxi")
    print("*\t\t2 - View our Locations")
    print("*\t\t3 - Check for Discount")
    print("*\t\t4 - Exit")
    print(get_lines())

def exit_user(user):
    print(get_lines() + "\n*")
    print("* Exiting " + user + " view")
    print("*\n" + get_lines())

def close_function():
    print(get_lines() + "\n*")
    print("* THANK YOU\n* FOR TRYING YOUBA")
    print("\n*\n" + get_lines())
