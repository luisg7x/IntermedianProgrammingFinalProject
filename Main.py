from Misc.JsonManager import JsonManager
from Misc.Login import Login
from Misc.IdGenerator import IdGenerator
from Hotel import Hotel as hotel_class
from Staff import Staff as staff_class
from Services.Restaurant import Restaurant as restaurant_class
from Services.Spa import Spa as spa_class
from Client import Client as client_class
from Invoice import Invoice as invoice_class
import sys
import os
from datetime import datetime, timedelta


print("-------------------")
print ("Welcome to Hotel Administrator Program")

#---------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!--------------------------------------------

#Check/ To implement:
# ROLES FUCTIONS ?
# OPTIMIZATION 
# Check if services that the client will use, actually exist (adding client) id services can be printed to make it easer to type in
# Edit client function is missing
# check email, id format, add $symbol on every "price" related field, check if ids already exist when adding a new one 

#Missing from PDF: 
# Incorporar métodos de cadena y librerías !! DONE ????
# Creación y lectura de archivos en el código. Can be implemented by creating logs and reading them and show them on the console if the user is an admin

#---------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!--------------------------------------------

#Flag to register whether the user is logged or not
logged = False
#Storage staff after login check
staff1 = staff_class
#Dictionary with the services available to be added to the hotel
services = {
    1 : "RESTAURANT",
    2 : "SPA"
}
#Tuple with the name of each json file  
files_names = (
    "STAFF.json",
    "HOTEL.json",
    "CLIENT.json",
    "INVOICE.json"
)
#etting the current date
current_date = datetime.now()

#REGISTERING ADMIN FOR FIRST TIME (!!!ONLY RUN IF THERE IS NOT AN ADMIN USER YET!!!)
#staff1 = staff("1-1111-1111", "Admin", "Admin", "Admin", "Admin")
#JsonManager.save_as_json(staff1, "Staff.json")
#print("saved")

#Function to clean console
def clear_console():
    #'cls' for Windows, 'clear' for Unix/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

#Infite while loop til the person get authenticated
while not logged:

    print("-------------------")
    print("Please enter your credentials to login")
    print("-------------------")
    
    #Asking the loggin attributes to the user.
    username = input("Enter username: ") 
    password = input("Enter password: ")

    staff1 = Login.is_valid(username, password, files_names[0])
    if staff1 is not None:
        #If valid, print a success message and break the loop
        print("-------------------")
        print("Login successful!")
        print("-------------------")
        logged = True
        clear_console()
        break
    else:
        #If not valid, print a failure message and continue the loop
        print("-------------------")
        print("Login failed. Please try again.")
        print("-------------------")

#Function to save the hotel to a json file.
def save_hotel(hotel : hotel_class):
    JsonManager.save_as_json(hotel, files_names[1])

def save_client(client : client_class):
    JsonManager.save_as_json(client, files_names[2])

def save_invoice(invoice : invoice_class):
    JsonManager.save_as_json(invoice, files_names[3])

#Function to check if any file exists                    
def check_if_file_exist(filename):
    return JsonManager.check_if_file_exist(filename)

#Function to load the json hotel file.
def load_hotel_file():
    try:
        data = JsonManager.load_from_json(files_names[1])
        data1 = hotel_class(**data)
        #check if the json file contains or has any data.
        if data1 is None:
            sys.exit("ERROR: Hotel file is empty")
        else:
            print("Systems for Hotel: " + data1.name + " have been loaded succesfully")
            print("-------------------")
            return data1
    except Exception as e:
        print(f"An error occurred: {e}")

#Function to load the json client file.
def load_client_file():
    try:
        data = JsonManager.load_from_json(files_names[2])
        #check if the json file contains or has any data.
        if data is None:
            sys.exit("ERROR: Client file is empty")
        else:
            return data
    except Exception as e:
        print(f"An error occurred: {e}")

#Function to load the json invoice file.
def load_invoice_file():
    try:
        data = JsonManager.load_from_json(files_names[3])
        #check if the json file contains or has any data.
        if data is None:
            sys.exit("ERROR: Invoice file is empty")
        else:
            return data
    except Exception as e:
        print(f"An error occurred: {e}")

