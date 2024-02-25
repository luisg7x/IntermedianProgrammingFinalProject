from Service import service

class restaurant(service):
    def __init__(self, id, name, schedule, price, capacity, availability, location, cuisine, rating):
        # call the parent class constructor to inherit the common attributes
        service.__init__(self, id, name, schedule, price, capacity, availability, location)
        # add new attributes specific to the restaurant class
        self.cuisine = cuisine
        self.rating = rating

    # override the display_info method to include the new attributes
    def display_info(self):
        # call the parent class method to display the common information
        service.display_info(self)
        # display the new information
        print(f"Cuisine: {self.cuisine}")
        print(f"Rating: {self.rating}")


