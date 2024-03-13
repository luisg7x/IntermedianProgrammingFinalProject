class Client:
    def __init__(self, id, name, email, is_currently_hosted, phone_number):
        self.id = id
        self.name = name
        self.email = email
        self.is_currently_hosted = is_currently_hosted
        self.phone_number = phone_number

    # Define a reprJSON method that returns a dict of the attributes
    def reprJSON(self):
        return self.__dict__
    
    # Implementing the __getitem__ method to allow subscripting
    def __getitem__(self, key):
        return getattr(self, key)

    

