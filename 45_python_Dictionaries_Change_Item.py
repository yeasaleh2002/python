# Doctomaroes change items
'''
# Change Dictionary Items
- We can change the value of a specific item by referring to its key name

# Update dictionary - update()
- The update() method will update the dictionary with the items from the given argument. (thisDict["Year"] = 2012)
- The argument must be a dictionary, or an iterable object with key: value pairs. (thisDict.update({"Year": 2000}))

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

# change dictionaries
myDictionariesData["Name"] = "NEW NAME";
print("MY dict", myDictionariesData)

# update() - must need to use curly bracket - {}
myDictionariesData.update({"cool": {
        "Age": 14,
        "Class": "Bsc in ECE",
}})
print("Update", myDictionariesData)