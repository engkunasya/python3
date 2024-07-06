# #inheritance
# class A:
#     def __init__(self):
#         print("A class constructor")
#         def feature1(self):
#             print("feature 1 working")
#             def feature2(self):
#                 print("feature 2 working")
#                 class B(A):
#                     def __init__(self):
#                         print("B class constructor")
#                         def feature3(self):
#                             print("feature 3 working")
#                             def feature4(self):
#                                 print("feature 4 working")
#                                 class C(B):
#                                     def __init__(self):
#                                         print("C class constructor")

#has a relationship
class Passport:
    def __init__(self, country, passportnumber):
        self.country = country
        self.passportnumber = passportnumber
    def __str__(self):
        return f"Country: {self.country} PassportNo: {self.passportnumber}"

class Customer:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        self.passport = None

    def __str__(self):
        message = f"First Name: {self.firstname}"
        message += f"Last Name: {self.lastname}"
        message += f"IC Number: {self.icnumber}"
        if self.passport is not None:
            message += f"Passport: {self.passport}"
        return message
        

peter = Customer("Parker", "Peter")
passport = Passport("UK", "UK0908")
peter.passport = passport
print(peter)
print(peter.__dict__)  #equal to json.stringify(obj) // vice versa = json.parse

#HAS A RELATIONSHIP VS
#IS A RELATIONSHIP