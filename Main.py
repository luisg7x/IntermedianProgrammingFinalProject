from Misc.JsonManager import JsonManager
from Misc.Login import Login
from Hotel import Hotel as hotel_class
from Staff import Staff as staff_class
from Services.restaurant import restaurant as restaurant_class
from Services.spa import spa as spa_class
import sys

print("-------------------")
print ("Welcome to Hotel Administrator Program")


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
                price_night = input("Enter price one night: ")
                restaurants = []
                spas = []
                    
                while True:
                    print("-------------------")
                    print("Registering a services for Hotel: " + name)
                    print("-------------------")
                    #print the options for the services
                    print("Type the number of the service that you want to add:")
                    print("1- Restaurant")
                    print("2- SPA")
                    print("3- Gym")
                    print("4- Events")
                    print("5- Exit & Create Hotel")
                    #Displaying options
                    service_value = int(input("Options 1,2,3,4,5: "))


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


                #creating a dictionary with the data and dividing it
                service = {"Restaurants": restaurants, "Spas": spas}
                hotel1 = hotel_class(name, address, number_of_rooms, price_night, service)
                JsonManager.save_as_json(hotel1, files_names[1])
                
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
        print("3- Edit or Delete hotel services")
        print("4- Edit hotel information")
        print("5- Exit")
        #Displaying options
        service_value = int(input("Options 1,2,3,4,5: "))
        
        if service_value == 3:
            print("Menu options:")
            print("1- Show all Restaurants")
            print("2- Edit specific restaurant by ID")
            option_value = int(input("Options 1,2,3,4,5: "))
            if option_value == 1:
                print(hotel1.services["Restaurants"])
            elif option_value == 2:
                by_id = input("Type any restaurand ID: ")
                restaurants = hotel1.services["Restaurants"]
                for rest in restaurants:
                    rest1 = restaurant_class(**rest)
                    if rest1.id == by_id:
                        print(rest)

            # Get the restaurants and spas from the data
            restaurants = hotel1.services["Restaurants"]
            spas = hotel1.services["Spas"]

            # Print the number of restaurants and spas
            print(f"There are {len(restaurants)} restaurants and {len(spas)} spas in the hotel.")

            # Print the name and rating of each restaurant
            for restaurant in restaurants:
                print(f"{restaurant['name']} has a rating of {restaurant['rating']}.")



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





