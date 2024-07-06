# Polymorphism

class Gender:
    def __init__(self):
        pass
    def doCarryObject(self):
        pass

class Male(Gender):
    def __init__(self):
        pass
    def doCarryObject(self):
        print("Male can carry heavy objects")


class Female(Gender):
    def __init__(self):
        pass
    def doCarryObject(self):
        print("Female can carry light objects")


def getGender(name):
    if "Bin"in name:
        return Male()
    else:
        return Female()
    
gender = getGender("Nash Bin Net")
gender.doCarryObject()
print(type(gender))