# Function to generate Fibonacci series
n = 10
fib_series = [0, 1]
len_fib = len(fib_series)

while len_fib < n:
    new_fib = fib_series[-1] + fib_series[-2]
    fib_series.append(new_fib)
    len_fib +=1 #he length is recalculated on each iteration, reflecting the current size of the list after each append operation.

print("The first 10 terms of the Fibonacci series are:", fib_series)
      

# # Number of terms to generate
# n = 10

# # Generate and print the Fibonacci series
# fib_series = fibonacci(n)


# listA = [2,3,4,5,6]
# listA[-1] + listA[-1] 