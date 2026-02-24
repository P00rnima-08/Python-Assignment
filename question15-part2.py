#Part 2
start = int(input("Enter start range: "))         #Asking the user to enetr the start value
end = int(input("Enter end range: "))             #Asking the user to enetr the end value
print("Prime numbers:", end=" ")
for num in range(start, end + 1):                 #Ierating for loop from strart value till end value
    if num > 1:                                   #Checking if the numbers are greater than 1 
        is_prime = True
        for i in range(2, num):                   #Iterating from 2 till the number
            if num % i == 0:
                is_prime = False                  #Calculating if the number is prime or not
        if is_prime:
            print(num, end=" ")                   #Printing the prime status