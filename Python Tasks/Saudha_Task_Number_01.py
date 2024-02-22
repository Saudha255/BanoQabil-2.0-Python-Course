#Name: Saudha Ibrahim
 # Email: saudhaibrahim.76@gmail.com
  
 #Task Number 01
  #Even or Odd Checker
   
   #Objective--Write a Python program that takes an integer input from the user and checks if it's even or odd. Display an appropriate message.
print("---Even_Odd Checker---")
 
print() 
#user-input

num=int(input("Enter the whole number: ")) 

 #Conditional statement 
 
if num%2==0:
     print()
     print("The entered number is even in nature.")

else:
      print()
      print("The entered number is odd in nature.")
 
print()   
'''Task Number 02
   Multiplication Table Generator
   
 Objective--Create a program that generates a multiplication table for a given number. Allow the 

user to input the number and display the table.'''

print("---Multiplication Table Generator---")  

print()

#User input

num1=int(input("Enter the number for generating a multiplication table: "))

if num1==int(num1):

#range loop

    for num2 in range(1,11):
        product=num1*num2
        print(f"{num1}×{num2} = {product}")
else:
    print("Invalid input")
    
#Task Number 03

#Factorial Calculator 

#Objective--Write a Python program that calculates the factorial of a given number. Use a loop to perform the calculation.

print()

print("---Factorial calculator---")

print()

#defining a function

def factorial(num2):
    
    if num2 < 0:
        print("Invalid input: not defined for negative integers")
        
    else:
        for num1 in range(1, num2 + 1):
            num2 *= num1
            
    return num2

#user input

num1 = int(input("Enter a non-negative integer: "))

# Calculate factorial

fact = factorial(num1)

print(f"The factorial of {num1} is {fact}")

#Task Number 04
#Objective--Create a program that calculates the sum of the digits of a given number. For example, if the input is 12345, the output should be 15.

print()

print("---Sum of Digits---")

#defining function

def sum_of_digits(num):
        total_sum=0
        
# for loop

        for digits in str(num):
            total_sum+=int(digits)
        return total_sum 
        
# user input

print()
num_input=int(input("Enter the numbers:"))

#Call the function

number_input= sum_of_digits(num_input)

print(f"the total sum of given digits is {number_input}")

#Task Number 05
#FizzBuzz Game:
    
#Objective--Implement the FizzBuzz game in Python. Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and formultiples of both 3 and 5, print "FizzBuzz."

print()

print("---FizzBuzz Game---")

print()

#instructions
instructions=("instructions: \n1.If the entered number is the multiple of 3, the word 'fizz' will be printed. \n2.If the entered number is multiple of 5, the word 'buzz' will be printed")

print(instructions)
print()

#Choosing integers as user input

print("Choose from the integers given below: ")

#range loop

for numbers in range(1,101):
        
        print(f"{numbers:<5}", end=" ")  
        if numbers % 10 == 0:
            print()

print()

#user-input

user_input=input("Enter the number: ")

print()

#initialize variables

int=int(user_input)

# conditions

if int%3 == 0 and int%5==0:
        print("FizzBuzz")
            
elif  int%5 ==0:
            print("Buzz")
            
elif int%3==0:
            print("Fizz")
            
else: 
        print("not a multiple of 3 or 5")

print()

#Task Number 06
#PalindromeChecker

#Objective--Develop a Python program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards).

print("---Palindrome Checker---")
print()

#User-Input

word=input("Enter the word or phrase: ").lower()

print()

#using slicing for reversing input strings 
#Conditions

if word == word[ : :-1]:
    print("The entered word or phrase is a palindrome")
else:
    print("The entered word or phrase is not a palindrome")

print()
    
#Task Number 07
#Prime_Num_Checker

#Objective--Write a program that checks if a given number is prime or not. Display an appropriate message.

print("---Prime Number Checker---")
print()

#user-input

prime_num = int(input("Enter a number: "))

#Condition for checking prime number

if prime_num <= 1:
    print(prime_num, "is not a prime number")
    
else:
# check for factors in range loop

    for num in range(2, prime_num):
        if (prime_num % num) == 0:
            print(prime_num, "is not a prime number")
            break
    else:
        print(prime_num, "is a prime number")
