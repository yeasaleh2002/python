'''
The three types of sequences in Python are lists, tuples, and (strings/range).
- Lists are mutable and defined by square brackets([]),
- tuples are immutable and enclosed in parentheses(()),
- strings are a sequence of characters enclosed in single or double quotes(""/ '').
- Python range is a function that returns a sequence of numbers. By default, range returns a sequence that begins at 0 and increments in steps of 1. The range function only works with integers. Other data types like float numbers cannot be used.
'''

#list type (its look line an array)
listData = ["Kutta mizan", "Atim Akbor", "Dancer Shah Alom", "Body Shohel"];
print("List data & it's type", listData, type(listData));

# tuple type
tupleData = ("Kutta mizan", "Atim Akbor", "Dancer Shah Alom", "Body Shohel", "Labu Comisoner");
print("Tuple data & it's type", tupleData, type(tupleData));

# range type
rangeValue = 23;
print("range values", range(23), type(range(rangeValue)));

for i in range(rangeValue):
    print(i)