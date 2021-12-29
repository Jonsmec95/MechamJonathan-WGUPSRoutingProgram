import csv

# This class creates a table to store the information from the distance file. It also contains the functions necessary
# to access the distance table's data.

class DistanceTable:

    def __init__(self):
        self.distance_list = []
        self.distance_index = {}

        f = open('data/distanceTable2.csv', 'r')
        reader = csv.reader(f, delimiter=',')
        row_zero = list(next(reader))  # skips first line

        self.distance_list = list(reader)  # stores file as list
        f.seek(0)  # starts the reader over
        row_zero = list(next(reader))  # skips first line again

        row_count = 0
        for line in reader:
            key = line[0].replace('\n', '').replace('(', ' ').replace(')', '')
            self.distance_index[key] = row_count
            row_count += 1

        index = self.distance_index['1060 Dalton Ave S 84104']
        index_two = self.distance_index['195 W Oakland Ave 84115']


    def get_distance_list(self):
        return self.distance_list

    # This function looks up the distance between two addresses.
    def get_distance(self, from_address, to_address):

        from_address = [val for key, val in self.distance_index.items() if from_address in key]
        to_address = [val for key, val in self.distance_index.items() if to_address in key]

        distance = self.distance_list[from_address[0]][to_address[0] + 1]

        if distance == '':
            distance = self.distance_list[to_address[0]][from_address[0] + 1]
        return float(distance)




