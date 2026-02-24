import math  # Needed for square root

def add(first_number, second_number):                  #Addition Operation
    return first_number + second_number

def subtract(first_number, second_number):             #Subtraction Operation
    return first_number - second_number

def multiply(first_number, second_number):             #Multiplication Operation
    return first_number * second_number

def divide(first_number, second_number):               #Division Operation
    if second_number == 0:                             #Checking if the denominator is 0 
        return "Cannot divide by zero"
    else:
        return first_number / second_number

def modulus(first_number, second_number):              #Modulus Operation
    return first_number % second_number

def power(first_number, second_number):                #Exponentiation/power Operation
    return first_number ** second_number

def square_root(number):                               #Square root operation
    if number < 0:
        return "Invalid input for square root"
    return math.sqrt(number)

def percentage(a, b):                                  #Percentage calculation a% of b
    return (a * b) / 100

def calculator():
    print("\nCALCULATOR")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Percentage")
    print("9. Exit")

    choice = int(input("Enter your choice: "))  #Choose an operation 

    if choice == 9:                             #Exiting the program
        print("Exiting calculator")
        return

    if choice == 7:                             #Square root needs only one number
        first_number = float(input("Enter number: "))
        print("Result:", square_root(first_number))
    elif choice == 8:                           #Percentage calculation
        first_number = float(input("Enter first number (percentage): "))
        second_number = float(input("Enter second number: "))
        print("Result:", percentage(first_number, second_number))
    else:
        first_number = float(input("Enter first number: "))    #Asking the user to enter the first number
        second_number = float(input("Enter second number: "))   #Asking the user to enter the second number

        if choice == 1:
            print("Result:", add(first_number, second_number))
        elif choice == 2:
            print("Result:", subtract(first_number, second_number))
        elif choice == 3:
            print("Result:", multiply(first_number, second_number))
        elif choice == 4:
            print("Result:", divide(first_number, second_number))
        elif choice == 5:
            print("Result:", modulus(first_number, second_number))
        elif choice == 6:
            print("Result:", power(first_number, second_number))
        else:
            print("Invalid choice")

calculator()  # Calling the calculator function