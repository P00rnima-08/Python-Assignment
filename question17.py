#Question 17 

value = input("Enter word/number: ")              #Enter a number or a word
original = value                                  #Saving the original word or number
reversed_value = ""

for ch in value:                                  # Reversing the word or the number by iterating each element 
    reversed_value = ch+reversed_value
print("Original:", original)                      #Printing the original word or number
print("Reversed:", reversed_value)                #Printing the reversed form of the word or the number
    
if original.lower() == reversed_value.lower():  #Converting both original word/number and reversed word/number to lower case and printing palindrome status
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")