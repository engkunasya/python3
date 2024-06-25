n = int(input("Please insert the value for Harmonic: "))


sum = 0
for i in range (1, n+1):
    print(i)
    sum = sum + 1/i

print(f"Harmonic number of {n} is {sum}")