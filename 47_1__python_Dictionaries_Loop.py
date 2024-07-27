# python dictionaries loop
'''

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
    "cool": True
}

# to get all the parent keys
for x in myDictionariesData:
    print("keys", x);

# add values() after the dict name
for x in myDictionariesData.values():
    print("values", x);

# keys(): we can use the keys() method to return the keys of a dictionary
for x in myDictionariesData.keys():
    print("values", x);

# items(): loop through both keys and values, by using the items() method:
for x, y in myDictionariesData.items():
    print("keys and values", x, y);
