class Hotel:
    def __init__(self, name, address, number_of_rooms, price_night, services):
        self.name = name
        self.address = address
        self.number_of_rooms = number_of_rooms
        self.price_night = price_night
        self.services = services

    # Define a reprJSON method that returns a dict of the attributes
    def reprJSON(self):
        return self.__dict__

