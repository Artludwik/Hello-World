#My first Project, 100 years old
input("This simple Program will calculate the year of your 100th birthday anniversary, please click ENTER to start the Program.")
import datetime
#The Program ask about user's name"
name = input("Give me your name: ")
#The Program ask about user's age"
age = int(input("How old are you?: "))
#The Program returns the year of 100th birthday anniversary
present = (datetime.datetime.now())
timeperiod = 100 - age
result = present.year + timeperiod
print(name + ", you will be 100 years old in " + str(result) + ".")
input("Calculations have been completed. Now the program can be closed.")
