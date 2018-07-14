#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
number = int(input("Dear User, please give a number: "))
mod = number % 2
if mod > 0:
    print("You piked an odd number")
else:
    print("You picked an even number")
input("The Program ended his computations, now it can be closed")
