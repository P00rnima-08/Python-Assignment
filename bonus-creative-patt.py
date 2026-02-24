for run in range(1, 8):                 # Loop to run the whole pattern code 5 times
    choice = int(input("Choose pattern (1-6): "))      # Asking the user to choose which pattern they need
    height = int(input("Enter height: "))              # Asking the user to enter the height

    if choice == 1:                                   # First pattern
        for i in range(1, height+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
    elif choice == 2:                                 # Second pattern 
        for i in range(1, height+1):
            for j in range(i):
                print(i, end=" ")
            print()
    elif choice == 3:                                 # Third pattern 
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()
    elif choice == 4:                                 # Fourth pattern 
        for i in range(1, height+1):
            for j in range(1, i+1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()
    elif choice == 5:                                 # Fifth pattern
        for i in range(1, height+1):
            print(" "*(height-i) + "* " * i)
    elif choice == 6:                                 # Sixth pattern: Simple right-angled star triangle
        for i in range(1, height+1):
            print("* " * i)
    else:                                             # Invalid choice message
        print("Invalid choice")