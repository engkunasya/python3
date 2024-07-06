



def generate_dict1(a_initial,b):
    dict_data1 = {}
    while a_initial < b:
        a_initial += 1
        divisors = [i for i in range(1, int(a_initial / 2) + 2) if a_initial % i == 0]
        dict_data1[a_initial] = sum(divisors)
    return dict_data1

def find_amicable_numbers(dict_data):
    amicable_numbers = []
    for key, value in dict_data.items():
        # "boolean exist", "boolean match", "boolean match"
        if value in dict_data and dict_data[value] == key and key != value: 
            amicable_numbers.append((key, value))

    return amicable_numbers  

a = int(input("Enter the lowest value: "))
b = int(input("Enter the highest value: "))
a_initial = int(a - 1)
dict_data= generate_dict1(a_initial,b)
# print(dict_data)

amicable_numbers = find_amicable_numbers(dict_data)
print("Amicable numbers in the range are: ", amicable_numbers)
