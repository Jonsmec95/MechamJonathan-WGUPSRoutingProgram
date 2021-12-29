import csv

# This class reads the package file in as a list so the data is able to be added to packages.

class PackageTable:

    def __init__(self):
        self.package_data_list = []

        with open('./data/WGUPS_Package_File.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')

            # skip file header
            header_count = 0
            while header_count < 8:
                next(csv_reader, None)
                header_count += 1

            self.package_data_list = list(csv_reader)

    def getPackageDataList(self):
        return self.package_data_list

    def setPackageDataList(self, new_list):
        self.package_data_list = new_list
