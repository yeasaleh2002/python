# python loops
# for loop vs while loop in python
# for loop: for loop is used when the number of iterations is already known.
# while loop: While loop is used when the number of iterations is already unknown.
# while loop syntax:
'''
initialValue = 1
while initialValue < conditionValue:
print(iniitialValue)
i = i+1; # increment or decrement
'''

# for loop - we can do it for only known data
data = [1, 2, 4, 5, 7, 8, 10, 23];
x = 1;
for x in data:
    print(x)


# while loop
i = 0;
while i < 19:
    print("item", i);
    i = i + 1;