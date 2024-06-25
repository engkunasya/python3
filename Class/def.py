# function arent for solving problem
# like if for while.

# they are all used for organizing codes, wherever u copy and paste of block of code
# then u know ald it has to be fx.
# if the fx takes more than 1 value, than we must create more than 1 var.
#separator by comma

#parameter can be number, string and list
def sayHello(x):
    print(f"Hello World! Hello {x}")


x = "Nash"
sayHello(x)

def summation(a,b,c):
    d = a + b + c
    print (d)

summation(5,3,10)

def buyLunch(food, drink):
    price = [] #initialize empty list

   
    for i in food:
        if i == "nasi":
            price.append(1.20)
        if i == "ayam":
            price.append(5.00)
        if i == "sayur":
            price.append(0.50)

    for i in drink:
        if i == "coffee":
            price.append(2.00)
        if i == "milo":
            price.append(3)

    return price #only used within defined function.

print(buyLunch(["ayam"], ["milo"]))




#tupple is nothing but readonly list

