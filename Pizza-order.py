#Program to calculate bill of your final pizza order
'''
Key Points to remember:
1. variables are defined as we go further, to store the input and then the math takes place as per the stored values.
    But this can also be defined first and then let math work later. I guess. idk. check and update.
2. cost = 0 because we needed a var for cost additions
3. notice the indentations. the most imp. consumed most time because of it. understand why
    if needed, try making a flow chart of your requirement. it helps. like really.!
'''



print("Kindly choose your pizza and pay the bill as provided")

start = input("Do you want a pizza? Y or N: ")
#pizza_size = input("What size of Pizza do you want? \n For Large Pizza, Kindly enter 'L' \n For Medium Pizza, Kindly enter 'M' \n For Small Pizza, Kindly enter 'S' : ")
#chicken = input("Do you want chicken toppings? Kindly input Y or N :")
#cheese = input("Do you want extra cheese as an add on? Kindly input Y or N :")
cost = 0

#If you dont need pizza, jump to the last else condition.
if start == "Y":
    print("Wonderful, Kindly proceed")

    #Storing the Pizza size input into the variable pizza_store right before the size-condition starts and update cost.
    pizza_size = input("What size of Pizza do you want? \n For Large Pizza, Kindly enter 'L' \n For Medium Pizza, Kindly enter 'M' \n For Small Pizza, Kindly enter 'S' : ")
    if pizza_size == 'L':
        cost += 15
        print("You have chosen a Large pizza")

    elif pizza_size == 'M':
        cost += 10
        print("You have chosen a Medium pizza")

    elif pizza_size == 'S':
        cost += 5
        print("You have chosen a Small pizza")

    #Storing chicken condition here and update the cost again to the above updated cost value.
    chicken = input("Do you want chicken toppings? Kindly input Y or N :")
    if chicken == 'Y':
        cost += 3
    else:
        print("You have opted not to choose chicken toppings")

    #Storing cheese condition here and update the cost again to the above updated cost value.
    cheese = input("Do you want extra cheese as an add on? Kindly input Y or N :")
    if cheese == 'Y':
        cost += 1
    else:
        print("You have not opted for cheese add-ons")

else:
    print("Get lost")
    
#Now printing the latest and final updated cost value and printing it. Also notice the 'f' inside the print() fn.
print(f"Your bill is : Rs. {cost}/- \n kindly pay the bill and wait for your number :) ")

