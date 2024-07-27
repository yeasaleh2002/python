#python add items
'''
1. Append Items - To add an item to the end of the list, use the append() method:
2. Insert Items - To insert a list item at a specified index, use the insert() method.
3. Extend List - To append elements from another list to the current list, use the extend() method. The elements will be added to the end of the list.
4.Add Any Iterable - The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
'''

# 1. Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# 2. Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange"); # here must need to give index first and comma, and then value
print(thislist)

# 3. Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# 4.Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
