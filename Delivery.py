import datetime

from PackageTable import PackageTable
from DistanceTable import DistanceTable
from Package import Package
from Truck import Truck
from HashTable import HashTable


# Delivery.py contains all the functions involved and used in the delivery process of the packages.
# It goes through loading the trucks, finding the optimal delivery route for the trucks, finding the expected delivery
# times, and generate status and mileage reports.




dt = DistanceTable()
pt = PackageTable()
distance_table_list = dt.get_distance_list()
package_data_list = pt.getPackageDataList()

hash_table = HashTable()
truck_one = Truck()
truck_one.setTruckId(1)
truck_one.setDepartureTime('8:00:00')

truck_two = Truck()
truck_two.setTruckId(2)
truck_two.setDepartureTime('9:00:00')

truck_three = Truck()  # truck_one's second trip
truck_three.setTruckId(3)
truck_three.setDepartureTime('11:00:00')


# This function reads the package file creating package objects. It then organizes the packages and distributes them
# into the trucks.
def loadTrucks():
    for line in package_data_list:
        package = Package(line)

        if 'Wrong address listed' in package.getDeliveryNotes():
            package.setDeliveryAddress('410 S State St.')
            package.setDeliveryZip('84111')
            truck_three.getInventory().append(package)

        if 'Can only be on truck 2' in package.getDeliveryNotes():
            truck_two.getInventory().append(package)

        if 'Delayed on flight' in package.getDeliveryNotes():
            truck_two.getInventory().append(package)

        if package.getPackageID() == 19:
            truck_one.getInventory().append(package)

        if 'EOD' not in package.getDeliveryDeadline():
            if 'Must be delivered with' in package.getDeliveryNotes() or package.getDeliveryNotes() in (None, ""):
                truck_one.getInventory().append(package)

        if 'EOD' in package.getDeliveryDeadline():
            package.setDeliveryDeadline('11:59 PM')

        if package not in truck_one.getInventory() and package not in truck_two.getInventory() and package not in \
                truck_three.getInventory():
            if len(truck_two.getInventory()) < len(truck_three.getInventory()):
                truck_two.getInventory().append(package)
            else:
                truck_three.getInventory().append(package)

        hash_table.insert(package.getPackageID(), package)

# This function finds the optimal route for the truck to take to deliver it's loaded packages. The algorithm used is a
# 'Greedy Algorithm'. It recursively checks the distance between the truck's current location and each package's
# delivery address. Which ever distance is the lowest, it becomes the next visited location.
#


def find_optimal_route(truck, current_location):
    # This is the base case that will stop the function once all the packages are delivered.
    if len(truck.getInventory()) == 0:
        return truck.getInventory()

    else:
        lowest_distance = 100
        next_location = ''
        try:
            # Checks the truck's inventory for which delivery address has the lowest distance.
            for package in truck.getInventory():
                if dt.get_distance(current_location, package.getDeliveryAddress()) <= lowest_distance:
                    lowest_distance = dt.get_distance(current_location, package.getDeliveryAddress())
                    next_location = package.getDeliveryAddress()

            # Checks for packages with the same address and the current address and removes them from the inventory. It
            # then calls upon itself to perform the same operation on it's smaller self.
            for package in truck.getInventory():
                if dt.get_distance(current_location, package.getDeliveryAddress()) == lowest_distance:
                    truck.getOptimalRoute().append(package.getDeliveryAddress())
                    truck.getSortedInventory().append(package)
                    truck.travelled_distance += dt.get_distance(current_location, package.getDeliveryAddress())
                    truck.getInventory().remove(package)
                    current_location = next_location
                    find_optimal_route(truck, current_location)
        except IndexError:
            print('index error')
            pass

# This function calculates the time the truck reaches each delivery address.
def find_delivery_times(truck):
    route = truck.getOptimalRoute()
    sorted_inventory = truck.getSortedInventory()
    departure = truck.getDepartureTime()
    package_departure = truck.getDepartureTime()
    speed = truck.getSpeed()

    (h, m, s) = departure.split(':')
    departure = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    (a, b, c) = package_departure.split(':')
    package_departure = datetime.timedelta(hours=int(a), minutes=int(b), seconds=int(c))

    for i in range(0, len(route)):
        updated_package = hash_table.search(sorted_inventory[i].getPackageID())
        updated_package.setDeliveryStatus('In Transit')
        updated_package.setDepartureTime(package_departure)

        try:
            distance = dt.get_distance(route[i], route[i + 1])
            truck_time = distance / speed
            minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck_time * 60, 60))
            delivery_time = minutes + ':00'
            (h, m, s) = delivery_time.split(':')
            converted_delivery_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            departure += converted_delivery_time

            if updated_package.getDeliveryAddress() in route[i]:
                updated_package.setDeliveredTime(departure)
                updated_package.setDeliveryStatus('Delivered')
                # print(updated_package.getPackageID(), ' delivered at: ', updated_package.getDeliveredTime(),
                #       'deadline: ', updated_package.getDeliveryDeadline())

                hash_table.insert(updated_package.getPackageID(), updated_package)


        except IndexError:
            if updated_package.getDeliveryAddress() in route[i]:
                updated_package.setDeliveredTime(departure)
                updated_package.setDeliveryStatus('Delivered')
                # print(updated_package.getPackageID(), ' delivered at: ', updated_package.getDeliveredTime(),
                #       'deadline: ', updated_package.getDeliveryDeadline())

                hash_table.insert(updated_package.getPackageID(), updated_package)


# This function generates a report of every package at a given time.
def generate_status_report(specific_time):
    package_id_count = len(truck_one.getOptimalRoute()) + len(truck_two.getOptimalRoute()) + len(
        truck_three.getOptimalRoute())
    i = 1

    specific_time += ':00'
    (h, m, s) = specific_time.split(':')
    converted_specific_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    print('\n' + '{:-^150}'.format('DELIVERY STATUS REPORT AT: ' + specific_time))
    print('PACKAGES:')

    while i <= package_id_count:
        package = hash_table.search(i)
        package_status = 'no status'
        if converted_specific_time < package.getDepartureTime():
            package_status = 'At Hub'

        elif package.getDeliveredTime() > converted_specific_time:
            package_status = 'In Transit'

        elif package.getDeliveredTime() <= converted_specific_time:
            package_status = 'Delivered'

        if package_status == 'Delivered':
            delivered_at = str(package.getDeliveredTime())

        else:
            delivered_at = ''


        print('Package ID:', '{:<5}'.format(package.getPackageID()), 'Delivery Deadline:',
              '{:<10}'.format(package.getDeliveryDeadline()), 'Delivery Address:',
              '{:<70}'.format(
                  package.getDeliveryAddress() + ', ' + package.getDeliveryCity() + ', ' + package.getDeliveryZip()),
              'Package Weight:', '{:<10}'.format(package.getPackageMass() + ' Kilo'), 'Package status:', '{:<15}'.format(package_status),
              'Delivery Time:', '{:<10}'.format(str(package.getDeliveredTime())))
        i += 1


# This function generates a report of a individual truck's mileage, optimal route, and total packages.
def generate_truck_data_report(truck):
    print('\nTRUCK:', truck.getTruckId())
    print('Optimal Route:', truck.getOptimalRoute())
    print('Traveled Distance:', truck.getTravelledDistance())
    print('Total Packages:', len(truck.getSortedInventory()))
