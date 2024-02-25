from Misc.JsonManager import JsonManager
from Misc.Login import Login
import Staff as st

print ("Welcome to Hotel Administrator Program")

#Flag to register whether the user is logged or not
logged = False

while not logged:

    print("Please enter your credentials to login")
    
    #Asking the loggin attributes to the user.
    username = input("Enter username: ") 
    password = input("Enter password: ")

    if Login.is_valid(username, password):
        #If valid, print a success message and break the loop
        print("Login successful!")
        break
    else:
        #If not valid, print a failure message and continue the loop
        print("Login failed. Please try again.")


# I need to create O PULL data like this from JSON: 
        service1 = Service(1, “Pizza Hut”, “10:00-22:00”, 15, True, 50, “Main Street”)
                           
                           
                           


print("Welcome "+ (st.Staff.) + "") #storeage the loggin?

if st.


