def calculatePrincipal(principle, period, rate=6):
    interest = (principle * period * rate) / 100
    return interest

# parameter
print(calculatePrincipal(10,20))


# named argument
print(calculatePrincipal(principle=33 , period = 45))


#variable length argument
# the number of arguments which we pass vary
#caller can pass value as list


def findTotal (givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total += givenNumber
    return total


print(findTotal([10,20,30]))


#second demo
def listSixLetterFruits(*fruits):
    for fruit in fruits:
        if len(fruit) == 6 : print(fruit)
        # print(fruit)
    print(type(fruits)) #check the type

listSixLetterFruits("apple,""orange", "mango", "banana", "durian", "grapes")

