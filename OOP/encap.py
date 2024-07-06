class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
            self.__radius = radius
        
    


    def area(self):
        return 3.14 * self.__radius * self.__radius

    def circumference(self):
        return 2 * 3.14 * self.__radius

    def __str__(self):
        return f"Radius of this circle is {self.__radius}"

mycircle = Circle(20)
# print(mycircle)
# print (mycircle.getRadius())
# print(mycircle)
mycircle.__radius = 30 
print(mycircle.__radius)

#  do not use __ or _ to access property outside of the class
# read alias property
# done with encapsulation


