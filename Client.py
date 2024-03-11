class Client:
    def __init__(self, id, name, email, number_nights, id_services, phone_number, payment_method, total):
        self.id = id
        self.name = name
        self.email = email
        self.number_nights = number_nights
        self.id_services = id_services
        self.phone_number = phone_number
        self.payment_method = payment_method
        self.total = total

    # Define a reprJSON method that returns a dict of the attributes
    def reprJSON(self):
        return self.__dict__
    
    # Implementing the __getitem__ method to allow subscripting
    def __getitem__(self, key):
        return getattr(self, key)

    

