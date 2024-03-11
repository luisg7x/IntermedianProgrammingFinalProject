class Service:
    def __init__(self, id, name, schedule, price, availability, capacity, location):
        self.id = id
        self.name = name
        self.schedule = schedule
        self.price = price
        self.availability = availability
        self.capacity = capacity
        self.location = location

    # Implementing the __getitem__ method to allow subscripting
    def __getitem__(self, key):
        return getattr(self, key)




        