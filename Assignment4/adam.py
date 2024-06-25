# input_number = int(input("Enter how many Adam numbers you want: "))
# adam = []

# number = 0
# while len(adam) < input_number:
#     original_square = number ** 2
#     reverse_of_number = int(str(number)[::-1])
#     reverse_of_square = reverse_of_number ** 2

#     if int(str(original_square)[::-1]) == reverse_of_square:
#         adam.append(number)

#     number += 1

# print("Adam Numbers:", adam)


x = int(input("Enter how many Adam numbers you want: "))
y = 1
adamNum = []
lenAN = len(adamNum)

while x > lenAN:
    revNum = int(str(y)[::-1])
    sqrNum = y **2
    sqrRevNum = revNum**2
    revSqrRevNum = int(str(sqrRevNum)[::-1])

    if sqrNum == revSqrRevNum:
        adamNum.append(y)
        lenAN = lenAN + 1  #ikan keli

    y+=1 #ikan bilis

print(adamNum)