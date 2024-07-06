import functools
import operator

x = input("Please enter the digits: ")
x_int = int(x)

num = 1
num_list = []


while x_int > 0:
    y = x_int % 10
    num_list.append(y)

    x_int //= 10

# print (num_list)

multiply_List = functools.reduce(operator.mul, num_list)
print(f"The product of {x} is:\n{multiply_List}")