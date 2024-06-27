x = 10

list_perfect = []
len_perfect = len(list_perfect)

list_proto = []

# while len_perfect < x:

# while len_perfect < x:


m = 6
     
for i in range (1, int(m **0.5) + 2): #inclusive so make it add 2 to make it 3.

    
    # list_proto = [] #it will clear after one complete iteration
    if m % i == 0:
        list_proto.append(i)  #[1] [1,2] [1,2,3]        
    # print(list_proto) #finalize debug run
   
    if sum(list_proto) == m:
        list_perfect.append(m)

    
    
        

    

print(f"Perfect numbers are {list_perfect}")

 

    





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