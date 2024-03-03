from Misc.JsonManager import JsonManager
from Misc.Login import Login
from Hotel import Hotel as hotel_class
from Staff import Staff as staff_class
from Services.restaurant import restaurant as restaurant_class
from Services.spa import spa as spa_class
import sys

print("-------------------")
print ("Welcome to Hotel Administrator Program")

#SEE ROLES CONCRETE FUCTIONS
#OPTIMIZATION
#IMPLEMENT EXEPTIONS
#FIX Incorporar variables locales y globales.
# Incorporar métodos de cadena y librerías.
#  iteradores y generadores.
# reación y lectura de archivos en el código
#  3 excepciones

#Flag to register whether the user is logged or not
logged = False
#Storage staff after login check
staff1 = staff_class
# dictionary with the services available to be added to the hotel
services = {
    1 : "RESTAURANT",
    2 : "SPA",
    3 : "GYM", 
    4 : "EVENTS"
}
# tuple with the file names of every json
files_names = (
    "STAFF.json",
    "HOTEL.json",
    "CLIENT.json"
)

#defining the secret key and time limit if that will be used if there is not user in the data base
secret_key = "g"
time_limit = "5"


#REGISTERING ADMIN FOR FIRST TIME
#staff1 = staff("1-1111-1111", "Admin", "Admin", "Admin", "Admin")
#JsonManager.save_as_json(staff1, "Staff.json")
#print("saved")


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
        break
    else:
        #If not valid, print a failure message and continue the loop
        print("-------------------")
        print("Login failed. Please try again.")
        print("-------------------")

def save_hotel(hotel : hotel_class):
    JsonManager.save_as_json(hotel, files_names[1])
                                
def check_if_file_exist(filename):
    return JsonManager.check_if_file_exist(filename)

def load_hotel_file():
    data = JsonManager.load_from_json(files_names[1])
    hotel1 = hotel_class(**data)
    if hotel1 is None:
        sys.exit("ERROR: Hotel file is empty")
    else:
        print("Systems for Hotel: " + hotel1.name + " have been loaded succesfully")
        print("-------------------")
        return hotel1
    
def get_staff_id():
    if logged:
        return staff1.role.upper()
    else:
        sys.exit("Could find staff role")

def add_services(add_To_Exising : bool, hotel : hotel_class):
    if add_To_Exising:
        restaurants = hotel.services["Restaurants"]
        spas = hotel.services["Spas"]
    else: 
        restaurants = []
        spas = []
                    
    while True:
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

            id = input("Enter id: ") 
            name = input("Enter name: ")
            schedule = input("Enter schedule: ") 
            price = input("Enter price: ")
            availability = input("Enter availability: ")
            capacity = input("Enter capacity: ")
            location = input("Enter location: ")

            if service_value == 1:
                cuisine = input("Enter cuisine: ")
                rating = input("Enter rating: ")
                # create a restaurant object
                restaurant1 = restaurant_class(id, name, schedule, price, availability, capacity, location, cuisine, rating)

                # append the restaurant object to the list
                restaurants.append(restaurant1)

            elif service_value == 2:
                # create a spa object
                spa1 = spa_class(id, name, schedule, price, availability, capacity, location)

                # append the spa object to the list
                spas.append(spa1)
                            
            # ask the user if they want to add more services
            answer = input("Do you want to add more services? (y/n): ")

            # check if the user wants to exit the loop
            if answer.lower() == "n":
                break

        elif service_value == 5:
            # exit the loop
            break

        else:
            # print a message that the input is invalid
            print("Invalid option. Please enter a number between 1 and 5.")

    #creating a dictionary with the data and dividing it and return it
    return {"Restaurants": restaurants, "Spas": spas}

def show_create_hotel_menu():
    if get_staff_id == "ADMIN":

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

                
                service = add_services(False)
                hotel1 = hotel_class(name, address, number_of_rooms, available_rooms, price_night, service)
                save_hotel(hotel1)

                
                print("-------------------")
                print("The Hotel has been succesfully created")
                print("-------------------")
            else:
                sys.exit("End of execution, nothing to load")
    else:
        sys.exit("Please loggin with an admin account to create a Hotel")


