from Misc.JsonManager import JsonManager
from Misc.Login import Login
from Hotel import Hotel as hotel
from Staff import Staff as staff
from Services.restaurant import restaurant 
from Services.spa import spa
import sys

print("-------------------")
print ("Welcome to Hotel Administrator Program")


#Flag to register whether the user is logged or not
logged = False
#Storage staff after login check
staff1 = staff
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
        break
    else:
        #If not valid, print a failure message and continue the loop
        print("-------------------")
        print("Login failed. Please try again.")
        print("-------------------")


                           
                                    
print("Welcome "+ (staff1.name) + " role: " + (staff1.role))
print("-------------------")


    
if JsonManager.check_if_file_exist(files_names[1]):
    data = JsonManager.load_from_json("Hotel.json")
    hotel1 = hotel(**data)
    print("Systems for Hotel: " + hotel1.name + "have been loaded succesfully")
    print("-------------------")
    
else:
    if staff1.role.upper() == "ADMIN":

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
                        restaurant1 = restaurant(id, name, schedule, price, availability, capacity, location, cuisine, rating)

                        # append the restaurant object to the list
                        restaurants.append(restaurant1)

                    elif service_value == 2:
                        # create a spa object
                        spa1 = spa(id, name, schedule, price, availability, capacity, location)

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
            hotel1 = hotel(name, address, number_of_rooms, price_night, service)
            JsonManager.save_as_json(hotel1, files_names[1])
            
            print("-------------------")
            print("The Hotel has been succesfully created")
            print("-------------------")
        else:
            sys.exit("End of execution")
    else:
        print("Please loggin with an admin account to create a Hotel")





