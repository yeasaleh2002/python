# python update tuple
'''
* Once a tuple is created, you can't change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, changes the list, and convert the list back into a tuple.

-- you need to follow few of step for updating tuple ---

-- # Add Items ---
Since tuples are immutaable, they do not have a build in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it backinto a tuple.
2. Add tuple to a tuple: You are allowed to add tuples to tuples, so if you want to add one ite, (or many), create a new tuple with the item(s), and add it to the existing tuple.

'''

tupleData = ("Ab", "Ac", "Ad");
tupleDataConvertedlist = list(tupleData);
tupleDataConvertedlist.append("Ae"); # Add a item in the list
tupleDataConvertedlist[1] = "AC";
tupleDataConvertedlist_To_Tuple = tuple(tupleDataConvertedlist);
print("tupleDataConvertedlist_To_Tuple", tupleDataConvertedlist_To_Tuple);