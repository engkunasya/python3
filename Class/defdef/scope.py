def add(a,b):
    #result is a local var
    # a var created inside a function
    result = a+b
    return result

# The above discussion is called scope of a var.
x = 10
# variable x is created at the main context / global context

def modifyX():
    x = 5
    print("local", x)

print("global",x)
modifyX()
    


y = 16
def traditionalModifyY():
    y = 19

    return y #to modify a global var within a nested function, bubble up

x = traditionalModifyY()
print(y)
#THIS IS A PROPER OR BP


z = 200
def pythonModifyZ():
    global z   #modify the global read-only variable from withi.
    z = 300

    print("Inside", z)

pythonModifyZ()
print(z)


# Let us discuss about scope of variables in the function context
def simpleInterest(principle, period, rate): # outer function
    result = 0
    def printSimpleInterest(): # inner function
        temp = 0 # variable created inside the inner function
        print("Simple Interest:", result)
        print(temp)  # Moving print(temp) inside the inner function
    result = (principle * period * rate) / 100
    printSimpleInterest()

 

