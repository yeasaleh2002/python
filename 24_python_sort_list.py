#python sort list
'''
- List objects have a sort() method that will sort the list alphanumerically, ascending by sort()
- if we want we can descending it by using -- reverse = True ---
- we can do it by customize cort function
- We can do sorting by case insensitive
- we can do it by reverse().

'''


# ascending example
number = [3, 5, 1, 4, 4, 2, 5, 112, 12, 12];
name = ['kuddos', 'nus', 'asman', 'jomin'];
number.sort();
name.sort();

print("Number sort", number);
print("name", name);

# reverse
name.sort(reverse=True) #for descending
