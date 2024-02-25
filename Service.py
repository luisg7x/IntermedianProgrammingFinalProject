class Service:
    def __init__(self, id, name, schedule, price, availability, capacity, location):
        self.id = id
        self.name = name
        self.schedule = schedule
        self.price = price
        self.availability = availability
        self.capacity = capacity
        self.location = location

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Schedule: {self.schedule}")
        print(f"Price: {self.price}")
        print(f"Capacity: {self.capacity}")
        print(f"Availability: {self.availability}")
        print(f"Location: {self.location}")



        