from Service import service

class spa(service):
    def __init__(self, id,  name, schedule, price, capacity, availability, location):
        # call the parent class constructor to inherit the common attributes
        service.__init__(self, id, name, schedule, price, capacity, availability, location)

    # override the display_info method to include the new attributes
    def display_info(self):
        # call the parent class method to display the common information
        service.display_info(self)

