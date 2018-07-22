__author__ = 'Artur_Ulaszek'
number = int(input("Provide me a number to divide: "))
listRange = list(range(1,number+1))

divisorList = []

for number in listRange:
    if number % number == 0:
        divisorList.append(number)

print(divisorList)
