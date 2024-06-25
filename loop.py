# Foundation = "for loop"
fruits = ["apple" , 'orange', "mango", "banana", "grape", "rambutan", "durian", "mangosten"]
for fruit in fruits [::2]:
    print(fruit)

for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

# Foundation = "while loop"
count = -2 #initial state of while
while count < 5:
    count += 1  #setState of while
    print(count)
    


#For and Break
for i in range(1,10):
    if (i % 5 == 0 ):break
        
    print(f"break: {i}")  

#For and Continue
for i in range(10):
    if i % 2 == 0:continue
         # unlike break, continue jump to the loop and keep executing next sequence.
    print(f"continue: {i}")


#While and infinite loop
count = 0 #initial state of while
while count < 10:
    count += 1 #setState of while #if remove this line, code will print infinitely
    print("If line 3 in this codeblock deleted, This will print infinitely because count is not incremented")


#print each fruti (FOR) with its index value

position = 0 
for fruit in fruits:
    print(position, fruit)
    position += 1