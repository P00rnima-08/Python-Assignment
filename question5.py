#Qyuestion 5

total_bill = float(input("Enter the total bill: "))                #Asking the user to input total bill
number_of_people = int(input("Enter number of people: "))          #Asking the user to input number of people present
tax_percentage = int(input("Enter tax in percentage form: "))      #Asking the user to input tax percentage
tip_percentage = int(input("Enter tip in percentage form: "))      #Asking the user to input tip percentage

#Printing sub total, tax, bill after including tax, tip bill after including tip and money to be paid by each person
print("=== BILL BREAKDOWN ===")                     
print(f"Subtotal: {total_bill}")
tax_number=(tax_percentage/100)*total_bill
print(f"Tax({tax_percentage}%): {tax_number}")
after_tax=total_bill+tax_number
print(f"After tax: {after_tax}")
tip_number=(tip_percentage/100)*after_tax
print(f"Tip({tip_percentage}%): {tip_number}")
total=after_tax+tip_number
print(f"Total: {total}")
print(f"Per person: {total/number_of_people}")