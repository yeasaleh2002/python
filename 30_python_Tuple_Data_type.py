# Python tuple data type and Access
'''
* tuple is a datatype of python
- tuple are used to store multiple items in a single variable
- A tuple is a collection which is ordered and unchangeable/immuteable.
- Tuples are written with round brackets ().
-
# Access tuples
- if we can to access any element from tuple we can use it same as list (tuples[2])
# Tupes negative indexing :
- Negative indexing means start form the end. for example (-1 refers to the last items, -2 refers to the second last items - items access (tupes[-1]))
# Range of index
- We can specifiy a range of indexes by specifying where to start and where to end the range.
- when specifying a range, the return value will be a new tuple with the specified items. (ex: tuples[2:4])
- Important: (firt index is for starting and the last values means its previous index)
- Must we need to use the squre bracket ([])
-

'''

newTuples = ("Cool", "Hot", "Average", "Non ice", "ice", "Rain");
print(type(newTuples));
print("Access", newTuples[1])

# Negative Index
print("Negaive indexing", newTuples[-1], newTuples[-3])

# Ranges of indexes
print("Range of index", newTuples[0: 3]) #here 1st values mean the starting index but the second value means the index of before its value
