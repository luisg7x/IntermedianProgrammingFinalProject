class Hotel:
    def __init__(self, name, address, number_of_rooms, available_rooms, price_night, services):
        self.name = name
        self.address = address
        self.number_of_rooms = number_of_rooms
        self.available_rooms = available_rooms
        self.price_night = price_night
        self.services = services

    # Define a reprJSON method that returns a dict of the attributes
    def reprJSON(self):
        return self.__dict__
    
    # Implementing the __getitem__ method to allow subscripting
    def __getitem__(self, key):
        return getattr(self, key)

