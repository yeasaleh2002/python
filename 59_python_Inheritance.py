# python inheritance
'''
Interitance :
- Interitance allows us to define a class that inherite all the methods and properties from another class
- Parent class: parent class is the class being inherited from, also called base class
- Child class: child class is the class that inherits from another class, also called derived class

'''

class dad():
    car= "cool";
    tk= "134141";
    home= "5";

class uncle(dad):  # here we are sending dad data for uncle using inherit
    study= "no";
    job= "yes";

access = uncle();
print(access.tk);

