
# input_bil = list(input("Please insert the number: ")) #453
# print(input_bil) #[4,5,3]

# Armstrong_list = []
# len_Armstrong = len(Armstrong_list)




# FOUNDATION: use input intro as capturer loop FOR sum or accumulation of i
# totalsum = 0
# for digit in range (7):
#     totalsum += digit
#     print(totalsum)
# print(totalsum)
    
# def is_armstrong_number(num):
#     num_str = str(num)
#     num_len = len(num_str)
#     sum_powered_digit = sum(int(digit) ** num_len for digit in num_str)
#     return sum_powered_digit == num

# input_user = int(input("Key in total Armstrong numbers you need: "))

# found_count = 0
# num = 0

# while found_count < input_user:
#     if is_armstrong_number(num):
#         print(num)
#         found_count += 1
#     num += 1

    

# def Armstrong():
#     x = int(m[n]) ** 3
#     len_m +=1
#     n +=1
#     x+=x
#     if x


#     #input computation?
# while len_Armstrong <= input_bil:
#     # Armstrong computation

#         sum = int(input_number[n])**3 
#         n +=1
#         lenDigits +=1

#         print(sum)

# lenArmstrong = len(armstrong)  # 453
# n = 0
# positionArmstrong = n


# while input_number > lenArmstrong:
#      cube = int(armstrong[n]) ** 3
#      print (cube)
#      n += 1

def is_armstrong_number(num):
    num_str = str(num)
    num_len = len(num_str)
    
    sum_powered_digit = 0
    for digit in num_str:
        powered_digit = int(digit) ** num_len
        sum_powered_digit += powered_digit
    
    return sum_powered_digit == num

input_user = int(input("Key in total Armstrong numbers you need: "))

found_count = 0
num = 0

while found_count < input_user:
    if is_armstrong_number(num):
        print(num)
        found_count += 1 #ikan keli
    num += 1 #ikan bilis