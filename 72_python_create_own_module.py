# python create own module

# non parameterized constructor
class parentInfo:
    def coolguys(self, name, age):
        print(f'{name} is a cool guy whos age is {age}');

person1 = parentInfo();

person1.coolguys("matha nosto", 32);
person1.coolguys("patafati", 23);


# parameterized constructor
class coolGuysInfo:
    def __init__(self, name, age ):
        print(f'{name} is a cool man and he is {age}');

p1 = coolGuysInfo("mouse", 12);