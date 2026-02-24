#Question 10

balance = 10000                                            #Initial amount assigned as the balance in the account
MIN_BALANCE = 500                                          #Minimum balance to be maintained always

#Allowing the user to perform 5 operations
for i in range(5):
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:                                                   #Checking the balance
        print("Current Balance:", balance)

    elif choice == 2:                                                 #Entering the amount to deposit in the account
        amount = int(input("Enter amount to deposit: "))
        if amount>0:                                                  #Checking if the amount to be deposited is greater than 0
            balance = balance+amount                                  #Adding the deposited amount to the balance
            print("Deposit successful!")
            print("New balance:", balance)
        else:
            print("Invalid deposit amount")                           #Printing invalid message if amount is equal to or lesser than 0 
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))             #Asking the user to enter the amount to withdraw 
        if amount<=0:                                                 #Checking if the amount entered is lesser than or equal to 0
            print("Invalid withdrawal amount")
        elif balance-amount<MIN_BALANCE:                              #Checking the balance if it goes less than minimum balance if the user withdraws  
            print("Insufficient balance!")     #Print as insufficient when user tries to withdraw amount which can violate minimum balance requirement
            print("Minimum balance of ₹500 must be maintained.")
        else:                                                         #Successful withdrawal and display updated balance
            balance = balance-amount
            print("Withdrawal successful!")
            print("New balance:", balance)
    elif choice == 4:                                                 #Thank you message and session termination message
        print("Thank you, Visit again.")
        print("Session ended.")
    else:
        print("Invalid choice. Please select between 1 and 4.")