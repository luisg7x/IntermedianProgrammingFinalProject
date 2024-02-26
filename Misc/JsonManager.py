import json 

class JsonManager:

    # define a method to save an object as a JSON file
    def save_as_json(self, obj, filename):
        # open a file with the given name in write mode
        with open(filename, "w") as f:
            # use the json module to dump the object as a JSON string
            self.json.dump(obj.__dict__, f, indent=4)

    # define a method to load an object from a JSON file
    def load_from_json(self, filename):
        # open a file with the given name in read mode
        with open(filename, "r") as f:
            # use the json module to load the JSON string as an object
            return self.json.load(f)