#Function to return the staff role    
def get_staff_role():
    #check if is logged
    if logged:
        return staff1.role.upper()
    else:
        sys.exit("Could not find staff role")

#Function to convert string date to system datetime
def parse_date(date_string):
    return datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")

#Function to add new services to a new hotel that is being created or add new servcies to an already existing hotel
def add_services(add_To_Exising : bool, hotel : hotel_class):
    #check if the method is being called add services to an already existing hotel.
    if add_To_Exising:
        restaurants = hotel.services["Restaurant"]
        spas = hotel.services["Spa"]
    else: 
        restaurants = []
        spas = []

    #Infinity loop to show the "add services menu"              
    while True:
        clear_console()
        print("-------------------")
        print("Registering a services for Hotel")
        print("-------------------")
        #print the options for the services
        print("Type the number of the service that you want to add:")
        print("1- Restaurant")
        print("2- SPA")
        print("3- Exit & Create Hotel")
        #Displaying options
        service_value = int(input("Options 1,2,3: "))


        #check if the user input is valid
        if service_value in services:
            id_gen = IdGenerator()
            name = input("Enter name: ")
            schedule = input("Enter schedule: ") 
            price = input("Enter price: ")
            availability = input("Enter availability: ")
            capacity = input("Enter capacity: ")
            location = input("Enter location: ")

            #Check if the option is 1
            if service_value == 1:
                id = id_gen.get_Id(restaurant_class, files_names[1])
                cuisine = input("Enter cuisine: ")
                rating = input("Enter rating: ")
                # create a restaurant object
                restaurant1 = restaurant_class(id, name, schedule, price, availability, capacity, location, cuisine, rating)

                # append the restaurant object to the list
                restaurants.append(restaurant1)

            #Check if the option is 2
            elif service_value == 2:
                id = id_gen.get_Id(spa_class, files_names[1])
                # create a spa object
                spa1 = spa_class(id, name, schedule, price, availability, capacity, location)

                # append the spa object to the list
                spas.append(spa1)
                            
            # ask the user if they want to add more services
            answer = input("Do you want to add more services? (y/n): ")

            # check if the user wants to exit the loop
            if answer.lower() == "n":
                break
        #Check if the option is 5
        elif service_value == 5:
            # exit the loop
            break

        else:
            # print a message that the input is invalid
            print("Invalid option. Please enter a number between 1 and 5.")

    #creating a dictionary with the data that have been added and returning it
    return {"Restaurant": restaurants, "Spa": spas}

#Function to update available rooms in the hotel data
def update_available_rooms(hotel : hotel_class, is_new_reservation : bool):
    if is_new_reservation:
        #update rooms available
        hotel.available_rooms = str(int(hotel["available_rooms"]) - 1)
        #save hotel
        save_hotel(hotel)
        return
    
    #check if client and invoice .json files exist 
    if check_if_file_exist(files_names[2]) and check_if_file_exist(files_names[3]):
        data_a = load_client_file()
        data_b = load_invoice_file()
        client_list = data_a[client_class.__name__]
        invoice_list = data_b[invoice_class.__name__]

        # Loop, checking each invoice
        for invoice in invoice_list:
            departure_date = parse_date(invoice['departure_date'])
            if departure_date > current_date:
                id_client = invoice['id_client']
                # Loop up for the client that need to be modified
                for client in client_list:
                    if client['id'] == id_client:
                        client['is_currently_hosted'] = False
                        #update rooms available
                        hotel.available_rooms = str(int(hotel["available_rooms"]) + 1)       

        #save client json
        save_client({"Client": client_list})
        #save hotel
        save_hotel(hotel)

#Function to prompt for client information
def get_client_data():
    id = input("Enter client ID: ")
    name = input("Enter client name: ")
    email = input("Enter client email: ")
    phone_number = input("Enter client phone number: ")

    return client_class(id, name, email, True, phone_number)

