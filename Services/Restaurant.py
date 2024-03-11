from Service import Service as service

class Restaurant(service):
    def __init__(self, id, name, schedule, price, capacity, availability, location, cuisine, rating):
        # call the parent class constructor to inherit the common attributes
        service.__init__(self, id, name, schedule, price, capacity, availability, location)
        # add new attributes specific to the restaurant class
        self.cuisine = cuisine
        self.rating = rating

    # Define a reprJSON method that returns a dict of the attributes
    def reprJSON(self):
        return self.__dict__

    # override the display_info method to include the new attributes
    def display_info(self):
        # call the parent class method to display the common information
        service.display_info(self)
        # display the new information
        print(f"Cuisine: {self.cuisine}")
        print(f"Rating: {self.rating}")


