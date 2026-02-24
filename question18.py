# Calculator Functions

def add(first_number, second_number):                  #Addition Operation
    return first_number + second_number

def subtract(first_number, second_number):             #Subtraction Operation
    return first_number - second_number

def multiply(first_number, second_number):             #Multiplication Operation
    return first_number * second_number

def divide(first_number, second_number):               #Division Operation
    if b == 0:                                         #Checking if the denominator is 0 
        return "Cannot divide by zero"
    else:
        return first_number / second_number

def modulus(first_number, second_number):              #Modulus Operation
    return first_number % second_number

def power(first_number, second_number):                #Exponentiation/power Operation
    return first_number ** second_number

def calculator():
    print("\nCALCULATOR")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = int(input("Enter your choice: "))  #Choose an operation 

    if choice == 7:                             #Exiting the program
        print("Exiting calculator")
        return

    first_number = float(input("Enter first number: "))    #Asking the using to enter the first number
    second_number = float(input("Enter second number: "))   #Asking the using to enter the second number

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

calculator()                    #Calling the calculator function 
