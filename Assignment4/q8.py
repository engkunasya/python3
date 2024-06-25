# import sys

# # total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)

# # Arguments passed
# print("\nName of Python script:", sys.argv[0])

# print("\nArguments passed:", end = " ")
# for i in range(1, n):
#     print(sys.argv[i], end = " ")

# # Addition of numbers
# Sum = 0
# # Using argparse module
# for i in range(1, n):
#     Sum += int(sys.argv[i])

# print("\n\nResult:", Sum)

# Function to display all elements
def display_all_elements(numbers):
    print("All elements:")
    for number in numbers:
        print(number, end=" ")
    print()

# Function to display elements in even positions
def display_even_position_elements(numbers):
    print("Elements in even positions:")
    for i in range(1, len(numbers), 2):
        print(numbers[i], end=" ")
    print()

# Function to display elements in odd positions
def display_odd_position_elements(numbers):
    print("Elements in odd positions:")
    for i in range(0, len(numbers), 2):
        print(numbers[i], end=" ")
    print()

# Input handling
numbers = []
while True:
    try:
        num = input("Enter a number (or 'done' to finish): ")
        if num.lower() == 'done':
            break
        numbers.append(int(num))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Display all elements
display_all_elements(numbers)

# Display elements in even positions
display_even_position_elements(numbers)

# Display elements in odd positions
display_odd_position_elements(numbers)
