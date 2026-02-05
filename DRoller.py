import random
from colorama import Fore, Style

operators = ["+", "-", "*", "/"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "d"]

def menu():
    print("+--------------Menu--------------+")
    print("1) Roll dices")
    print("2) Exit")
    print("+--------------------------------+")
    select = input()
    match int(select):
        case 1:
            dices()
        case 2:
            exit()

def dices():
    command = input("Introduce the comand:")

    #Commands
    match command:
        case "Exit" | "exit" | "e":
            menu()
            return
        case "Help" | "help" | "h":
            print(Fore.GREEN + "Syntaxis: (Number of sides+d+Number of sides of the dice) Example: 1d20 (1 dice of 20 sides)" + Style.RESET_ALL)
            print(Fore.GREEN + "You can add operations to the syntaxis for expecific resposes. Example: 1d20+3 (3 are added to the result)" + Style.RESET_ALL)
            print(Fore.GREEN + "Use the command 'exit' or 'e' to exit the dice roller" + Style.RESET_ALL)
            dices()
            return

    #Preparations
    search = command.find("d")
    long = len(command)
    position = -1

    if search < 1:
        print(Fore.RED + f"Syntax error, use 'help' or 'h' for more info" + Style.RESET_ALL)
        dices()
        return
    
    for character in command:
        if character not in operators and character not in numbers:
            print(Fore.RED + f"Invalid character, use 'help' or 'h' for more info" + Style.RESET_ALL)
            dices()
            return

    for i, character in enumerate(command):
        if character in operators:
            position = i
            break
    
    if position == -1:
        position = long

    #Data
    rolls = int(command[0:search])
    sides = int(command[search + 1:position])
    operation = command[position:long]

    if sides < 1:
        print(Fore.RED + f"You can't roll a dice with {sides} sides" + Style.RESET_ALL)
        dices()
        return

    #Text
    if rolls < 2:
        half1 = Fore.YELLOW + str(rolls) + Style.RESET_ALL + " dice of"
    else:
        half1 = Fore.YELLOW + str(rolls) + Style.RESET_ALL + " dices of"
    
    if sides < 2:
        half2 = Fore.YELLOW + str(sides) + Style.RESET_ALL + " side"
    else:
        half2 = Fore.YELLOW + str(sides) + Style.RESET_ALL + " sides"
    
    if len(operation) > 1:
        half3 = Fore.YELLOW + operation + Style.RESET_ALL
    else:
        half3 = ""
    
    print(f"You have rolled {half1} {half2} {half3}")

    #Rolls
    result = []
    total = 0
    for x in range(rolls):
        roll = random.randint(1, sides)
        result.append(roll)
        total = total + roll
    
    result.sort(reverse=True)
    total = operate(total, operation)
    
    print ("Your result is: " + str(result) + " Total: " + str(total))

    dices()

def operate(total, o):
    o = o + "+"
    operlist = []
    start = 0
    finish = 0
    
    for i, character in enumerate(o):
        if character in operators:
            finish = i
            if start != finish:
                operlist.append(o[start:finish])
            start = i

    for x in operlist:
        simb = x[0:1]
        num = int(x[1:len(x)])
        match simb:
            case "+":
                total = total + num
            case "-":
                total = total - num
            case "/":
                total = total / num
            case "*":
                total = total * num
            
    return int(total)

if __name__ == "__main__":
    menu()