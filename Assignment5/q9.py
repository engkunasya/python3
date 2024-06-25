# roman = ["I","V","X","L","C","D","M"] # use .index() or [index]
# lead_num = [1,5,10,50,100,500,1000]
# romanzipped = zip(roman, lead_num)
# romanDic = dict(romanzipped)




# inter = input("Insert the integer value: ")

# #prioritize unique rare
# for key, value in romanDic.items():
#     if int(inter) == value:
#         print(f"The Roman Numeral for {inter} is {key}")



# inter_list = list(map(int, inter))



# if inter_list [-1] == 4:
#     end_roman = roman[0]+roman[1]
#     print(end_roman)

# elif inter_list [-1] == 9:
#     end_roman = roman[0] + roman[2]

#     print(end_roman)


# elif inter_list[-1] in [1, 2, 3, 6, 7, 8]:
#     for i in range(1,inter_list[-1] +1):
#         end_roman = roman[0]*i
#         if i > 5:
#             end_roman = roman[0]*(i - 5)
#     print(end_roman)



# if len(inter_list) == 2:
#     if inter_list[0] <3:
#         start_roman = inter_list[0] * roman[2]
#         print(start_roman)

#     elif inter_list[0] == 3:
#         start_roman = inter_list[0] * roman[2]

#     elif inter_list[0] == 4:
#         start_roman = roman[2] + roman[3]
#         print(start_roman)







# Mapping of Roman numerals to integers
roman = ["I", "V", "X", "L", "C", "D", "M"]
lead_num = [1, 5, 10, 50, 100, 500, 1000]
romanDic = dict(zip(lead_num, roman))  # Dictionary mapping integers to Roman numerals

# Input integer value
inter = int(input("Insert the integer value: "))

# Initialize the Roman numeral string
roman_numeral = ""

# Check if the input is exactly in the lead_num list
if inter in lead_num:
    roman_numeral = romanDic[inter]

else:
    # Handle cases where the input integer needs to be converted to Roman numeral
    if inter >= 1000:
        roman_numeral += "M" * (inter // 1000)
        inter %= 1000

    if inter >= 900:
        roman_numeral += "CM"
        inter %= 900

    if inter >= 500:
        roman_numeral += "D"
        inter %= 500

    if inter >= 400:
        roman_numeral += "CD"
        inter %= 400

    if inter >= 100:
        roman_numeral += "C" * (inter // 100)
        inter %= 100

    if inter >= 90:
        roman_numeral += "XC"
        inter %= 90

    if inter >= 50:
        roman_numeral += "L"
        inter %= 50

    if inter >= 40:
        roman_numeral += "XL"
        inter %= 40

    if inter >= 10:
        roman_numeral += "X" * (inter // 10)
        inter %= 10

    if inter >= 9:
        roman_numeral += "IX"
        inter %= 9

    if inter >= 5:
        roman_numeral += "V"
        inter %= 5

    if inter >= 4:
        roman_numeral += "IV"
        inter %= 4

    if inter >= 1:
        roman_numeral += "I" * inter

# Output the Roman numeral for the input integer
print(f"The Roman Numeral for {inter} is {roman_numeral}")

def roman_to_integer(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for symbol in roman:
        current_value = roman_numerals[symbol]
        
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

# Example usage:
roman_numeral = input().upper()  # MXMX
integer_value = roman_to_integer(roman_numeral)
print(f"The integer value of '{roman_numeral}' is {integer_value}")


        




    




