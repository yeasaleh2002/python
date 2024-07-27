# python iterator
'''
Python Iterators:
- An iterator is an object that contains a countable number of values.
- An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
- Technically, in python an iterator is an object which implemnets the iterator protocol, which consist of the methods _iter_() and _next_().

# Iterator vs Iterable
- Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
- All these objects have a iter() method which is used to get an iterator:

'''

list = [1, 2, 3, 4, 5]; # this is iterable - which is a list, tuple and etc

for i in list:
    print(i); # the each of value is iterate value

# iterator - must need to use iter()

cool = iter(list); # convert iterator
print("cool", cool.__next__()) # by using __next__ we can get each of iterate value for each print

# we can resolve the __next__ long text to next() only.
print("Next", next(cool))
print("Next 2", next(cool))

