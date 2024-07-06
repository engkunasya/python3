#let us find the perfect number, dont confuse wiith prime, adam , armstrong, divisors.

# PERFECT number is the example of  28, 1+2+4+7+14

# x = int(input())

def generate_dict1():
    dict_data = {}
    num = 0
    while len(dict_data) < 10000:
        num += 1
        divisors = [i for i in range(1, int(num / 2) + 2) if num % i == 0]
        dict_data[num] = sum(divisors)

    return [i for i in dict_data if dict_data[i] == i]
        


dict_data1 = generate_dict1()
print(dict_data1)

