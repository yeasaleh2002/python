# multiple inheritance in python
# here child can only acesss to use parents data but parents can't access child data.

class parents1():
    car= "cool";
    tk= "134141";
    home= "5";
class parents2():
    smartPhone = "Iphone";
    fan = "10pics";
class parents3():
    Ac = "Samsung";
    labtop = "Apple";
    Camera = "Canon";

class child(parents1, parents2, parents3):  # here we are sending all parents data for child using multiple inheritance
    webcam= "oneteck";
    desktop= "samsung";

access = child();
print(access.tk);
print(access.smartPhone);
print(access.Ac)