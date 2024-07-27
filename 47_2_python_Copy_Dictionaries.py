# copy a dictionaries
'''
there are 2 method:
- copy()
- dict()
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


# copy()
newData = myDictionariesData.copy();
print("copy", newData);


# dict()
newData2 = dict(myDictionariesData);
print("dict", newData2)
