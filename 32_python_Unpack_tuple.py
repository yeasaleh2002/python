# Python Unpack tuple
'''
Packing: When we create a tuple, we normally assign values to it. This is called 'packing' a tuple:

Unpacking: In python, we are also allowed to extract the values back into variables. This is called 'unpacking'.

'''

# Destructure method for unpacking - mean based on it serial we can add variable name and we can easily access it
tupleData = ("Ab", "Ac", "Ad");
(a, c, d) = tupleData;
print(d);

# Astrick (*) sign - we can unpack tuple using * sign. if we use * means(ex: (*any_name, ) ) it will destructrue all the values in one veriable. If we add more options there its means it will access rest of data expect it another data position. (ex: (*a, b)) - here if you have 5 data in your tuple. the b will return the last index data and "*a" will return first all the tuple data. Must need to use comma after a unpacking


(*a, ) = tupleData;
print("App", a[1]);