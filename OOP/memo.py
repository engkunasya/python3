class Student():
    def __str__(self):
        return "Student"

class Alumni(Student):
    pass
    def __str__(self):
        return "Alumni"

alumni = Alumni()
print(alumni)
   
#iterator object like enumerator, range, map, filter, do not override the method __str__
# however those classes are inherited from the default python class called object which has 
# the method __str__ which return the address location of the object
# that gets printed using the print function.


