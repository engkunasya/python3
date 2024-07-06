def luhn(x):
    x = list(x)
    x = list(map(int, x))

    list_reserve = []
    list_alter = []
   

    for i in range(len(x)):
        if i % 2 != 0:
            list_reserve.append(x[i])
        else:
            doubled = x[i] * 2
            if doubled > 9:
                doubled -= 9
            list_alter.append(doubled)

    list_final = list_reserve + list_alter

    checksum = sum(list_final)

    return checksum

# Example usage:
x = input("Please enter card number:" ).strip().replace(" ","").replace("-","")


if x.isdigit():
    luhnn = luhn(x)
    print(f"The checksum using Luhn is {luhnn}")
    if luhnn % 10  == 0:
            print(f"---The checksum value using Luhn is {luhnn}")
            print(f"---{luhnn} is divisible by 10\n---The number is valid!")

    if luhnn % 10  != 0:
            print(f"---The checksum value using Luhn is {luhnn}")
            print(f"---{luhnn} is NOT divisible by 10\n---The number NOT valid!")


else:
    print("Please enter proper card number")
    
# 4539319503436467