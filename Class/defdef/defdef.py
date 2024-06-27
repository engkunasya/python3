def authenticate(username,password):
    
    
    def pricewithSI(price):
        calculateSI = price + (price*0.06)     
        return calculateSI


func = authenticate("admin","pwd123")
print("simple interest: " , func(1000,1,6))


#
#functiin def inside another function def
#function returning inner function (grandpa def invoke grandchild return)


#
#Anonymous function is function without name
#But, if u create fx without name what to call?
#It is always good to assign the anonymous fx to a var
#sum = def(a,b)
    #return a+b
#the above not valid, but this is how function are handled by python itself.
#That means in python every fx is an anonymous fx.
#the function can have only one statement (line of code)
def add(a,b): return a+b # def-short hand
add =lambda c,d: c+d # lambda function

farenheitToCel = lambda farenheitvalue: (farenheitvalue -32) *5/9

celciusvalues = map (farenheitToCel, lambda value: (value - 32) * 5/9)
print(list(celciusvalues))