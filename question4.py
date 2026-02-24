#Question 4

birth_year = int(input("Enter your birth year: "))        #Asking the user their birth year
current_year = 2026                                       #Assigning 2026 as the current age for calculating the current age
age_years = current_year-birth_year                       #Calculating the current age of the user         
age_months = age_years*12                                 #Calculating user's age in terms of months
age_days = age_years*365                                  #Calculating the user's age in termsof days
age_hours = age_days*24                                   #Calculating the user's age in terms of hours
age_minutes = age_hours*60                                #Calculating the user's age in terms of minutes
years_until_100 = 100-age_years                           #Calculating the years left to attain 100 years

#Printing all the calculated ages in terms of years, months, days, hours, along with years left to 100
print("Current Age:", age_years, "years")
print("Age in months:", age_months)
print("Age in days:", age_days)
print("Age in hours:", age_hours)
print("Age in minutes:", age_minutes)
print("Years until age 100:", years_until_100)