# Dictionaries Remove
'''
# Removing items:
- pop(): The pop() method removes the item with the specified key name
- popitem(): The popitem() method removes the last inserted item
- clear(): the clear() method emties the dictionary:
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


# pop() method
myDictionariesData.pop("cool");
print("pop ()", myDictionariesData);

# popitem() method - it will remove the last item
myDictionariesData.popitem();
print("Pop item", myDictionariesData);


# clear() method - clear all the data
myDictionariesData.clear();
print("Clear method", myDictionariesData);