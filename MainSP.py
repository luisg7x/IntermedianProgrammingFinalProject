from Misc.JsonManager import JsonManager
from Misc.Login import Login
from Misc.IdGenerator import IdGenerator
from Misc.ServiceIterator import ServicesIterator
from Hotel import Hotel as hotel_class
from Staff import Staff as staff_class
from Services.Restaurant import Restaurant as restaurant_class
from Services.Spa import Spa as spa_class
from Client import Client as client_class
from Invoice import Invoice as invoice_class
import sys
import os
import difflib
from datetime import datetime, timedelta


print( "****---------------------------------------------------*****")
print(" ")
print ("Bienvenido al programa administrador del Hotel.")

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
#Getting the current date
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

    print(" ")
    print("Por favor ingrese sus credenciales de acceso al programa.")
    print(" ")
    
    #Asking the loggin attributes to the user.
    username = input("Ingrese su usuario: ") 
    password = input("Ingrese su contraseña: ")

    staff1 = Login.is_valid(username, password, files_names[0])
    if staff1 is not None:
        #If valid, print a success message and break the loop
        print(" ")
        print("¡Ingreso exitoso!")
        print(" ")
        logged = True
        clear_console()
        break
    else:
        #If not valid, print a failure message and continue the loop
        print(" ")
        print("Lo sentimos ingreso fallido, por favor ingrese nuevamente sus credenciales")
        print(" ")

#Function to get the file name through a class name
def get_save_file_name(obj_class : object) -> str:
    class_name = obj_class.__name__
    #Looking up for similar words orbest match in a list of strings, n means returnthe top match, cufoff = set similarity threshold
    matches = difflib.get_close_matches(class_name.upper(), [file.upper() for file in files_names], n=1, cutoff=0.6)
    #returning the matching word
    return matches[0] if matches else None

#Function to save a json file.
def save_file_json(obj_class : object, file_name : str):
    JsonManager.save_as_json(obj_class, file_name)

#Function to check if any file exists                    
def check_if_file_exist(filename):
    return JsonManager.check_if_file_exist(filename)

#Function to load the json file.
def load_json_file(file_name):
    try:
        data = JsonManager.load_from_json(file_name)
        #check if the json file contains or has any data.
        if data is None:
            sys.exit("Error, el archivo del cliente se encuentra vacío")
        else:
            return data
    except Exception as e:
        print(f"A ocurrido un error: {e}")

#Function to return the staff role    
def get_staff_role():
    #check if is logged
    if logged:
        return staff1.role.upper()
    else:
        sys.exit("No se pudo encontar el rol del personal")

#Function to convert string date to system datetime
def parse_date(date_string : str):
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
        print(" ")
        print("Registrar servicios en el Hotel")
        print(" ")
        #print the options for the services
        print("Indique el número del servicio que desea agregar")
        print(" ")
        print("1- Restaurant")
        print("2- SPA")
        print("3- Exit & Create Hotel")
        print(" ")
        #Displaying options
        service_value = int(input("Opciones 1,2,3: "))


        #check if the user input is valid
        if service_value in services:
            id_gen = IdGenerator()
            name = input("Ingrese el nombre: ")
            schedule = input("Ingrese un horario: ") 
            price = input("Ingrese el precio: ")
            availability = input("Ingrese la disponibilidad: ")
            capacity = input("Ingrese la capacidad: ")
            location = input("Ingrese la ubicación: ")

            #Check if the option is 1
            if service_value == 1:
                id = id_gen.get_Id(restaurant_class, files_names[1])
                cuisine = input("Ingrese la cocina: ")
                rating = input("Ingrese la calificación: ")
                # create a restaurant object
                restaurant1 = restaurant_class(id, name, schedule, price, availability, capacity, location, cuisine, rating)

                # append the restaurant object to the list
                restaurants.append(restaurant1)

            #Check if the option is 2
            elif service_value == 2:
                id = id_gen.get_Id(spa_class, files_names[1])
                # create a spa object
                spa1 = spa_class(id, name, schedule, price, availability, availability, location)

                # append the spa object to the list
                spas.append(spa1)
                            
            # ask the user if they want to add more services
            answer = input("Le gustaría agregar más servicios? (y/n): ")

            # check if the user wants to exit the loop
            if answer.lower() == "n":
                break
        #Check if the option is 5
        elif service_value == 5:
            # exit the loop
            break

        else:
            # print a message that the input is invalid
            print("Opción inválida. Por favor ingrese un número entre 1 y 5")

    #creating a dictionary with the data that have been added and returning it
    return {"Restaurant": restaurants, "Spa": spas}

