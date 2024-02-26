from Misc.JsonManager import JsonManager
from Staff import Staff
class Login:
    def is_valid(user, password, filename):

        data = JsonManager.load_from_json(filename)
        staff1 = Staff(**data)
        if staff1.user == user and staff1.password == password:
            return staff1
        else:
            return None


