import random

set = ['santosh', 'hari', 'dadi', 'bagal', 'ganguly']

word = random.choice(set)

word1 = list(word)

v = input("Guess a word :")

for i in word1:
    if v == i:
        print("Yes")
    else:
        print("No")


print(word1)

