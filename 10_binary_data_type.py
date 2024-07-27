#binary datatype

#byte
# byte range is 0 to 255;
'''
for image processing we can use byte. and but is immuteable. so we can assign value on it after assignment.
we can use byte() function for converting as a byte data.
'''
byteData = [23, 42, 41, 42, 42, 12];
print(byteData)
print(type(bytes(byteData)))
print((bytes(byteData)))


#byte array type
'''
byte array type is muteable. we can assign value after assign.
it's range is 0 to 255.
'''

# * they both are converted list or this kind of things to byte.
byteData1 = [23, 42, 41, 42, 42, 12];
print(byteData1)
print(type(bytearray(byteData)))
print((bytearray(byteData)))

newData = bytearray(byteData1);
newData[3] = 32;
print("new data", newData, newData[3]);