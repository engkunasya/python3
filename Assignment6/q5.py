def factors(num):
    """Return a list of all the factors of a given number."""
    factorsList = []
    for i in range(1, int(num / 2 + 1)):
        if num % i == 0:
            factorsList.append(i)
            # if i != num // i:  
            #     factorsList.append(num // i)
    return factorsList #print(factorList)



num = int(input("Enter the number: "))
print(factors(num))
