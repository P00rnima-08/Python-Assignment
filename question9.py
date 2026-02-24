#Question 9

age = int(input("Enter age: "))                                                     #Asking the user to input their age 
day_of_week = input("Enter day of week: ").lower()                                  #Asking the user to input the day of a week
number_of_tickets = int(input("Enter number of tickets: "))                         #Asking the user to enter the number of tickets required 

#Pricing and category based on the given age
if age < 3:
    base_price = 0
    category = "Free"
elif age <= 12:
    base_price = 150
    category = "Child"
elif age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

#Calculating base amount
total_base = base_price*number_of_tickets

#Discounts available based on the given day
if day_of_week == "friday" or day_of_week == "saturday" or day_of_week == "sunday":
    discount = total_base * 0.20
else:
    discount = 0

#Calculating price after discount
price_after_discount = total_base - discount

#Displaying the final result
print("\n--- TICKET DETAILS ---")
print("Category:", category)
print("Base price per ticket: ₹", base_price)
print("Number of tickets:", number_of_tickets)
print("Base price (all tickets): ₹", total_base)
print("Discount: ₹", discount)
print("Price after discount: ₹", price_after_discount)
print("Total amount to pay: ₹", price_after_discount)