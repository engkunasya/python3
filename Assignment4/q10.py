# x = input()
# z= x.split(',')
# zNumList = list(map(int, z))
# zNumString = ' '.join(z) # Join only accept string as parameter.
# print (zNumList)
# print(zNumString)


# z = set (x)

# a = [1,3,2,4,5]
# b = (1,2,3,4,5)

# if len(a) == len(b):
#     print("It is same number")
# else:
#     print("Nope")

    # Input string
input_string = input("Enter numbers separated by commas: ")
zListString = input_string.split(",")

# Convert input string to a list of integers
numbers = list(map(int, zListString))
  
# Check if all numbers are unique 
all_unique = len(numbers) == len(set(numbers))  

# Output the result
if all_unique:
    print("All the numbers are different from each other.")
else:
    print("There are duplicate numbers in the list.")