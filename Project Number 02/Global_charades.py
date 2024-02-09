
#Name: Saudha Ibrahim

#E-mail: saudhaibrahim76@gmail.com

#Project: 02

#Objective:- To create a python program inspired by the classic game of charades, named "Global Charades-Guess the country edition"

# importing random module

import random

# Create a dictionary of countries and their corresponding facts as the first hint.

countries ={
    "India": "This country is famously known as the land of spices. Famous for the diversity in population and one of the biggest film industries in the world.",
    "Pakistan": "Diverse landscapes from high mountain ranges to deserts. It is the only Muslim nuclear power in the world and known for diverse cultures and delicious cuisine.",
    "China": "The second strongest economy in the world. It is known for technological advancement and historical inclination to communism.",
    "United States Of America": "The strongest economy and military in the world. It's the melting pot of cultures from all over the world and it is home to the biggest film industry in the world.",
    "Germany": "Famous for manufacturing sports cars, innovative engineering, and beer culture. It was on the offensive side in World War II."
}


# Welcome message

print("Welcome to Global Charades - Guess the Country Edition!")

#Rules

rules = ( "Rules:-\n" 
         "1. You will get 3 attempts to guess a country based on hints provided.\n"
         "2. Write the first letter of every word of your answer in uppercase, the rest in lowercase.\n"
         "3. You have to write full form of usually abbreviated country names")
         
print(rules)

# Defining the main function to run the game loop

def play_game():

    while True:
        
# Choose a random country

        country=random.choice(list(countries.keys()))
        
# Initialize variables

        attempts_left = 3
        hints_given = 0

# Game loop

        while attempts_left > 0:
            
# Provide a hint based on hints_given

            if hints_given == 0:
                
                hint_1 = "First hint: " + countries[country]
                
                print(hint_1)
                
            elif hints_given == 1:
                
                hint_2 = "Second hint: "
                
# Providing Second hint which include famous monuments and landmarks

                if country == "India":
                    hint_2 += "Home to The great Taj Mahal."
                    
                elif country == "Pakistan":
                    hint_2 += "Home to Iconic Badshahi Mosque."
                    
                elif country == "China":
                    hint_2 += "Home to The Great Wall."
                    
                elif country == "United States Of America":
                    hint_2 += "Known for its famous landmark, The Statue of Liberty."
                    
                else:
                    hint_2 += "Home to the memorabilia of World War II victims."
                    
                print(hint_2)
                
            else:
                hint_3 = "Third hint: "
               
 # Providing third hint which include capitals of respective countries
 
                if country == "India":
                    hint_3 += "The capital of this country is New Delhi."
                    
                elif country == "Pakistan":
                    hint_3 += "The capital of this country is Islamabad."
                    
                elif country == "China":
                    hint_3 += "This country's capital is Beijing."
                    
                elif country == "United States Of America":
                    hint_3 += "This country's capital is Washington D.C."
                    
                else:
                    hint_3 += "The capital of this country is Berlin."
                    
                print(hint_3)

#Take a Guess as input from player 

            guess = input("Enter your guess: ")
       
# Check if guess is correct

            if guess == country:
                
                print("Congratulations! You won! :D")
                break
                
            else:
                attempts_left -= 1
                hints_given += 1
          
# Provide feedback based on remaining guesses

                if attempts_left > 0:
                    
                    print(f"Incorrect. You have {attempts_left} attempts left.")
                    
                else:
                    print("Sorry! You lose :(")
                    
                    print(f"The correct answer was: {country.upper()}")

# Ask if player wants to play again

        play_again = input("Would you like to play again? (yes/no) ")
        
#If player wants to exit
        if play_again.lower() != "yes":
            break
#else

if __name__ == "__main__":
    play_game()
