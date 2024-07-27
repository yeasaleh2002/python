# python open file
'''
* file handling:
- The key function for working with files in python is the 'open()' function.
- the 'open()' function takes two parameters; filiename, and mode.
- there are four different methods(modes) for opening a file:

-------------
'r' - Read - Default value. Opens a file for reading, error if the file does not exist.
'a' - Append - Opens a file for appending, creates the file if it does not exist.
'w' - Write - Opens a file for writing, creates the file if it does not exist.
'x' - Create - Creates the specified file, returns an error if the file exists.


-------------
'''


text = open("open.text", "r");

print(text.read())