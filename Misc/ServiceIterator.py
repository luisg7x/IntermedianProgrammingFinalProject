class ServicesIterator:
    def __init__(self, hotel_services, id_services):
        self.hotel_services = hotel_services
        self.id_services = id_services
        self.generator = self.services_generator()

    def __iter__(self):
        #print("ITER")
        return self

    def __next__(self):
        #print("NEXT")
        return next(self.generator)

    def services_generator(self):
        #Iterate over each category in services
        for category in self.hotel_services:
            #Iterate over each service in the category
            for service in self.hotel_services[category]:
                #Check if the service ID is in the list of service IDs
                if service['id'] in self.id_services:
                    yield service
