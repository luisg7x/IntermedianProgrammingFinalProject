from Misc.JsonManager import JsonManager
from Misc.Login import Login
import Staff as staff
import Hotel as hotel
import Service as Service
import Services.Restaurant as restaurant
import Services.Spa as spa

import keyboard
import time

print ("Welcome to Hotel Administrator Program")

#Flag to register whether the user is logged or not
logged = False
#Storage staff after login check
staff1 = object
#services available to be added to the hotel
services = {
    1 : "RESTAURANT",
    2 : "SPA",
    3 : "GYM", 
    4 : "EVENTS"
}
#defining the secret key and time limit if that will be used if there is not user in the data base
secret_key = "g"
time_limit = "5"

while not logged:

    print("Please enter your credentials to login")
    
    #Asking the loggin attributes to the user.
    username = input("Enter username: ") 
    password = input("Enter password: ")

    staff1 = Login.is_valid(username, password)
    if staff1 is not None and staff1 != 1 or 2:
        #If valid, print a success message and break the loop
        print("Login successful!")
        break
    elif staff1 == 2:

        print(f"Press '{secret_key}' to see the secret menu within {time_limit} seconds.")
        # get the current time
        start_time = time.time()

        # create a loop to check the keyboard events
        while True:
            # check if the user presses the secret key
            if keyboard.is_pressed(secret_key):
                # print the secret menu
                print("Here is the secret menu:")
                print("1. Super pizza")
                print("2. Mega burger")
                print("3. Ultra fries")
                # break the loop
                break
            # check if the time limit is reached
            elif time.time() - start_time > time_limit:
                # print a message that the user ran out of time
                print("Sorry, you ran out of time.")
                # break the loop
                break
            # wait for a short time to avoid high CPU usage
            time.sleep(0.01)
    else:
        #If not valid, print a failure message and continue the loop
        print("Login failed. Please try again.")


                           
                           
                    
print("Welcome "+ (staff1.name) + "") 


try:
    data = JsonManager.load_from_json("Hotel.json")
    hotel1 = hotel(**data)
    print("Systems for Hotel: " + hotel1.name + "have been loaded succesfully")

    if data is None and staff1.role.upper() == "ADMIN":
        print("Enter the next data to create a New Hotel:")
        name = input("Enter name: ") 
        address = input("Enter address: ")
        number_of_rooms = input("Enter number of rooms: ") 
        price_night = input("Enter price one night: ")
        restaurants = []
        spas = []
        
        while True:
            print("Registering a services for Hotel: " + name)
            #print the options for the services
            print("Type the number of the service that you want to add:")
            print("1- Restaurant")
            print("2- SPA")
            print("3- Gym")
            print("4- Events")
            print("5- Exit")
            #Displaying options
            service_value = int(input("Options 1,2,3,4,5: "))


            #check if the user input is valid
            if service_value in services:

                id = input("Enter id: ") 
                name = input("Enter name: ")
                schedule = input("Enter schedule: ") 
                price = input("Enter price: ")
                availability = input("Enter price: ")
                capacity = input("Enter capacity: ")
                location = input("Enter location: ")

                if service_value == 1:
                    cuisine = input("Enter cuisine: ")
                    rating = input("Enter rating: ")
                    # create a restaurant object
                    restaurants = restaurant(id, name, schedule, price, availability, capacity, location, cuisine, rating)

                    # append the restaurant object to the list
                    restaurants.append(restaurant)

                elif service_value == 2:
                    # create a spa object
                    spas = spa(id, name, schedule, price, availability, capacity, location)

                    # append the spa object to the list
                    spas.append(spa)
                
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


        Service = [restaurants, spas]
        hotel1 = (name, address, number_of_rooms, price_night, Service)

        JsonManager.save_as_json(hotel1, "Hotel.json")


    
except:
    print("System could not find Hotel.json")