#Fuction to promt for services and payment information
def get_invoice_data(client_id):
    id_gen = IdGenerator()
    id = id_gen.get_Id(invoice_class, files_names[3])
    number_nights = int(input("Enter number of nights: "))
    id_services = input("Enter service IDs (comma-separated)(no space): ").split(',')
    payment_method = input("Enter payment method: ")
    departure_date = (current_date + timedelta(days=number_nights))
    return invoice_class(id, client_id, number_nights, id_services, current_date.strftime("%d/%m/%Y %H:%M:%S"), departure_date.strftime("%d/%m/%Y %H:%M:%S"), payment_method, 0)

#Fuction that uses a Generator to iterate over services in 'Restaurants' and 'Spas'
def services_used(hotel_services, id_services):
    #Iterate over each category in services
    for category in hotel_services:
        #Iterate over each service in the category
        for service in hotel_services[category]:
            #Check if the service ID is in the list of service IDs
            if service['id'] in id_services:
                yield service

#Function to calculate the total cost for the client
def calculate_total(invoice, hotel):
    #Create a generator for the client's used services
    used_services = services_used(hotel['services'], invoice.id_services)
    #Use the service_generator to iterate over all services and string methods
    total = sum(float(service['price'].strip('$')) for service in used_services)
    #Add the price per night, and using string methods
    total += float(hotel["price_night"].strip("$")) * invoice.number_nights
    return total

#Function to add client information and calculate total cost
def add_client(hotel: hotel_class):
    #Checks if there is any available room 
    try:
        if int(hotel["available_rooms"]) <= 0:
            print("There is not any available room")
            return
    except ValueError:
        print("Error on number of rooms available, check file")
    
    clear_console()
    print("-------------------")
    print("Adding a client")
    print("-------------------")

    #Call "get_client_data" function
    client = get_client_data()

    #Call "get_invoice_data " function
    invoice = get_invoice_data(client.id)

    #Calculate total and updates it
    invoice.total = calculate_total(invoice, hotel)

    #Update hotel data 
    update_available_rooms(hotel, True)

    client_list = None
    invoice_list = None

    #check if client and invoice .json files exist 
    if check_if_file_exist(files_names[2]) and check_if_file_exist(files_names[3]):
        data_a = load_client_file()
        data_b = load_invoice_file()
        client_list = data_a[client_class.__name__]
        invoice_list = data_b[invoice_class.__name__]
    else:
        client_list = []
        invoice_list = []
    
    client_list.append(client)
    invoice_list.append(invoice)

    #Save client json
    save_client({client_class.__name__: client_list})
    #Save invloice json
    save_invoice({invoice_class.__name__: invoice_list})

#Function to display "add new hotel" options, therefore it will create a new hotel.
def show_create_hotel_menu():
    if get_staff_role == "ADMIN":

            print("There is not any Hotel registered, would like to register one? y/n")
            option = input("Options: y/n -> ")
            print("-------------------")

            # checking if the user want to create a hotel
            if option.upper() == "Y":
                # Gathering the needed data to create a hotel
                print("Enter the next data to create a New Hotel:")
                name = input("Enter name: ") 
                address = input("Enter address: ")
                number_of_rooms = input("Enter number of rooms: ")
                available_rooms = input("Enter number of available rooms: ")
                price_night = input("Enter price one night: ")

                #Calling add_services fuction, and marking it as new services for a new hotel
                service = add_services(False)
                #Assigning the attributes to the hotel class.
                hotel1 = hotel_class(name, address, number_of_rooms, available_rooms, price_night, service)
                #Calling save_hotel fuction to save and create hotel.json file
                save_hotel(hotel1)

                
                print("-------------------")
                print("The Hotel has been succesfully created")
                print("-------------------")
            else:
                sys.exit("End of execution, nothing to load")
    else:
        sys.exit("Please loggin with an admin account to create a Hotel")

