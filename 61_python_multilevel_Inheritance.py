# Multi Level inheritance
# its means data is forward parents to child1, child1 to child2 and child2 to child3 and same way to go for next

class parents():
    car= "cool";
    tk= "134141";
    home= "5";
class child1(parents):
    smartPhone = "Iphone";
    fan = "10pics";
class child2(child1):
    Ac = "Samsung";
    labtop = "Apple";
    Camera = "Canon";

class child3(child2):  # here we are sending all parents data for child using multiple inheritance
    webcam= "oneteck";
    desktop= "samsung";

access = child1();
access2 = child2();
access3 = child3();
print(access.car);
print(access2.fan);
print(access3.labtop);