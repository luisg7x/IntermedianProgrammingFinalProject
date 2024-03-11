class Staff:
    def __init__(self, id, name, role, user, password):
        self.id = id
        self.name = name
        self.role = role
        self.user = user
        self.password = password

    # Define a reprJSON method that returns a dict of the attributes
    def reprJSON(self):
        return self.__dict__
    
    # Implementing the __getitem__ method to allow subscripting
    def __getitem__(self, key):
        return getattr(self, key)
        
        