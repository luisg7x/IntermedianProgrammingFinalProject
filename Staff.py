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
        
        