#Function to update available rooms in the hotel data
def update_available_rooms(hotel : hotel_class, is_new_reservation : bool):
    if is_new_reservation:
        #update rooms available
        hotel.available_rooms = str(int(hotel["available_rooms"]) - 1)
        #save hotel
        save_file_json(hotel, get_save_file_name(hotel_class))
        return
    
    #check if client and invoice .json files exist 
    if check_if_file_exist(get_save_file_name(client_class)) and check_if_file_exist(get_save_file_name(invoice_class)):
        client_list = load_json_file(get_save_file_name(client_class))[client_class.__name__]
        invoice_list = load_json_file(get_save_file_name(invoice_class))[invoice_class.__name__]

        # Loop, checking each invoice
        for invoice in invoice_list:
            departure_date = parse_date(invoice['departure_date'])
            if departure_date < current_date:
                id_client = invoice['id_client']
                # Loop up for the client that need to be modified
                for client in client_list:
                    if client['id'] == id_client:
                        if client['is_currently_hosted'] == True:
                            client['is_currently_hosted'] = False
                            #update rooms available
                            hotel.available_rooms = str(int(hotel["available_rooms"]) + 1)       

        #save client json
        save_file_json({"Client": client_list}, get_save_file_name(client_class))
        #save hotel
        save_file_json(hotel, get_save_file_name(hotel_class))

#Function to prompt for client information
def get_client_data():
    id = input("Ingrese el número de indentificación del cliente: ")
    name = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    phone_number = input("Ingrese el número telefónico del cliente: ")

    return client_class(id, name, email, True, phone_number)

#Fuction to promt for services and payment information
def get_invoice_data(client_id):
    id_gen = IdGenerator()
    id = id_gen.get_Id(invoice_class, files_names[3])
    number_nights = int(input("Ingrese el número de noches: "))
    id_services = input("Ingrese el identificacor de los servicios deseados (separados con coma)(sin espacios): ").split(',')
    payment_method = input("Ingrese el método de pago: ")
    departure_date = (current_date + timedelta(days=number_nights))
    return invoice_class(id, client_id, number_nights, id_services, current_date.strftime("%d/%m/%Y %H:%M:%S"), departure_date.strftime("%d/%m/%Y %H:%M:%S"), payment_method, 0)

#Function to calculate the total cost for the client
def calculate_total(invoice, hotel):
    #Create an instance of the ServicesIterator
    used_services = ServicesIterator(hotel['services'], invoice.id_services)
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
            print("No hay habitaciones disponibles")
            return
    except ValueError:
        print("Error en número de habitaciones disponibles, revise el archivo")
    
    clear_console()
    print(" ")
    print("Agregando un cliente")
    print(" ")

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
    if check_if_file_exist(get_save_file_name(client_class)) and check_if_file_exist(get_save_file_name(invoice_class)):
        client_list = load_json_file(get_save_file_name(client_class))[client_class.__name__]
        invoice_list = load_json_file(get_save_file_name(invoice_class))[invoice_class.__name__]

        #checks if user id already exists
        for diccionario in client_list:
            if diccionario['id'] == client.id:
                print("El número de indentificación ingresado ya existe, regresando al menú principal....")
                print(" ")
                return
    else:
        client_list = []
        invoice_list = []

    
    client_list.append(client)
    invoice_list.append(invoice)

    #Save client json
    save_file_json({client_class.__name__: client_list}, get_save_file_name(client_class))
    #Save invloice json
    save_file_json({invoice_class.__name__: invoice_list}, get_save_file_name(invoice_class))

    print("La reserva del cliente a sido creada exitosamente")
    print(" ")

