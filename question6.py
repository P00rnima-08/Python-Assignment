#Question 6

total_marks = 0                                            #Initializing total marks as 0
pass_status = True                                         #Initializing the pass status as 1
for i in range(1, 6):                                      #Iteration to input marks of 5 subjects 
    mark = int(input(f"Enter marks for Subject {i}: "))
    total_marks += mark                                    #Adding all the 5 subject marks

percentage = (total_marks / 500) * 100                     #Calculating the percentage with maximum marks of 500

# Finding the grade based on the percentage
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Declaring Pass or Fail 
if mark < 40:
    result="Fail"
else:
    result="Pass"
    
# Display results
print("Grade Scale")
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)