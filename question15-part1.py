#Question 15

#Part 1
number = int(input("Enter a number: "))           #Asking an user to enter a number
if number <= 1:                                   #Checking if the given number is less than or equal to 1
    print(number, "is NOT a prime number")
else:
    is_prime = True
    for i in range(2, number):                   #Checking if the given number if divisible by any number starting from 2 till the given number
        if number % i == 0:
            is_prime = False
    if is_prime:                                 #Printing if the given number is prime or not
        print(number, "is a PRIME number")
    else:
        print(number, "is NOT a prime number")