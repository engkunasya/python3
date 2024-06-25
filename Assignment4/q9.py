# import sys

# # Function to calculate the average of a list of numbers
# def calculate_average(numbers):
#     total = 0
#     count = 0
#     for number in numbers:
#         total += number
#         count += 1
#     return total / count if count != 0 else 0

# # Ensure there are command line arguments provided
# if len(sys.argv) > 1:
#     # Convert command line arguments to a list of integers
#     numbers = list(map(int, sys.argv[1:]))

#     # Calculate the average
#     average = calculate_average(numbers)

#     # Output the result
#     print(f"The average of the provided numbers is: {average}")
# else:
#     print("Please provide a few numbers as command line arguments.")

#INPUT
# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    total = sum(numbers)  # Calculate the sum of numbers in the list
    count = len(numbers)  # Determine the number of elements in the list

    # Calculate the average, handling the case where count is 0 to avoid division by zero
    if count != 0:
        return total / count
    else:
        return 0

# Input handling
numbers = []
while True:
    try:
        num = input("Enter a number (or 'done' to finish): ")
        if num.lower() == 'done':
            break
        numbers.append(float(num))  # Convert input to float
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the average
if numbers:
    average = calculate_average(numbers)
    print(f"The average of the provided numbers is: {average}")
else:
    print("No numbers provided to calculate average.")
