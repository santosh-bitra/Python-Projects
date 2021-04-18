#Love Percentage Calculator

#Just an intro message on the program/app
print("Hello.! Welcome to the love calculator. \n"
      "This in an app where you enter the your name along with your crush's name \n"
      "and you get to know how good will it work between you two .!!")

#inout the names to be stored as below variables
name1 = input("\n Enter your full name : ")
name2 = input("\n Enter your crush's full name : ")

#converting any upper caps input to lower caps using lower() function
name1_smaller = name1.lower()

name2_smaller = name2.lower()

#concactinating the values for effeciency
total_name = name1_smaller + name2_smaller

#counr() to count the strings repeated in the input. used map and sum to make it efficiently map and sum the format
count_true = sum(map(total_name.count, ["t", "r", "u", "e"]))
count_love = sum(map(total_name.count, ["l", "o", "v", "e"]))

#if the below is not done, it throws a NoneType error. this is to concatinate the values after converting them into str
total = str(count_true) + str(count_love)

#Just an additional if-elif-else for a little drama. lol
if int(total) < 50:
      print(f"So the love calculator says the compatibility between you two is *{total} % \n"
      f"which means you guys might want to not consider this and walk your separate paths. :/ ")

elif 50 < int(total) < 80:
      print(f"So the love calculator says the compatibility between you two is *{total} % \n"
            f"which means you guys are pretty cool.! \n"
            f"Yay.!! Good Luck ;) ")
else:
      print(f"So the love calculator says the compatibility between you two is *{total} % \n"
      f"which means the sheets are always hot between you two .!! \n"
            f"Whaoooa You guys are the ABSOLUTE PERFECT MATCH :O <3 ")



#total_count = print(f"{count_name1}{count_name2}")

#count_name1 = name1_smaller.count("t") + name1_smaller.count("r") + name1_smaller.count("u") + name1_smaller.count("e")
#print((name1_smaller.count("") + name1_smaller.count("")).format(a,b))

