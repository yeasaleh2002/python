# Python tuple method
'''
* Tuple Methods:
- python has two build in methods that  you can use on tuples

# count(): Returns the number of times a specified value occurs in a tuple
- The count() method returns the number of times a specified value appears in the tuple.
- Syntax: tuple.count(value)


# index(): Searches the tuple for a specified value and returns the position of where it was found.
- The index() method finds the first occurrrence of the specified value
- The index() method raises an exception if the value is not found.
- syntax: tuple.index(value)

'''

# count
tuple = (1, 2, 3, 4, 6, 5, 6, 6, 9);
print(tuple.count(6))

# index
print(tuple.index(9))
