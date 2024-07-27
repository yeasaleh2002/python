# Access set item
'''
- you can't access items in a set by referring to an index or a key.
- we can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
- check if the specific data is present in the set.
'''
# for in loop for access all the items
setData = {"Ab", "Ab", "Ac", "Ad", 1, 2, 3, 4, True, False};
for x in setData:
    print("item", x);

# specific items access
print("Ac is there", "Ac" in setData, 2 in setData, 5 in setData);