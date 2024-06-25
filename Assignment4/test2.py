x = [1,4,3,2,6]



checkList = [] #len = 1
for i in x:
    kantoi = x.count(i)

    if  kantoi >= 2:
        checkList.append(i)
        break


if len(checkList) > 0:
    print("Not Unique")

else: # (if 0)
    print("Unique")


greet = "hello"
cl=greet.count("l")
print(cl)

    
        
    




       
    