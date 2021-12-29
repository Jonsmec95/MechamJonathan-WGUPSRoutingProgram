

# This is the Package class. Each Package is stored as as a unique package object containing it's own data.

class Package:
    def __init__(self, line):
        self.package_id = line[0]
        self.delivery_address = line[1]
        self.delivery_city = line[2]
        self.delivery_state = line[3]
        self.delivery_zip = line[4]
        self.delivery_deadline = line[5]
        self.package_mass = line[6]
        self.delivery_notes = line[7]
        self.delivery_status = 'At Hub'
        self.delivered_time = ''
        self.departure_time = ''

    def __str__(self):
        return str(self.delivery_address)

    def getPackageID(self):
        return int(self.package_id)

    def setPackageID(self, package_id):
        self.package_id = package_id

    def getDeliveryAddress(self):
        return self.delivery_address

    def setDeliveryAddress(self, delivery_address):
        self.delivery_address = delivery_address

    def getDeliveryCity(self):
        return self.delivery_city

    def setDeliveryCity(self, city):
        self.delivery_city = city

    def getDeliveryState(self):
        return self.delivery_state

    def setDeliveryState(self, state):
        self.delivery_state = state

    def getDeliveryZip(self):
        return self.delivery_zip

    def setDeliveryZip(self, zip):
        self.delivery_zip = zip

    def getDeliveryDeadline(self):
        return self.delivery_deadline

    def setDeliveryDeadline(self, deadline):
        self.delivery_deadline = deadline

    def getPackageMass(self):
        return self.package_mass

    def setPackageMass(self, mass):
        self.package_mass = mass

    def getDeliveryNotes(self):
        return self.delivery_notes

    def setDeliveryNotes(self, notes):
        self.delivery_notes = notes

    def getDeliveryStatus(self):
        return self.delivery_status

    def setDeliveryStatus(self, status):
        self.delivery_status = status

    def getDeliveredTime(self):
        return self.delivered_time

    def setDeliveredTime(self, time):
        self.delivered_time = time

    def getDepartureTime(self):
        return self.departure_time

    def setDepartureTime(self, departure):
        self.departure_time = departure
