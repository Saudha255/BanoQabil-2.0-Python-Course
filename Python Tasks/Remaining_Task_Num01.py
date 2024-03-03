#Task Number 07
#Prime Number Checker

print("Prime Number Checker")
print()

#user-input

num_input = int(input("Enter the Number: "))

#for loop 

for num in range(2, num_input):
        if num_input % num == 0:
            print(f"{num_input} is not a prime number")
            break
else:
        print(f"{num_input} is a prime number")
        print()
    
#Task Number 08

#Objective--To Create a word guessing game.
  
print("-----WordQuest- A Word Guessing Game-----")
print()
print("instructions: \nEnter your guess in lowercase only")

import random

# List of words
pak_cities = ["karachi", "islamabad", "lahore", "quetta"]
birds = ["eagle", "sparrow", "pigeon", "crow"]
fruits = ["mango", "kiwi", "orange", "guava"]


# Combining all lists into one
words = pak_cities + birds + fruits

# Choosing a random word from the list
random_guess = random.choice(words)

print()

# Providing hints based on the category of the word

if random_guess in pak_cities:
    print("Hint: It is a city in Pakistan")
    
elif random_guess in birds:
    print("Hint: It is a bird")

else:
    print("Hint: It is a fruit")

# User input and attempts

user_guess = ''
attempts = 5

# Main loop

while attempts > 0:
    print("Attempts left:", attempts)
    user_guess = input("Guess the word: ").lower()
    
    # Checking if the user's guess is correct
    
    if user_guess == random_guess:
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        print("Incorrect guess. Try again.")
        attempts -= 1
        
        # Checking if attempts are exhausted
        
        if attempts == 0:
            print("Sorry, you ran out of attempts. The word was:", random_guess)
            break
  
