fruits = ["hello", "mango","stabery","banana", "manggis", "mango"] #sambung ekor

fruits.copy

#fruits append

#fruits remove last item
 


 
fruits.insert(1, "durian") #fruits append sring at specified index


fruits.remove("hello") #fruits remove the element by value

fruits.pop() #fruits remove at the end, so simple

# python method.py # clear all element
# print(fruits)

# print(fruits)


# NAME ERROR
# greeting = "Hello alll"

# del greeting
# print(greeting) #name error

# print([2,3,4] + 5) #type error

newFruits = fruits[2:]
print(fruits.index("mango") +1)

#enumerate return list of tuple
#eachtuple has 2 items, first is index and second is item

print(fruits)
print(list(enumerate(fruits)))
fruits.sort()
print(fruits)

# print(tuple(map(str,fruits)))

jeganfruits = ["hello","stabery","mango", "banana", "manggis", "mango"] #sambung ekor

print(jeganfruits.index("mango") )