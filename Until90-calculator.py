#Program to calculate how many days, weeks and years left until you're 90 years old
'''This program will ask you of your date of birth, maybe to calculate your current age.
It will then calculate how many days, weeks and years are precisely left until you turn to 90 years of age.
The important factors to be noted are the following:
1 year = 365 days = 12 months = 52 weeks
90 years = 32,850 days =  1,080 months = 4,680 weeks'''

#input is an integer of the year, month and date you were born
year = int(input("What is the year you were born in ? :"))

month = int(input("What is the month you were born in ? :"))

date = int(input("What is the date you were born in ? :"))


#establishing few variables as constants in this program such as the current year and then calculating your current age 
this_year = 2021
age = this_year - year
#print("Your current age is ", age)

#This below is the actual part this is going to calculate and determine the number of years, months, weeks and days until you are 90
years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

#your current age is now printed
print("Your current age is :", age)

#just printing an extra line for space
print("\n")

#printing the final output for the user
print(f"You have \n {years_left} years, \n {months_left} months, \n {weeks_left} weeks and \n {days_left} days left until you are 90")

