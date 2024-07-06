class Student:
    #in python we cant declaRE VARIABLE/PROPERTY WITHOUT VAR
    #but in python we can declare variable without var USING CONSTRUCTOR
    #constructor is a function which is called when object is created
    #constructor is a function which is called when object is created
    #init double underscore
    # def __init__(self):
    #method is nothing but function inside a class
    # self is a reference variable which is used to access the properties of the class
    #first parameter of the method is very special
    #value of first param is handled by python itself
    #that param is usually call self
    def __init__(self):
        print("object is created")

    #this is our first method
    #remember method need to have at least 1 param
    def attendClass(self):
        print("Object is attending class")

    def doProject(self, projectName):
        print(f"Onject started doing the project: {projectName}")
        #this is our second method, no need to assign argument to self paramater, so we consider 2nd paramater
    
    def attendExam (self, exam):
        grade = "A"
        return f"Object has attended the exam call {exam} and attains the score {grade}"
    







zul = Student()
zul.attendClass()
zul.doProject("ebox")
print(zul.attendExam("python 104"))

    ## conclusion: same as javascript where we have expressjs
    #const express = express()
    #route = express.route("/", (req, res) => {})
    