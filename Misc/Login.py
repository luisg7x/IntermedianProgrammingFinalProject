from Misc.JsonManager import JsonManager
import Staff as staff
class Login:
    def is_valid(username, password):
        
        try:
            data = JsonManager.load_from_json("Staff.json")
            staff1 = staff(**data)
            if staff1.username == username and staff1.password == password:
                return staff1
            elif staff1 is not None:
                return 1
            else:
                return 2
        except:
            print("System could not find Staff.json")

