def combination(n, r):
    if r == n or r == 0:
        return 1
    if r == 1:
        return n
    return combination(n-1, r) + combination(n-1, r-1)


n = int(input("Enter n: "))

for i in range(n):
    for j in range(n-i):
        
        print(" ", end="")
    for j in range(i+1):
        print(combination(i, j), end=" ")
    print()
# print(combination(4, 2))
