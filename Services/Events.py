from Service import service

class Evets(service):
    def __init__(self, id, name, schedule, price, capacity, availability, location, subject):
        # call the parent class constructor to inherit the common attributes
        service.__init__(self, id, name, schedule, price, capacity, location, availability)
        # add new attributes specific to the restaurant class
        self.subject = subject

    # override the display_info method to include the new attributes
    def display_info(self):
        # call the parent class method to display the common information
        service.display_info(self)
        # display the new information
        print(f"location: {self.location}")
        print(f"subject: {self.subject}")
