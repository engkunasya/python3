
prime_num = []
n = 3

while n < 1000:
    is_prime = True
    for i in range (2,int(n ** 0.5)+2):
       

        if  n  % i  == 0:
            is_prime = False
            break

    if is_prime:
        prime_num.append(n)

    n+=1
# print(prime_num)

len_prime = len(prime_num)
prime_pair = []


# print(prime_pair)
for i in range (1,len_prime):
    if prime_num[i] -2 == prime_num[i-1]:
        prime_pair.append((prime_num[i],prime_num[i-1]))


print(prime_pair)   


