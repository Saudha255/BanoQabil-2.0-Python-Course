#Name: Saudha Ibrahim
# Email: saudhaibrahim.76@gmail.com

#Objective: To create a python program for a calculator

#Welcome message

print("Welcome to Python Calculator!")


#defining main function

def calculator():
    
#main loop

    while True:
        print()
        print("Select an operation: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")

#User_Choice
        print()
        user_choice = int(input("Enter your choice (1, 2, 3, 4, or 5): "))

        if user_choice == 5:
          
                print("Exiting the calculator. Goodbye!!")
                break
                
        else:

#Note:Operand limit

                   print()
                   print("Operand limit: 2")
            
#Taking user input for operands
                   print()
                   num1 = float(input("Enter first number: "))
                   num2 = float(input("Enter second number: "))

#for Addition

        if user_choice == 1:
            addition_result = num1 + num2
            addition_result=round(addition_result, 3)
            print()
            print(f"Result = {num1} + {num2} = {addition_result}")

#for subtraction

        elif user_choice == 2:
            subtraction_result = num1 - num2
            subtraction_result=round(subtraction_result, 3)
            print()
            print(f"Result = {num1} - {num2} = {subtraction_result}")

#for Mulitiplication

        elif user_choice == 3:
            multiplication_result = num1 * num2
            multiplication_result=round(multiplication_result, 3)
            print()
            print(f"Result = {num1} × {num2} = {multiplication_result}")

#for division

        elif user_choice == 4:
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                division_result = num1 / num2
                division_result=round(division_result, 3)
                print()
                print(f"Result = {num1} ÷ {num2} = {division_result}")

if __name__ == "__main__":
    calculator()
