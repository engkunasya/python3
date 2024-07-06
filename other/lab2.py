prices = [ 1,2,3,4,5]
#using list comprehension
pricewithsst = [price + (price*0.6) for price in prices]
print(pricewithsst)


priceinEven = [number for number in prices if number % 2 == 0]
print(priceinEven) 



def sum(a,b):
    summation = a*b
    return summation

print(sum(5,3))


# from itertools import