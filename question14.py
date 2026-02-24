#Question 14

number = int(input("Enter a number: "))                      #Asking the user to enter a number
if number < 0:                                               #Checking if the number is less than 0
    print("Factorial is not defined for negative numbers")
elif number == 0:                                            #Checking if the number is equal to 0
    print("0! = 1")
else:                                                        #Calculating the factorial 
    fact = 1
    print(number , "! =", end=" ")
    for i in range(number, 0, -1):                           #Iterating the loop from the given number till 1
        fact*=i                                              #Calculating the factorial of the given number
        print(i, end=" ")
        if i!=1:                                             #Printing x symbol until i becomes 1
            print("×", end=" ")
    print("= ", fact) 