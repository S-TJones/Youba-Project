#################################################################################

"""
Youba Ltd. is a startup company that aims to revolutionize the local public transportation by
introducing a brand new way for travellers to connect with drivers. Users only need
to have a cellphone to utilize the service. Given your knowledge of ADTs, Youba Ltd.
has contracted you to implement the platform for thier service.
"""


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