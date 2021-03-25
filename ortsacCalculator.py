print("Ortsac Calculator 1.0!")

print(""" Symbols for each operation:
Addition: +
Subtraction: -
Multiplication: *
Division: /
""")

repeat = True

while repeat:
    isItNotChosen = True
    numberIsNotInt = True
    while isItNotChosen:
        symbol = str(input("Select an operation by typing its symbol: "))
        symbolList = ['-', '+', '*', '/']
        if symbol in symbolList:
            isItNotChosen = False

    while numberIsNotInt:
        try:
            number1 = int(
                input("What is the first number of your operation ?: "))
            number2 = int(
                input("What is the second number of your operation ?: "))
        except ValueError:
            print("This is not a number!")
        else:
            numberIsNotInt = False
    if symbol == "+":
        print("The sum of their numbers is: ", number1 + number2)

    if symbol == "-":
        print("Subtracting your numbers is: ", number1 - number2)

    if symbol == "*":
        print("A multiplicação dos seus números é: ", number1 * number2)

    if symbol == "/":
        print("The division of your numbers is: ", number1 / number2)

    notAnsweredLoop = True

    while notAnsweredLoop:
        loopCalc = str(
            input("Do you want to do another operation? Answer with Yes or No: "))
        if loopCalc in "nN":
            repeat = False
            notAnsweredLoop = False
        elif loopCalc in "yYSs":
            repeat = True
            notAnsweredLoop = False
    if repeat is False:
        print("Thanks for using the Ortsac Calculator 1.0!")
