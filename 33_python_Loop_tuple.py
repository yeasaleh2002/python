# Python Loop Tuple
tupleData = ("Ab", "Ac", "Ad");

# loop using normal for loop
for i in tupleData:
    print(i);

# loop tuple using range -- we will get the index of the tuple data
for x in range(len(tupleData)):
    print(x);
# we can access data using tuple index
print("Access tuple using index", tupleData[1]);


# while loop for tuple
newTupleData = tupleData;
i = 0;
while i < len(newTupleData):
    print("Index num", newTupleData[i]);
    i = i + 1 # increment