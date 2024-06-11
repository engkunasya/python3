# Foundation = "for"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Foundation = "loop"
count = -2
while count < 5:
    count += 1
    print(count)
    


#Break
for i in range(5):
    if (i == 4):
        break
    print(i)    

#Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


#infinite loop
count = 0
while count < 10:
    count += 1
    print("If line 3 in this codeblock deleted, This will print infinitely because count is not incremented")


