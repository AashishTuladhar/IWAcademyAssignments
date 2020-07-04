# Find a package in the Python standard library for dealing with JSON. Import the library module and inspect the attributes of the module. 
# Use the help function to learn more about how to use the module. 
# Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string. Deserialize the JSON back into python.

import json

print(help(json))                              

jsonString = json.dumps({'Name':'Aashish','Age':24})
dictionaryData = json.loads(jsonString)

print(type(dictionaryData))