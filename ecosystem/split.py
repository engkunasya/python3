numbers = input("Enter the numbers")
numberlist = numbers.split(",")
print(numberlist)
total = 0
for number in numberlist:
    total +=  int(number)
print(total)