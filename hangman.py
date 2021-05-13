"Importing Random Module"
import random

#Setting the list of wrods to be guessed into the list 'set'
set = ['santosh', 'hari', 'dadi', 'bagal', 'ganguly']

#Choosing the random word to be guessed to start
word = random.choice(set)

#Converting the string of the variable word into a list called word1
word1 = list(word)

#Calculating the length of the word to be guessed. This will be used to print the number of dashes.
c = len(word1)
print(f"_ "*c)
#print(c)

#Letting the player know the number of words he needs to guess to complete the game. Also asking him to guess the word.
print(f"This name consists of {c} number of letters")
v = input("Guess a word :")

#This conditional logic is still under construction.
for i in word1:
    if v == i:
        print("Yes")
    else:
        print("No")

#Printing the answer
print(word1)

