from Misc.JsonManager import JsonManager
from Staff import Staff
class Login:
    #Check if the user exits
    def is_valid(user, password, filename):
        #Loads the json file
        data = JsonManager.load_from_json(filename)
        #Loads the data (dictionaty type) into staff (class) parameters
        staff1 = Staff(**data)
        if staff1.user == user and staff1.password == password:
            return staff1
        else:
            return None


