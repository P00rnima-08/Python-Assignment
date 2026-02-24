#Question 8

year = int(input("Enter a year: "))                            #Asking the user to give the year
if year%400 == 0:                                              #Checking if the year is divisible by 400
    print(year,": Leap Year")
    print("Reason: Divisible by 400")
elif year%4 == 0 and year%100!=0:                              #Checking the given year is divisible by 4 and not by 100
    print(year,": Leap Year")
    print("Reason: Divisible by 4 and not divisible by 100")
else:                                                          #This prints when the given year is neither divisible by 100 nor 400 nor 4
    print(year,": Not a leap Year")
    print("Reason: Does not satisfy leap year rules")