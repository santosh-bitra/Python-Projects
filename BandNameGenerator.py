#Program to generate your new band name.
'''This script will ask two questions, will input both and combine to form some really lame Band
name in a really lame and straight forward way. But hey, this is my 1st python project so, cheers.!'''

#importing module random for my addition to this script
import random

#giving city name into the variable x to contain
x = input("What is the name of the city you're from? " '\n')

#giving pet name into the variable y to contain
y = input("What is the name of your pet ? " '\n')

#holding few random cool words into the variable z
z = ["Mega", "Funky", "Giant", "Master", "The"]

#Printing the string and then using random.choice() to add a random header to the made up band name.
#the band name is just x with y beside and an empty space added in between
print("Your new band could be called", random.choice(z), x + " " + y)

#print(random.choice(z))
