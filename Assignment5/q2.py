try:
    starting_number = int(input("Enter a positive integer: "))
    
    if starting_number <= 0:
        raise ValueError("The number must be a positive integer.")
    
    n = starting_number
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    print(f"The Collatz sequence starting at {starting_number} is: {sequence}")

except ValueError as e:
    print(e)
