class Client:
    def __init__(self, id, name, email, is_Hosted, phone_number, payment_method):
        self.id = id
        self.name = name
        self.email = email
        self.is_Hosted = is_Hosted
        self.phone_number = phone_number
        self.payment_method = payment_method

    # define a method to display the service information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Email: {self.email}")
        print(f"is Hosted: {self.is_Hosted}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Payment Method: {self.payment_method}")

    # Generator function to yield services used by the client
    def services_used(self, hotel_services):
        for service_category, services in hotel_services.items():
            for service in services:
                yield service_category, service
    

