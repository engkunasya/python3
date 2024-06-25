roman = ["I","V","X","L","C","D","M"] # use .index() or [index]

lead_num = [1,5,10,50,100,500,1000]

zipped = zip(roman, lead_num)

 
newList= list(zipped)
newTup= tuple(zipped)
newDic= dict(zipped)


print(newList)
print(newTup)
print(newDic)
