class Student:
  
    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        print(firstname,lastname,icnumber)
        

    
    def attendClass(self):
        print("Object is attending class")

    def doProject(self, projectName):
        print(f"Onject started doing the project: {projectName}")
      
    
    def attendExam (self, exam):
        grade = "A"
        return f"Object has attended the exam call {exam} and attains the score {grade}"
    
    def info(self):
        print(f"firstname:", self.firstname)
        print(f"lastname:", self.lastname)
        print(f"icnumber:", self.icnumber)

    

zul = Student("zul", "akmal", 92029292)
zul.attendClass()
zul.doProject("ebox")
print(zul.attendExam("python 104"))
zul.info()

#assign value to object property directly as dictionary
zul.address = { "No": "15 jalan tar",
               "Street": 'Street2',
               "country": "malaysia"
                 }

# __str__



    ## conclusion: same as javascript where we have expressjs
    #const express = express()
    #route = express.route("/", (req, res) => {})

    # balik tengok how to mpass dictionary to property of the object created
    #by class consturctor called student.  
    