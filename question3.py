#Question 3

sentence = input("Enter a sentence: ")                         #Asking the user to give a sentence as an input
print("Original:", sentence)                                   #Printing the original sentence
print("Characters (with spaces):", len(sentence))              #Counting the characters including the spaces in the sentence 
without_spaces = sentence.replace(" ", "")                     
print("Characters (without spaces):", len(without_spaces))     #Counting the characters excluding the spaces
words = sentence.split()                                       
print("Words:", len(words))                                    #Counting the number of words present in a sentence
print("UPPERCASE:", sentence.upper())                          #Printing the upper case of the sentence
print("lowercase:", sentence.lower())                          #Printing the lower case of the sentence
print("Title Case:", sentence.title())                         #Printing the title case of the sentence
print("First word:", words[0])                                 #Printing the first word in a sentence using index "0"
print("Last word:", words[-1])                                 #Printing the last word in a sentence using index "-1"
reversed_sentence = ""
for char in sentence:                                          #Reversing a sentence and printing it
    reversed_sentence = char + reversed_sentence
print("Reversed:", reversed_sentence)    