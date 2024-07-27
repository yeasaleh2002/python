# Python Dictionaries
'''
# Dictionary:
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- Dictionaries are written with curly brackets, and have keys and values. (like a json in javascript)
- For getting single element by keys: dictionariesData[keyvalue]
- if we need to get more nested data then we can increage the squre bracket([]) - dictionariesData[keyValues][AnotherKey]

'''

myDictionariesData = {
    "Name": "Kuddos",
    "Kuddos": {
        "Age": 18,
        "Class": "Bsc",
        "Addess": "Rajbari",
        "Major": "CSE",
        "Dept": "Bsc in CSE",
        "ID": "01212",
        "DateOfBirth": "14-12-2002",
        "University": "City University, Bangladesh"
        },
    "NASA": {
        "Age": 19,
        "Class": "Bsc",
        "Addess": "Rajbari pangsha",
        "Major": "CSE",
        "Dept": "Bsc in CSE",
        "ID": "01213",
        "DateOfBirth": "12 - 12 - 2002",
        "University": "City University, Bangladesh"
    },

}

# calling single data using key
print(myDictionariesData["NASA"])

# more nested
print(myDictionariesData["NASA"]["ID"])