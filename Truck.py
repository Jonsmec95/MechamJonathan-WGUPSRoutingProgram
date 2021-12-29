
# This is the Truck Class. Each truck is created as it's own Truck object containing it's own data.
class Truck:
    def __init__(self):
        self.truck_id = 0
        self.inventory = []
        self.sorted_inventory = []
        self.optimal_delivery_route = []
        self.speed = 18
        self.current_location = "HUB"
        self.departure_time = ""
        self.travelled_distance = 0

    def getInventory(self):
        return self.inventory

    def setInventory(self, inventory):
        self.inventory = inventory

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def getCurrentLocation(self):
        return self.current_location

    def setCurrentLocation(self, location):
        self.current_location = location

    def getDepartureTime(self):
        return self.departure_time

    def setDepartureTime(self, time):
        self.departure_time = time

    def getTruckId(self):
        return self.truck_id

    def setTruckId(self, truck_id):
        self.truck_id = truck_id

    def getOptimalRoute(self):
        return self.optimal_delivery_route

    def getTravelledDistance(self):
        return self.travelled_distance

    def setSortedInventory(self, new_list):
        self.sorted_inventory = new_list

    def getSortedInventory(self):
        return self.sorted_inventory
