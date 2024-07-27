'''
What is a python matrix?
=> A matrix in python is a two dimensional array having a secific number of rows and columns.
- example:
matList = [
[1, 4, 6, 7, 9, 2], [2, 4, 1, 6, 7, 6]
];
- There are two list inside the list, its called matrix or nested list.
'''

matList = [
[1, 4, 6, 7, 9, 2], [2, 4, 1, 6, 7, 6], 10
];

getElement = matList[0][2]; # we can use 2 dimential array or matrix like that. we can acess it by this way.
print(getElement)