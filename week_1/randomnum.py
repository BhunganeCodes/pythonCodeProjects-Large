import random

number = random.randint(0,100)
max_attempts = 10
guess = 0
count = 0

while count < max_attempts:

    guess = int(input("Enter Your Guess: "))
    
    if guess < number:
        print("Try Again! You Guessed Too Low!\n")
        count += 1
    elif guess > number:
        print("Try Again! You Guessed Too High!\n")
        count += 1
    else:
        print("Congratulations!\n")
        count += 1
        print(f"Total guesses: {count}")
        break
        
if guess != number:
    print("Game Over! Better Luck Next Time!\n")