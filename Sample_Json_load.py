#未完成

#https://docs.python.org/3/library/json.html

import json

#load file from harddisk
with open('json_sample.txt') as json_file:
    json_data = json.load(json_file)
    print(type(json_file))
    print(type(json_data))                    #<class 'str'>
    #{'firstName': 'John', 'lastName': 'Smith', 'sex': 'male', 'age': 25, 'address': {'streetAddress': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'postalCode': '10021'}, 'phoneNumber': [{'type': 'home', 'number': '212 555-1234'}, {'type': 'fax', 'number': '646 555-4567'}]}
    print(json_data)
    for json_element in json_data:
        json_dict_name = json_element
        json_dict_value = json_element[json_dict_name]
        print(json_dic_name,':',json_dict_value)         #e.g. : firstName, lastName, sex, age
    json_file.close()