#Function to display "add new hotel" options, therefore it will create a new hotel.
def show_create_hotel_menu():
    if get_staff_role == "ADMINISTRADOR":

            print("No hay ningún hotel creado, le gustaría registrar uno? y/n")
            option = input("Options: y/n -> ")
            print(" ")

            # checking if the user want to create a hotel
            if option.upper() == "Y":
                # Gathering the needed data to create a hotel
                print("Complete los siguientes datos para crear un Hotel:")
                name = input("Ingrese el nombre: ") 
                address = input("Ingrese la dirección: ")
                number_of_rooms = input("Ingrese el número total de habitaciones: ")
                available_rooms = input("Ingrese el número de habitaciones disponibles: ")
                price_night = input("Ingrese el precio por noche: ")

                #Calling add_services fuction, and marking it as new services for a new hotel
                service = add_services(False)
                #Assigning the attributes to the hotel class.
                hotel1 = hotel_class(name, address, number_of_rooms, available_rooms, price_night, service)
                #Calling save_hotel fuction to save and create hotel.json file
                save_file_json(hotel1, get_save_file_name(hotel_class))

                print(" ")
                print("***El hotel a sido creado de forma exitosa***")
                print(" ")
            else:
                sys.exit("Fin de la ejecución, nada más que agregar")
                print(" ")
    else:
        sys.exit("Por favor ingrese con credencial de administrador para crear un hotel")
        print(" ")

