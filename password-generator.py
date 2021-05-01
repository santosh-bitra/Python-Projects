# Random Password Generator
# Importing random module
import random

# PreDefining List for Alphabets
Alphabets = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

# PreDefining List for Numbers
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# PreDefining List for Charecters
Charecters = ["<", ">", "/", "$", "#", "&", "@", "."]

# Ask user for the number of alphabets, numbers and characters he wants in his password
a = int(input("How many alphabets do you want in your password? "))
b = int(input("How many numbers do you want in your password? "))
c = int(input("How many characters do you want in your password? "))
keyword = input("Kindly enter your keyword : ")

''' The actual logic goes below. Level = complex '''
# Defining variable 'password' as []. this means it is an empty list for now and will keep adding/appending values that are thrown by the loops into it.
# The logic below is to keep appending random alphabets till i = 5.
# The similar is carried out sequentially for numbers and special characters as well.
password = []
for i in range(0, a):
    password += random.choice(Alphabets)

for i in range(0, b):
    password += str(random.choice(Numbers))

for i in range(0, c):
    password += random.choice(Charecters)

# We are now printing the final list that has been created due to the above logic.
# This should contain all the values of the password but in list form, which will further be shuffled and set as one word.
# We are also then shuffling the list for more security using random.shuffle module-function
random.shuffle(password)

# We are now converting the final passwd list to string so we can get the passwd as a single word and not separated
y = f"{keyword}"
for x in password:
    y += x

y = list(y)
random.shuffle(y)
z = ''.join(y)

print(f"Your new complex password is : {z}")


