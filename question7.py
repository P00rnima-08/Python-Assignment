#Question 7

#Printing all types of possible conversions of the temperature
print("--- Temperature Converter ---")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")
print("7. Exit")
choice = int(input("Enter your choice (1-7): "))             #Asking the user to make choice and perform that particular conversion of temperature

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))       #Convert Celsius to Fahrenheit   
    f = (c*9/5)+32
    print("Temperature in Fahrenheit:", f)
elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))    #Convert Fahrenheit to Celsius
    c = (f-32)*5/9
    print("Temperature in Celsius:", c)
elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))       #Convert Celsius to Kelvin 
    k = c+273.15
    print("Temperature in Kelvin:", k)
elif choice == 4:
    k = float(input("Enter temperature in Kelvin: "))        #Kelvin to Celsius
    c = k-273.15
    print("Temperature in Celsius:", c)
elif choice == 5:
    f = float(input("Enter temperature in Fahrenheit: "))    #Fahrenheit to Kelvin 
    k = (f-32)*5/9+273.15
    print("Temperature in Kelvin:", k)
elif choice == 6:
    k = float(input("Enter temperature in Kelvin: "))        #Kelvin to Fahrenheit
    f = (k-273.15)*(9/5)+32
    print("Temperature in Fahrenheit:", f)
elif choice == 7:                                            #Program stops executing
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter a number between 1 and 7.")  #Prints this when user enters number other than 1-7