#Fuction to display and capture the option of the "Hotel main menu"
def show_menu_hotel():
    data = load_json_file(get_save_file_name(hotel_class))
    hotel1 = hotel_class(**data)
    #updating rooms
    update_available_rooms(hotel1, False)
    while True:
        print(" ")
        print("-*-*-*-*-*-*-*-> Bienvenido al Hotel " + hotel1.name, "<-*-*-*-*-*-*-*-*")
        print(" ")
        #print the options for the services
        print("Menú principal:")
        print(" ")
        print("1- Registrar un cliente nuevo")
        print("2- Editar información del cliente")
        print("3- Agregar, editar o borrar servicios del hotel")
        print("4- Mostrar información del hotel")
        print("5- Editar información del hotel")
        print("6- Salir del programa")
        #Displaying options
        service_value = int(input("Opciones 1,2,3,4,5,6: "))
        #options in the menu for edit and delete restaurant and spas
        options_edit_del = [3,4,7,8]

        #Checking if option is 1
        if service_value == 1:
            add_client(hotel1)
        #Checking if option is 2
        elif service_value == 2:
            
            if check_if_file_exist(get_save_file_name(client_class)):
                client_list = load_json_file(get_save_file_name(client_class))[client_class.__name__]
                clear_console()
                client_id = input("Cual cliente desea editar? Ingrese la identificación: ")
                #checks if user id already exists
                for index, value in enumerate(client_list):
                    if value['id'] == client_id:
                        #new dictionary that will create a new format to storage a number key for every item that will be printed
                        dict_menu_option = {}
                        #LOOP in case user wants to continue modifying
                        while True:
                            count = 1
                            # Iterate through items, and printing options
                            for key, value in client_list[index].items():
                                #storaring data in the "dict_menu_option" dictionary
                                dict_menu_option[count] = [key, value]
                                print(f"{count} - {key} : {value}")
                                count += 1
                            
                            #Ask the user for an option
                            option = int(input(f"Escriba la opción que desea editar (1-{len(dict_menu_option)}): "))

                            if option in dict_menu_option:
                                #asking the user for a value that will modify the previous one
                                new_value = input(f"Ingrese el nuevo valor {option} - {dict_menu_option[option][0]} : {dict_menu_option[option][1]} -->")
                                  
                                client_list[index][dict_menu_option[option][0]] = new_value
                                #calling "save_hotel". Saving hotel
                                save_file_json({client_class.__name__ : client_list}, get_save_file_name(client_class))
                            
                            # ask the user if they want to edit more services
                            answer = input("Desea continuar modificando la información de este usuario? (y/n): ")

                            # check if the user wants to exit the loop
                            if answer.lower() == "n":
                                break
                        
            else:
                print("NO hay ningún cliente registrado")
                print(" ")
        #Checking if option is 3
        elif service_value == 3:
            print("-----------------------------------------")
            print("          Menú de opciones:")
            print(" ")
            print("1- Mostrar todos los restaurantes")
            print("2- Agregar servicios")
            #checking if there is any restaurant, otherwise it will not print the options
            if len(hotel1.services[restaurant_class.__name__]) >= 1:
                print("3- Para editar información específica de un restaurante, ingrese ID")
                print("4- Para borrar un restaurante en específico, ingrese ID")

            print("6- Mostrar todos los SPA")
            #checking if there is any Spa, otherwise it will not print the options
            if len(hotel1.services[spa_class.__name__]) >= 1:
                print("7- Para editar una spa en específico, ingrese  ID")
                print("8- Para borrar un spa en esepecífico, ingrese ID")


            option_value = int(input("Opciones 1,2,3,4,5,6,7,8: "))

            #Filtering option selected by the user
            if (option_value == 1) or (option_value ==6):
                #printing every restaurant or spa
                print(hotel1.services[restaurant_class.__name__ if option_value == 1 else spa_class.__name__])
            elif option_value == 2:
                #calling add services fuction, sending 2 atributes, new services to a not new hotel, and current hotel information.
                hotel1.services = add_services(True, hotel1)
                save_file_json(hotel1, get_save_file_name(hotel_class))
            
            elif option_value in options_edit_del:
                #As there is only 2 services, we are checking if the option selected is related with.
                is_restaurant = True if (option_value == 3) or (option_value == 4) else False
                #asking for the id 
                print(" ")
                by_id = input(f"Digite cualquier {'Restaurant ID' if is_restaurant else 'Spa ID'}: ")
                #flag to exit the loop
                flag = True
                #looking which restaurant has the id typed by the user, !!those ternarial comparations need to be improved!!!.
                for index, value in enumerate(hotel1.services[restaurant_class.__name__ if is_restaurant else spa_class.__name__]):
                    #new dictionary that will create a new format to storage a number key for every item that will be printed
                    class_dict = {}
                    #displaying options
                    if hotel1.services[restaurant_class.__name__ if is_restaurant else spa_class.__name__][index]["id"] == by_id:
                        #LOOP in case user wants to continue modifying
                        while flag:
                            #verifying delete option
                            if (option_value == 4) or (option_value == 8):
                                #deleting element on the list by index
                                del hotel1.services[restaurant_class.__name__ if is_restaurant else spa_class.__name__][index]
                                save_file_json(hotel1, get_save_file_name(hotel_class))
                                flag = False
                            #Continue with editing
                            else:
                                print("***                          ***")
                                print("Que elemento le gustaría editar?")
                                # creating a dictionaty with the numbers option
                                # Counter for keys in class_dict
                                counter = 1
                                # Iterate through items, and printing options
                                for key, value in hotel1.services[restaurant_class.__name__ if is_restaurant else spa_class.__name__][index].items():
                                    #storaring data in the "class_dict" dictionary
                                    class_dict[counter] = [key, value]
                                    print(f"{counter} - {key} : {value}")
                                    counter += 1

                                #Ask the user for an option
                                option = int(input(f"Digite la opción que le gustaría cambiar (1-{len(class_dict)}): "))
                                #looking for the option selected
                                if option in class_dict:
                                    #asking the user for a value that will modify the previous one
                                    new_value = input(f"Ingrese un nuevo valor para la opción {option} - {class_dict[option][0]} : {class_dict[option][1]} -->")
                                  
                                    #Iterate bewtween every attribute on class restaurant
                                    #for attr in vars(rest1):
                                        #if attribute exist i'll be changed
                                    # if attr == restaurant_dict[option][0]:
                                    #     rest1.__setattr__(attr, new_value)
                                        
                                    #dictionary of services, get only the elements owned by key "restaurant" (a list of dictionaries or a list of many restaurants)
                                    #index = of the dictionary in the list.
                                    #restaurant_dict[option][0] = which attribute in the dictionary will be modified

                                    #aplying modification in the hotel
                                    hotel1.services[restaurant_class.__name__ if is_restaurant else spa_class.__name__][index][class_dict[option][0]] = new_value
                                    #calling "save_hotel". Saving hotel
                                    save_file_json(hotel1, get_save_file_name(hotel_class))
                                                
                                # ask the user if they want to edit more services
                                answer = input("Desea continuar la modificación del servicio? (y/n): ")

                                # check if the user wants to exit the loop
                                if answer.lower() == "n":
                                    flag = False
                    
                    #check is if the loop has to be broken
                    if flag is not True:
                        break
                
        #checks if the value is 4 and print the options
        elif service_value == 4:
            print("------------------------------------------------")
            print("Nombre: " + hotel1.name)
            print("Dirección: " + hotel1.address)
            print("Precio por noche: " + hotel1.price_night)
            print("Número total de habitaciones: " + hotel1.number_of_rooms)
            print("Habitaciones disponibles: " + hotel1.available_rooms)
            print(" ")

        #checks if the value is 5 and print the options
        elif service_value == 5:
            print("------------------------------------------------")
            print("Seleccione la opción que desea editar:")
            print(" ")
            print("1 - Nombre: " + hotel1.name)
            print("2 - Dirección: " + hotel1.address)
            print("3 - Precio por noche: " + hotel1.price_night)
            print("4 - Número total de habitaciones: " + hotel1.number_of_rooms)
            print("5 - Número de habitaciones disponibles: " + hotel1.available_rooms)
            print("6 - Salir")

            #ask the user for an option
            option = int(input(f"Ingrese la opción que desea editar (1-5): "))
            #every if check which one is the one that has been selected and request new data to create to edit the hotel.
            if option == 1:
                hotel1.name = input("Ingrese el nuevo nombre: ")
            elif option == 2:
                hotel1.address = input("Ingrese la nueva dirección: ")
            elif option == 3:
                hotel1.price_night = input("Ingrese el nuevo precio por noche: ")
            elif option == 4:
                hotel1.number_of_rooms = input("Ingrese la nueva cantidad de habitaciones: ")
            elif option == 5:
                hotel1.available_rooms = input("Ingrese la nueva cantidad de habitaciones disponibles: ")
            elif option == 6:
                continue
            save_file_json(hotel1, get_save_file_name(hotel_class))
                
        elif service_value == 6:
            sys.exit("El programa a sido cerrado exitosamente por el usuario")

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
        if check_if_file_exist(get_save_file_name(hotel_class)):
            load_json_file(get_save_file_name(hotel_class))
            show_menu_hotel()
        else:
            #dispoaly menu to create hotel
            show_create_hotel_menu()
            #recursivity?
            load_hotel_menu()
    else:
        sys.exit("Acceso no autorizado")

#Print staff info
print("Bienvenido "+ staff1.name + " role: " + get_staff_role())
print(" ")

#calls the main fuction
load_hotel_menu()





