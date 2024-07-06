
# prime_num = [2]
# n = 2
# x = int(input())

# while n < x:
#     is_prime = True
#     for i in range (2,int(n ** 0.5)+2):
       

#         if  n  % i  == 0:
#             is_prime = False
#             break

#     if is_prime:
#         prime_num.append(n)

#     n+=1

# print(prime_num[-1])
# print(min(prime_num))

# primeFactors = [prime for prime in prime_num if prime <= max(prime_num)/2]
# print(primeFactors)

def prime_factors(number):
    factors = []  # List to store prime factors
    divisor = 2   # Start with the smallest prime number

    while number > 1: #if number less or equal to 1, break the outer loop
        while number % divisor == 0: #if number got remainder more than 0, break the loop
            factors.append(divisor)
            number //= divisor
        divisor += 1 #servee outer loop, not inner

    return factors

# Example usage:
number = int(input("Enter a number to find its prime factors: "))
result = prime_factors(number)
print("The prime factors of", number, "are:", result)