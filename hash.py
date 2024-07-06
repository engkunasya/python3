
#no duplication = hashable
fruits = { (1,2,3),(4,5,6),(1,2,3), (2,1,3)}

print(fruits)

nestedList = [[1,2,3],[3,4,5],[1,2,3]]
nestedList = list(map(tuple, nestedList))
print(nestedList)