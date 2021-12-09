import random

num_of_guesses = {"easy": 10, "hard": 5}
print("Welcome to the NUmber Guessing Game!")
print("I'm thinking of a number between 1 nad 100.")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
correct_choice = False
while not correct_choice:
    try:
        nums = num_of_guesses[difficulty]
        correct_choice = True
    except:
        difficulty = input("Type 'easy' or 'hard': ")

guessed = random.randint(1, 100)

correct = False

while not nums == 0 and not correct:
    try:
        print(f"You have {nums} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess == guessed:
            print(f"You got it! The answer was {guessed}.")
            correct = True
        else:
            if guess > guessed:
                print("To high.")
            elif guess < guessed:
                print("To low.")
            
            nums -= 1
            if nums > 0:
                print("Guess again.")
    
    except:
        print("You may input only numbers.")
    

if nums == 0:
    print("You've run out of guesses, you lose.")

