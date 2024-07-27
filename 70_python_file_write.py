# python file write
'''
Write to an existing file
- to write to an existing file, you must add a parameter to the 'open()' function:
- 'a' - Append - will append to the end of the file.
- 'w' - write - will overwrite any existing content.
'''

# write = open('cool.html', 'w'); # for new file
write = open('cool.html', 'a'); # for existing file

write.write('<p>there should be cool data</p>\n<h1>cool</h1>\n');
write.write('<p>there should be cool data</p>\n<h1>cool</h1>\n');
write.write('<p>there should be cool data</p>\n<h1>cool</h1>\n');