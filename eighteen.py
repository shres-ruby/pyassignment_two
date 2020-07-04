# 18. Find a package in the Python standard library for dealing with JSON. Import the library module 
# and inspect the attributes of the module. Use the help function to learn more about how to use the 
# module. Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string. 
# Deserialize the JSON back into Python. 

import json

d = {
    'name' : 'Ruby', 
    'age' : 27
    }

j = json.dumps(d)
print(j)

dic = json.loads(j)
print(dic)