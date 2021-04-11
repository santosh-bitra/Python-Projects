# Program to calculate BMI
x = int(input("Please enter your current mass (in kg): "))
y = int(input("Please enter your current height (in centimeters): "))

z = (x / y ** 2) * 100 ** 2

print("As per your input, your current BMI index is: ", z)

print("\n")

if (float(z) < 18.5):
    print("your bmi indicates that you are 'UNDERWEIGHT' \n")

elif (18.5 < float(z) < 25):
    print("Your bmi indicates that you are under 'NORMAL' weight categeory \n")

else:
    print("You are 'OVER-WEIGHT'")
