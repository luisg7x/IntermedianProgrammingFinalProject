class Client:
    def __init__(self, id, name, email, phone_number, payment_method):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.payment_method = payment_method

    # define a method to display the service information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Payment Method: {self.payment_method}")

    

