# import random

# x = int(input("Enter value: "))
# x_new = x +1
# y = []

# while x != x_new :
#     x = random.randint(1,x_new)
#     y.append(x)
       

# random_try = len(y) #number or random try
# print('total try',random_try)
# print(y)
# ^^ TESTING RANDOM. ^^^^^^^^



import random

listKey = ["R","P", "S"]


while True:
    python = random.randint(0,2)
    user = input("Please enter R, P, or S for Rock, Paper or Scissors. Exit press E: ").upper()
    if user =="E":
        python = 3 #negating while of the python condition,
        break #then break. best practice 2 layers.

    elif user in listKey: 
        if python == 0:
            if user == "R":
                print("Random is Rock")
                print("You are on TIGHT")
                
            elif user == "P":
                print("Random is Rock")
                print("You are WINNING")

            elif user == "S":
                print("Random is Rock")
                print("You are LOSING")


        if python == 1:
            if user == "R":
                print("Random is Paper")
                print("You are on LOSING")
                

            elif user == "P":
                print("Random is Paper")
                print("You are on TIGHT")

            elif user == "S":
                print("Random is Paper")
                print("You are WINNING")



        if python == 2:
            if user == "R":
                print("Random is Scissors")
                print("You are on WINNING")
                

            elif user == "P":
                print("Random is Paper")
                print("You are on LOSING")

            elif user == "S":
                print("Random is Paper")
                print("You are LOSING")

    

 

