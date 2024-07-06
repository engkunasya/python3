#IS A RELATIONSHIP

class Student: #Parent

    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.proprwithoutparam = ""

#aLUMNI
#child
class Alumni(Student): #class that take aniother class as paramater
    
    def __init__(self, firstname, lastname, icnumber):
        # clalling the ini method statically
        # Student.__init__(self, firstname, lastname)
        #create parent object inside the child neoclass object
        #which wi9ll return the object of parent class
        super().__init__(firstname, lastname, icnumber)
        pass

    def __str__(self):
        return f"first name: {self.firstname}\nLastname: {self.lastname}\nICNumber: {self.icnumber}"

alumni = Alumni("Engku", "Nasya", "0192345")
print(alumni)

# When we create child object parent object is created automatically
# To initialize the parent object inside the child object,
# we are calling the __init__ method of the parent using super()
# from __init__ method of the child.