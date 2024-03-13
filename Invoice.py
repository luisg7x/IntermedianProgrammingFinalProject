class Invoice:
    def __init__(self, id, id_client, number_nights, id_services, issue_date, departure_date, payment_method, total):
        self.id = id
        self.id_client =id_client
        self.number_nights = number_nights
        self.id_services = id_services
        self.issue_date = issue_date
        self.departure_date = departure_date
        self.payment_method = payment_method
        self.total = total

    # Define a reprJSON method that returns a dict of the attributes
    def reprJSON(self):
        return self.__dict__
    
    # Implementing the __getitem__ method to allow subscripting
    def __getitem__(self, key):
        return getattr(self, key)
    

