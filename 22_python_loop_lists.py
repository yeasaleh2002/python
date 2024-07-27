# python loop list
# --- Loop Through a List ---
# for loop you must need to use colon(:) after the loop. otherwise loop will not work in the python.

# --- For in Loop ---
# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# --- Loop Through the Index Numbers ---
#You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i);
  print(thislist[i]);

#output: The iterable created in the example above is [0, 1, 2].


# --- Using a While Loop ---
'''
- You can loop through the list items by using a while loop.
- Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
- Remember to increase the index by 1 after each iteration.
'''

# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0  #inital values
while i < len(thislist):
  print(thislist[i])
  i = i + 2 #condition


