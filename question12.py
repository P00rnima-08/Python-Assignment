#Question 12

number = int(input("Enter number: "))        #Asking the user to enter a number whose table they want
rangee = int(input("Enter range (end): "))   #Asking the user to enter a number to detrmine how many times the previous number should be multiplied 
print("Multiplication Table of", number)
for i in range(1, rangee+1):                 #Iterating the loop till the number times the user wanted
    print(number,"x", i,"=",number*i)        #Printing the multiplication table of the number till the range