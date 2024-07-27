# python all oop method
'''
* python class method:
In object oriented programming, we use instance methods and class methods. Inside a class, we can define th efollowing three types of methods.

- Instance method: Used to access or modigy the object state. If we use instance variables insides a method, such methods are called instance methods.
  It must have a 'self' parameter to refer to the current object.
- Class method: Used to access or modify the class state. In method implementation, if we use only class variable, then such type of methods we should declare
  as a class method. The class method has a 'cls' parameter which refers to the class.
- Static method: It is a general utility method that performs a task in isolation. Inside this method, we don't use instance or class variable because theis
  static method doesn't take anhy parameters like 'self' and 'cls'.
'''

# instance method
class className:
    def InstanceMethod(self):
        print("hello instance method");

  # static method
    @staticmethod
    def StaticMethod():
        print("This is a static method");

#class method
    @classmethod
    def ClassMethod(cls):
        print("This is a class method");

varb1 = className();
varb1.InstanceMethod();
varb1.StaticMethod();

className.ClassMethod();