def show_menu_hotel():
    hotel1 = load_hotel_file()
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
        service_value = int(input("Options 1,2,3,4,5: "))
        
        if service_value == 3:
            print("------------------------------------------------")
            print("Menu options:")
            print("1- Show all Restaurants")
            print("2- Add services")
            if len(hotel1.services["Restaurants"]) >= 1:
                print("3- Edit specific restaurant by ID")
                print("4- Delete specific restaurant by ID")
            option_value = int(input("Options 1,2,3,4,5: "))
            #Filtering option selected by the user
            if option_value == 1:
                print(hotel1.services["Restaurants"])
            elif option_value == 2:
                hotel1.services = add_services(True, hotel1)
                save_hotel(hotel1)
            elif option_value == 3 or 4:
                #asking for the id 
                print("------------------------------------------------")
                by_id = input("Type any Restaurant ID: ")
                #flag to exit the loop
                flag = True
                #looking which restaurant has the id typed by the user
                #dictionary in lists
                for index, rest in enumerate(hotel1.services["Restaurants"]):
                    rest1 = restaurant_class(**rest)
                    restaurant_dict = {}
                    #displaying options
                    if rest1.id == by_id:
                        #LOOP in case user wants to continue modifying
                        while flag:
                            #verifying delete option
                            if option_value == 4:
                                #deleteting element on the list by index
                                del hotel1.services["Restaurants"][index]
                                save_hotel(hotel1)
                                flag = False
                            #Continue with editing
                            else:
                                print("------------------------------------------------")
                                print("Which element would like to edit?")
                                # creating a dictionaty with the numbers option
                                # Counter for keys in restaurant_dict
                                counter = 1
                                # Iterate through items, and printing options
                                for key, value in rest1.__dict__.items():
                                    restaurant_dict[counter] = [key, value]
                                    print(f"{counter} - {key} : {value}")
                                    counter += 1

                                    
                                option = int(input(f"Type the option that you want to change (1-{len(restaurant_dict)}): "))
                                #looking for the option selected
                                if option in restaurant_dict:
                                    new_value = input(f"Type the new value for {option} - {restaurant_dict[option][0]} : {restaurant_dict[option][1]} -->")
                                    #Iterate bewtween every attribute on class restaurant
                                    #for attr in vars(rest1):
                                        #if attribute exist i'll be changed
                                    # if attr == restaurant_dict[option][0]:
                                    #     rest1.__setattr__(attr, new_value)
                                        
                                    #dictionary of services, get only the elements owned by key "restaurant" (a list of dictionaries or a list of many restaurants)
                                    #index = of the dictionary in the list.
                                    #restaurant_dict[option][0] = which attribute in the dictionary will be modified
                                    hotel1.services["Restaurants"][index][restaurant_dict[option][0]] = new_value

                                #IMPLEMENTS EXEPTION ON THAT FOR 
                                                
                                # ask the user if they want to add more services
                                answer = input("Would like to continue modifiying this restaurant? (y/n): ")

                                # check if the user wants to exit the loop
                                if answer.lower() == "n":
                                    save_hotel(hotel1)
                                    flag = False
                    
                    if flag is not True:
                        break
        elif service_value == 4:
            print("------------------------------------------------")
            print("Name: " + hotel1.name)
            print("Address: " + hotel1.address)
            print("Price Night: " + hotel1.price_night)
            print("Number of Rooms: " + hotel1.number_of_rooms)
            print("Available Rooms: " + hotel1.available_rooms)

        elif service_value == 5:
            print("------------------------------------------------")
            print("Select the option that you want to edit:")
            print("1 - Name: " + hotel1.name)
            print("2 - Address: " + hotel1.address)
            print("3 - Price Night: " + hotel1.price_night)
            print("4 - Number of Rooms: " + hotel1.number_of_rooms)
            print("5 - Available Rooms: " + hotel1.available_rooms)
            print("6 - Exit")

            option = int(input(f"Type the option that you want to change (1-5): "))
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
                

        elif option_value == 6:
            sys.exit("Program has been closed by the user")

            # Get the restaurants and spas from the data
            #restaurants = hotel1.services["Restaurants"]
            #spas = hotel1.services["Spas"]

            # Print the number of restaurants and spas
            #print(f"There are {len(restaurants)} restaurants and {len(spas)} spas in the hotel.")

            # Print the name and rating of each restaurant
            #for restaurant in restaurants:
            #    print(f"{restaurant['name']} has a rating of {restaurant['rating']}.")



def load_hotel_menu():
    if get_staff_id == "EMPLOYEE" or "ADMIN":
        if check_if_file_exist(files_names[1]):
            load_hotel_file()
            show_menu_hotel()
        else:
            show_create_hotel_menu()
            #recursivity?
            load_hotel_menu()
    else:
        sys.exit("Unathorized access")

            


print("Welcome "+ (staff1.name) + " role: " + get_staff_id())
print("-------------------")

load_hotel_menu()





