import random

rand = random.randint(1,100)
print(rand)

guess= int(input("Please guess the number: "))

while True: #setup to True to initialize the  while loop

    if guess == rand:
        print(f"Yes, {guess} is correct!")
        break  # Exit the loop if the guess is correct

    elif guess > rand:
         print("Oops, too high!") #then guess input again

    else:
        print("Oops, too low!") #then guess input again
    
    guess= int(input("Please guess the number: ")) # here until first if is met