#Fuction to display and capture the option of the "Hotel main menu"
def show_menu_hotel():
    hotel1 = load_hotel_file()
    #updating rooms
    update_available_rooms(hotel1, False)
    while True:
        print("-------------------")
        print("-*-*-*-*-*-*-*-> Hotel: " + hotel1.name)
        print("-------------------")
        #print the options for the services
        print("Menu options:")
        print("1- Register new client")
        print("2- Edit client information")
        print("3- Add, Edit or Delete hotel services")
        print("4- Show hotel information")
        print("5- Edit hotel information")
        print("6- Exit program")
        #Displaying options
        service_value = int(input("Options 1,2,3,4,5,6: "))
        #options in the menu for edit and delete restaurant and spas
        options_edit_del = [3,4,7,8]

        #Checking if option is 1
        if service_value == 1:
            add_client(hotel1)
        #Checking if the option is 3
        if service_value == 3:
            print("------------------------------------------------")
            print("Menu options:")
            print("1- Show all Restaurants")
            print("2- Add services")
            #checking if there is any restaurant, otherwise it will not print the options
            if len(hotel1.services[restaurant_class.__name__]) >= 1:
                print("3- Edit specific restaurant by ID")
                print("4- Delete specific restaurant by ID")

            print("6- Show all Spa")
            #checking if there is any Spa, otherwise it will not print the options
            if len(hotel1.services[spa_class.__name__]) >= 1:
                print("7- Edit specific Spa by ID")
                print("8- Delete specific Spa by ID")

            #!!!!!!!!!!!!!!!!!!! IT NEEDS TO BE MODIFIED BECAUSE NOT EVERY OPTION WILL BE PRINTED!!!!!!!!!!!!!!!!!!!!!!!!!
            option_value = int(input("Options 1,2,3,4,5,6,7,8: "))

            #Filtering option selected by the user
            if (option_value == 1) or (option_value ==6):
                #printing every restaurant or spa
                print(hotel1.services[restaurant_class.__name__ if option_value == 1 else spa_class.__name__])
            elif option_value == 2:
                #calling add services fuction, sending 2 atributes, new services to a not new hotel, and current hotel information.
                hotel1.services = add_services(True, hotel1)
                save_hotel(hotel1)

            
            elif option_value in options_edit_del:
                #As there is only 2 services, we are checking if the option selected is related with.
                is_restaurant = True if (option_value == 3) or (option_value == 4) else False
                #asking for the id 
                print("------------------------------------------------")
                by_id = input(f"Type any {"Restaurant ID" if is_restaurant else "Spa ID"}: ")
                #flag to exit the loop
                flag = True
                #looking which restaurant has the id typed by the user, !!those ternarial comparations need to be improved!!!.
                for index, value in enumerate(hotel1.services[restaurant_class.__name__ if option_value == 1 else spa_class.__name__]):
                    #new dictionary that will create a new format to storage a number key for every item that will be printed
                    class_dict = {}
                    #displaying options
                    if hotel1.services[restaurant_class.__name__ if option_value == 1 else spa_class.__name__][index]["id"] == by_id:
                        #LOOP in case user wants to continue modifying
                        while flag:
                            #verifying delete option
                            if (option_value == 4) or (option_value == 8):
                                #deleting element on the list by index
                                del hotel1.services[restaurant_class.__name__ if option_value == 1 else spa_class.__name__][index]
                                save_hotel(hotel1)
                                flag = False
                            #Continue with editing
                            else:
                                print("------------------------------------------------")
                                print("Which element would like to edit?")
                                # creating a dictionaty with the numbers option
                                # Counter for keys in class_dict
                                counter = 1
                                # Iterate through items, and printing options
                                for key, value in hotel1.services[restaurant_class.__name__ if option_value == 1 else spa_class.__name__][index].items():
                                    #storaring data in the "class_dict" dictionary
                                    class_dict[counter] = [key, value]
                                    print(f"{counter} - {key} : {value}")
                                    counter += 1

                                #Ask the user for an option
                                option = int(input(f"Type the option that you want to change (1-{len(class_dict)}): "))
                                #looking for the option selected
                                if option in class_dict:
                                    #asking the user for a value that will modify the previous one
                                    new_value = input(f"Type the new value for {option} - {class_dict[option][0]} : {class_dict[option][1]} -->")
                                  
                                    #Iterate bewtween every attribute on class restaurant
                                    #for attr in vars(rest1):
                                        #if attribute exist i'll be changed
                                    # if attr == restaurant_dict[option][0]:
                                    #     rest1.__setattr__(attr, new_value)
                                        
                                    #dictionary of services, get only the elements owned by key "restaurant" (a list of dictionaries or a list of many restaurants)
                                    #index = of the dictionary in the list.
                                    #restaurant_dict[option][0] = which attribute in the dictionary will be modified

                                    #aplying modification in the hotel
                                    hotel1.services[restaurant_class.__name__ if option_value == 1 else spa_class.__name__][index][class_dict[option][0]] = new_value
                                    #calling "save_hotel". Saving hotel
                                    save_hotel(hotel1)
                                                
                                # ask the user if they want to add more services
                                answer = input("Would like to continue modifiying this service? (y/n): ")

                                # check if the user wants to exit the loop
                                if answer.lower() == "n":
                                    flag = False
                    
                    #check is if the loop has to be broken
                    if flag is not True:
                        break
                
        #checks if the value is 4 and print the options
        elif service_value == 4:
            print("------------------------------------------------")
            print("Name: " + hotel1.name)
            print("Address: " + hotel1.address)
            print("Price Night: " + hotel1.price_night)
            print("Number of Rooms: " + hotel1.number_of_rooms)
            print("Available Rooms: " + hotel1.available_rooms)

        #checks if the value is 5 and print the options
        elif service_value == 5:
            print("------------------------------------------------")
            print("Select the option that you want to edit:")
            print("1 - Name: " + hotel1.name)
            print("2 - Address: " + hotel1.address)
            print("3 - Price Night: " + hotel1.price_night)
            print("4 - Number of Rooms: " + hotel1.number_of_rooms)
            print("5 - Available Rooms: " + hotel1.available_rooms)
            print("6 - Exit")

            #ask the user for an option
            option = int(input(f"Type the option that you want to change (1-5): "))
            #every if check which one is the one that has been selected and request new data to create to edit the hotel.
            if option == 1:
                hotel1.name = input("Enter the new name: ")
                save_hotel(hotel1)
            elif option == 2:
                hotel1.address = input("Enter the new Address: ")
                save_hotel(hotel1)
            elif option == 3:
                hotel1.price_night = input("Enter the new Price Night: ")
                save_hotel(hotel1)
            elif option == 4:
                hotel1.number_of_rooms = input("Enter the new Number of Rooms: ")
                save_hotel(hotel1)
            elif option == 5:
                hotel1.available_rooms = input("Enter the new Available Rooms: ")
                save_hotel(hotel1)
            elif option == 6:
                continue
                
        elif service_value == 6:
            sys.exit("Program has been closed by the user")

            # Get the restaurants and spas from the data
            #restaurants = hotel1.services["Restaurants"]
            #spas = hotel1.services["Spas"]

            # Print the number of restaurants and spas
            #print(f"There are {len(restaurants)} restaurants and {len(spas)} spas in the hotel.")

            # Print the name and rating of each restaurant
            #for restaurant in restaurants:
            #    print(f"{restaurant['name']} has a rating of {restaurant['rating']}.")

#Main fuction, to check roles and load the menu
def load_hotel_menu():
    #checks staff role
    if get_staff_role == "EMPLOYEE" or "ADMIN":
        #check if there is a hotel already registered and loads menus
        if check_if_file_exist(files_names[1]):
            load_hotel_file()
            show_menu_hotel()
        else:
            #dispoaly menu to create hotel
            show_create_hotel_menu()
            #recursivity?
            load_hotel_menu()
    else:
        sys.exit("Unathorized access")

#Print staff info
print("Welcome "+ (staff1.name) + " role: " + get_staff_role())
print("-------------------")

#calls the main fuction
load_hotel_menu()





