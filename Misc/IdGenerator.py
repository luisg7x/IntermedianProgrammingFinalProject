from Misc.JsonManager import JsonManager

class IdGenerator:
    def __increment_id(self, id_str: str) -> str:
        #Split the ID into the prefix and the number
        prefix = id_str.rstrip('0123456789')
        num_part = id_str[len(prefix):]
        
        #Increment the number part
        new_num_part = str(int(num_part) + 1).zfill(len(num_part))
        
        #Combine them back together
        return f"{prefix}{new_num_part}"
    
    def __find_largest_id(self, class_name: str,file_name: str) -> str:
        #Load the JSON data
     
        data = JsonManager.load_from_json(file_name)

        #Initialize a list to store all the IDs
        ids: list[str] = []

        if data is None:
            ids.append(self.__create_zero_id(class_name))
        else:
            #Initialize a list to store all the IDs
            ids: list[str] = []
            
            #Check if 'services' key is in the JSON data
            if 'services' in data:
                # Extract IDs from 'Restaurant' and 'Spa' services
                for service_type in [class_name]:
                    if service_type in data['services']:
                        for service in data['services'][service_type]:
                            ids.append(service['id'])
            elif class_name in data:
                for value in data[class_name]:
                    ids.append(value['id'])

            if len(ids) < 1:
                ids.append(self.__create_zero_id(class_name))
        
        #Find the largest ID by sorting the list of IDs
        largest_id = sorted(ids, reverse=True)[0] if ids else None
        
        return largest_id
    
    def __create_zero_id(self, class_name: object) -> str:
        #Extracting the first, middle and last letter
        new_id = class_name[0] + class_name[len(class_name) // 2] + class_name[-1]
        #Adding the code number 
        new_id = new_id.upper() + "-000"
        return new_id

    def get_Id(self, class_to_gen: object, file_name: str) -> str:
        #Extracting class name
        class_name = class_to_gen.__name__
        #Check if file exist
        if not JsonManager.check_if_file_exist(file_name):
            return self.__create_zero_id(class_name)
        
        largest_id = self.__find_largest_id(class_name, file_name)
        return self.__increment_id(largest_id)
        




    
