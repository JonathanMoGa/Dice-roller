import random
import colorama
from colorama import init, Fore, Back, Style

print("Introduce the comand:", end=" ")
comand = input()
#Preparations
search = comand.find("d")
long = len(comand)
#Data
rolls = comand[0:search]
introlls = int(rolls)
sides = comand[search + 1:long]
intsides = int(sides)

if introlls < 2:
    print ("You have rolled " + Fore.YELLOW + rolls + Style.RESET_ALL + " dice of " + Fore.YELLOW + sides + Style.RESET_ALL + " sides" )
else:
    print ("You have rolled " + Fore.YELLOW + rolls + Style.RESET_ALL + " dices of " + Fore.YELLOW + sides + Style.RESET_ALL + " sides")

#Rolls
result = []
for x in range(introlls):
    roll = random.randint(1, intsides)
    result.append(roll)

total = 0

for i in result:
    total = total + i

print ("Your result is: " + str(result) + " Total: " + str(total))