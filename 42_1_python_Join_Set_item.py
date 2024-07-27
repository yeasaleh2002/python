# join set item
'''
# join two sets
- there are several ways to join two or more sets in python
- we can use the union() method that returns a new set containing all items from the both sets
- The update() method that inserts all the items form one set into another

'''
setData1 = {"Ab", "Ab", "Ac", "Ad"};
setData2 = {"Ae", "Af", "Ag", "Ah"};

# union() - the union() method returns a new set with all items form both sets:
setData3 = setData1.union(setData2);
print("set data 3", setData3 )

# update()
setData2.update(setData1);
print("Set data 2", setData2)
