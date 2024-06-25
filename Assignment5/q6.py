x = 10

list_perfect = []
len_perfect = len(list_perfect)

list_proto = []

# while len_perfect < x:

# while len_perfect < x:


m = 6
while len_perfect < 10:
     
    for i in range (1, int(m **0.5) + 1): #inclusive so make it add 2 to make it 3.

        if m % i == 0:
            list_proto.append(i)          
    # print(list_proto) #finalize
    # m=+1

    if sum(list_proto) == m:
        list_perfect.append(m)
        list_proto.clear()
        print(list_proto)
        print(list_perfect)
        len_perfect +=1

    m+=1





    # python q6.py
        


#try again
# x = 10

# list_perfect = []

# m = 6

# while len(list_perfect) < x:
#     list_proto = []
    
#     # Find the divisors of m
#     for i in range(1, int(m**0.5) + 1): 
#         if m % i == 0:
#             list_proto.append(i)
#             print(list_proto)

#             if sum(list_proto) == m:
#               list_perfect.append(m)
    

    
#     # Check if the sum of divisors (excluding the number itself) is equal to m
    
#     m += 1

# print(list_perfect)