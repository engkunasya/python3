#dont do thos
x= [ 20, 30, 40, 50]
y = x
x[2] = 35

print(x)
print(y)

#we have to perform deep copy
y1 = []
for i in x:
    y1.append(i)

print("=" * 40)
print(x)
print(y1)
x[2] = 36
print(x)
print(y1)

#conclusion u dont need to use for loop to copy.

x2= [ 20, 30, 40, 50]
y2 = x2.copy()

x2[0] = 1
print("x2:",x2)
print("y2:",y2)

#fruits is an insrtance of a list class
# the obj are created by clalling the class
#fruits ? list ? class?
x3 = list([1,2,3,4,5])
print(x3)
print(type(x3))

x3 = [5,6,7,8,9]
print (x3)
#sir argue about class vs function

# ** CLEAR THE AIR of `()` **
#   to invoke or call the operator  we use is ()
#   TO CALL BUILTIN FUNCTION WE CALL () eg print()

#   type, int float are class, not function
#   to create object we call class, eg list ()

#   to call function inside a modulesys.path
#   to call method inside a object "Television".split()
#   

