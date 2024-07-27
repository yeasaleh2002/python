# Add set item
'''
# Add Items
- once a set is created, you can't change its items, but you can add new items
- To add one item to a set use the add() method.

# Update items
- To add items from another set into the current set, use the update() method.

# Add any iterable
- The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries, etc)

'''

# Add items
setData = {"Ab", "Ab", "Ac", "Ad", 1, 2, 3, 4, True, False};
setData.add("Cool");
print(setData);

# Update items - Add elements from setData to setData1;
setData1 = {"Co", "Ao", "Bo"};
setData.update(setData1);
print("Set data ", setData)


# Add any iterable - add elements of a list to at set:
setData2 = {"Co", "Ao", "Bo"};
setData3 = ["Ci", "A9", "Bi"];
setData2.update(setData3);
print("Set data 2", setData2)

