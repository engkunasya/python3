from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Use reduce to calculate the product of all numbers
product = reduce(multiply, numbers)

# Print the product
print("The product of all numbers:", product)
