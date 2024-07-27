# Dictionaries Access

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

# Access spacific data
print(myDictionariesData["Name"])

# get method
newData = myDictionariesData.get("Name");
print("New data", newData)

#keys() - to get all the keys
print("Keys", myDictionariesData.keys()) # to get only parents keys

#values() - to get all the values including keys
print("Values", myDictionariesData.values());

