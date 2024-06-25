# multipliers = [1,2,3,4,5,6,7,8,9,10,11,12]
# multiplicant = 5
# for multiplier in multipliers:
#     print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

#     # this is not practical when we want to interate until 200 instead of 12 list
#     # this is where range come into rescue


# print (range(1,9)) # not printable.
# listno = range(1,9) # not printable.
# print(listno)# not printable.
# #range in an iterable object where we can use it in for loop with "in" operator
# # print function however dont understand to do iteration.
# #so it print as "range(1,12)"


# print(list(range(1,12)))
# range function doesnt inclu
# range is generating a list for numbers, the same way fruits before but it is string.
#WHEN YOU  WORK WITH A LIST, USE FOR LOOP

#--------------------------while loop start here // worst case scenario

#let say user give input 
# splt the digit as input and print them\
# let say user give 97509
# since case a: not got as a list, case b: dont know the initial digit number
# we gotta use while loop
#givenNumber = input("Give me the input number:")

givenNumber = 97409
while(givenNumber > 0):
    print("Modulas is:",givenNumber % 10)
    givenNumber //= 10
  

  # string are slow, not recommendable
# givenNumber2 = 287282
# strNo = str(givenNumber2)
# for digit in strNo:
#     print (digit)

fruits = ["apple" , 'orange', "mango", "banana", "grape", "rambutan", "durian", "mangosten"]

for fruit in fruits:
    print(fruit)

    if(fruit == "mango"): break
    else:
        print("this fruit is printed")