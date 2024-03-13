import json
import os.path

# Define a ComplexEncoder class that inherits from json.JSONEncoder
class ComplexEncoder(json.JSONEncoder):
    # Override the default method
    def default(self, obj):
        # Check if the object has a reprJSON method and call it
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        # Otherwise, use the default encoding behavior
        else:
            return json.JSONEncoder.default(self, obj)


class JsonManager:

    # define a method to save an object as a JSON file
    def save_as_json(obj, filename):
        try:
            # open a file with the given name in write mode
            with open(filename, "w") as f:
                # use the json module to dump the object as a JSON string
                # Serialize the hotel object using the ComplexEncoder
                json.dump(obj, f, cls=ComplexEncoder, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")

    # define a method to load an object from a JSON file
    def load_from_json(filename):
        # try to open the file in read mode
        try:
            with open(filename, "r") as f:
                # load the data from the file
                return json.load(f)
        # catch the FileNotFoundError exception
        except FileNotFoundError:
            # print a message that the file does not exist
            print(f"File {filename} does not exist.")
        except Exception as e:
            print(f"Could not load the file.")

    # define a method to check whether the file exist
    def check_if_file_exist(filename):
        #Check if file exist
        if os.path.exists(filename):
            return True
        else:
           return False
        
