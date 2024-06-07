"""
Serialization is the process of converting a Python object into a byte stream (a sequence of bytes) that can be easily stored in a file or
sent over a network.
Deserialization is the reverse process of converting the byte stream back into a Python object.

These processes are essential for saving the state of an object to a file or sending complex data structures over a network.

Python's pickle Module
Python provides the pickle module for serialization and deserialization of Python objects. Here’s how you can use it:

Serialization Example with pickle
Serialize (pickle) a Python object to a file:

"""
import pickle

# Define a Python object (e.g., a dictionary)
data = {'name': 'Shweta', 'age': 30, 'city': 'Wonderland'}

# Open a file in binary write mode
with open('data.pickle', 'wb') as file:
    # Serialize the object and write it to the file
    pickle.dump(data, file)

print("Data serialized and written to file.")

"""
Deserialization Example with pickle
Deserialize (unpickle) a Python object from a file:
"""

import pickle

# Open the file in binary read mode
with open('data.pickle', 'rb') as file:
    # Deserialize the object from the file
    data = pickle.load(file)

print("Data deserialized from file.")
print(data)

"""
JSON Serialization and Deserialization
For interoperability with other programming languages, you might use JSON (JavaScript Object Notation) instead of Python-specific pickle.
Python's json module can be used for this purpose.

JSON Serialization Example
Serialize (convert) a Python object to a JSON string:

"""

import json

# Define a Python object (e.g., a dictionary)
data = {'name': 'shweta', 'age': 30, 'city': 'Wonderland'}

# Serialize the object to a JSON string
json_string = json.dumps(data)

print("Data serialized to JSON string.")
print(json_string)

# Serialize the object and write it to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

print("Data serialized and written to JSON file.")

"""
JSON Deserialization Example
Deserialize (convert) a JSON string to a Python object:
"""

import json

# Deserialize the JSON string to a Python object
data = json.loads(json_string)

print("Data deserialized from JSON string.")
print(data)

# Deserialize the object from a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

print("Data deserialized from JSON file.")
print(data)








