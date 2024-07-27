# list comprehension
'''
What is list comprehension in Python?
=>
List comprehension is an easy to read, compact, and elegant way of creating a list
from any existing iterable object. Basically, it's a simpler way to create a new
list from the values in a list you already have. It is generally a single line of
code enclosed in square brackets.


* syntax -
newlist = [expression for item in iterable if condition == True]

- List comprehensions start and end with opening and closing square brackets, [].
- Then comes the expression or operation you'd like to perform and carry out on each value inside the current iterable. The results of these calculations enter the new list.
- The expression is followed by a for clause.
- variable is a temporary name you want to use for each item in the current list that is going through the iteration.
- The in keyword is used to loop over the iterable.
- iterable can be any Python object, such as a list, tuple, string and so on.
- From the iteration that was performed and the calculations that took place on each item during the iteration, new values were created which are saved to a variable, in this case new_list. The old list (or other object) will remain unchanged.
- There can be an optional if statement and additional for clause.


- The return value is a new list, leaving the old list unchanged.
- The condition is like a filter that only accepts the items that valuate to True.

'''


# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# With list comprehension you can do all that with only one line of code:
# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".


# The condition is optional and can be omitted:
# With no if statement:

newlist = [x for x in fruits]

# --- Iterable ---
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

# Same example, but with a condition:
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]


# --- Expression ---
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

# You can set the outcome to whatever you like:
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".


# question: make a array all values square using list compresion
value = [3, 4, 5 ,10]

square = [i * i for i in value];
print("square", square);