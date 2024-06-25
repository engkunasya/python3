# Write a program to perform basic string compression using the counts of repeated characters (e.g., "aabcccccaaa" -> "a2b1c5a3").

x = input("")
# y = list(x)

# y.remove(y[0])
# print(y)

# #aabcccccaaa"
# # a2b1c5a3

# count = 1
# for i in y:
#     if y[0] == y[1]:
#         y.remove(y[0])
#         count+=1

# Convert string to list for easier manipulation
y = list(x)

# Initialize variables
compressed_string = ""
count = 1

# Loop through the characters of the list
while y:
    # Check if the current character is the same as the next one
    if len(y) > 1 and y[0] == y[1]:
        count += 1
        y.pop(0)  # Remove the first element since it's already counted
    else:
        # Append the character and its count to the compressed string
        compressed_string += y[0] + str(count)
        count = 1  # Reset count for the next character
        y.pop(0)   # Remove the processed character from the list

print( compressed_string)
