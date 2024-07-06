#method nare nothing but function inside a class.
#method is a function inside a class

class calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def add(self):
        return self.x+self.y
    
mycalculator = calculator(10,20)
print(mycalculator.add())

#There is a class which has many methods 
#but got no properties.
#why methods take self as a parameter? because
# we want to access the properties




# there are called class method.
# these type of method are attached to class not object
class Utility:
    def addition (x,y):
        return x + y
    def subtraction (x,y):
        return x - y
    
print(Utility.addition(2,3))

#this can be easily done using a module.
#we can create a module and import it.

#decorator tbc
# done with class method and class variable


