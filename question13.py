#Question 13

numbers = int(input("How many numbers? "))    #Asking the user to enter a number

total = 0                                     #Initializing the total variable to 0
maximum = None
minimum = None

for i in range(1, numbers + 1):               #Ierating the for loop till the number specified by the user
    num=int(input(f"Enter {i} number :"))     #Asking the user to enter numbers they want to add
    total = total+num                         #Adding all the numbers

    if maximum is None or num > maximum:      #Finding the maximum number out of the given numbers
        maximum = num
    if minimum is None or num < minimum:      #Finding the minimum number out of the given numbers
        minimum = num

average = total/numbers                       #Calculating the average using the total and the numbers of items

#Printing sum, average, minimum number and maximum number
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)