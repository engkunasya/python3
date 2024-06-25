# Write a program that takes two integers 
# from the user and calculates their greatest common 
# divisor (GCD) using the Euclidean algorithm.

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# a = abs(int(input("First number:"))) 
# b = abs(int(input("Second number:")))


# (a,b) = (b,a%b)

# gcd(a,b)


def gcd(a,b):
    while b!=0:
        a,b = b, a % b #SWAPPING
    return a


x = abs(int(input("First value")))
y = abs(int(input("Second value")))

if (y > x):
    x, y = y, x

answer = gcd(x,y)

print(f"The greatest common divisor of {x} and {y} is {answer}")