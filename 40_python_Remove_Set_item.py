# Remove Set item
'''
# Remove set item

remove(): - if there are no value, you want to remove, then it will return error
discard():  - if there are no value, you want to remove, then it will not return error
pop(): - it will remove one element from the sets but we don't know which items it will remove
clear(): - we can clear all the data

'''

setData = {"Ab", "Ab", "Ac", "Ad", 1, 2, 3, 4, True, False};
setData.remove("Ab");
print("Set data", setData);

# pop()
setData1 = {"Ab", "Ab", "Ac", "Ad"};
setData1.pop()
print("pop data", setData1)

# clear()
setData1.clear();
print("Clear data", setData1)
