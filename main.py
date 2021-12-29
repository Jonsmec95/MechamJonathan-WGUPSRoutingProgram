
# Jonathan S. Mecham
# Student ID: 001311375

from DistanceTable import DistanceTable as DistanceTable
import Delivery


# This is the main class of the program. It creates the UI allowing the user to run the operations of the program.

class Main:
    distance = DistanceTable()
    Delivery.loadTrucks()

    Delivery.find_optimal_route(Delivery.truck_one, ' HUB')
    Delivery.find_optimal_route(Delivery.truck_two, ' HUB')
    Delivery.find_optimal_route(Delivery.truck_three, ' HUB')

    Delivery.find_delivery_times(Delivery.truck_one)
    Delivery.find_delivery_times(Delivery.truck_two)
    Delivery.find_delivery_times(Delivery.truck_three)

    main_menu = ('\nWelcome to the WGUPS Routing Program. Please select one of the following options:'
                 + '\n 1) Look up Package'
                 + '\n 2) Delivery status report at specific time'
                 + '\n 3) Truck route and mileage data report '
                 + '\n 4) Exit')

    print(main_menu)
    user_input = input('\nEnter the corresponding option number here:')

    while user_input != '4':
        if user_input == '1':
            input_package_id = input("enter package ID number or enter '0' to return to main menu: ")
            lookup_package = Delivery.hash_table.search(int(input_package_id))
            if input_package_id != '0':
                print('\n Package ID:', '{:<5}'.format(lookup_package.getPackageID())
                      + '\n Delivery Deadline:', '{:<10}'.format(lookup_package.getDeliveryDeadline())
                      + '\n Delivery Address:', '{:<50}'.format(
                    lookup_package.getDeliveryAddress() + ', ' + lookup_package.getDeliveryCity() + ', ' + lookup_package.getDeliveryZip())
                      + '\n Package Weight:', '{:<10}'.format(lookup_package.getPackageMass() + ' Kilo')
                      + '\n Delivery Status:', lookup_package.getDeliveryStatus()
                      + '\n Delivery Time:', lookup_package.getDeliveredTime(), '\n')
            else:
                print(main_menu)
                user_input = input('\nEnter the corresponding option number here:')

        elif user_input == '2':
            input_time = input("Please enter time in HH:MM format or enter '0' to return to main menu:")
            if input_time != '0':
                Delivery.generate_status_report(input_time)
                print('\n' + '{:-^150}'.format(''))

            else:
                print(main_menu)
                user_input = input('\nEnter the corresponding option number here:')

        elif user_input == '3':
            print('\n' + '{:-^150}'.format('TRUCK MILEAGE AND ROUTE REPORT'))
            Delivery.generate_truck_data_report(Delivery.truck_one)
            Delivery.generate_truck_data_report(Delivery.truck_two)
            Delivery.generate_truck_data_report(Delivery.truck_three)
            total_mileage = Delivery.truck_one.getTravelledDistance() + Delivery.truck_two.getTravelledDistance() + Delivery.truck_three.getTravelledDistance()
            print('\nTotal Truck Mileage:', total_mileage)
            print('\n' + '{:-^150}'.format(''))
            print(main_menu)
            user_input = input('\nEnter the corresponding option number here:')
    exit()
