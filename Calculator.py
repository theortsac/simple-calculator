print("Calculadora Ortsac versão 1.0!")

print(""" Símbolos para cada operação:
Adição: +
Subtração: -
Multiplicação: *
Divisão: /
""")

repeat = True

while repeat:
    isItNotChosen = True
    numberIsNotInt = True
    while isItNotChosen:
        symbol = str(input("Selecione uma operação digitando o seu símbolo: "))
        symbolList = ['-', '+', '*', '/']
        if symbol in symbolList:
            isItNotChosen = False
            while numberIsNotInt:
                try:
                    number1 = int(
                        input("Qual o primeiro número da sua operação?: "))
                    number2 = int(
                        input("Qual o segundo número da sua operação?: "))
                except ValueError:
                    print("Isso não é um número!")
                else:
                    numberIsNotInt = False
    if symbol == "+":
        print("A soma dos seus números é: ", number1 + number2)

    if symbol == "-":
        print("A subtração dos seus números é: ", number1 - number2)

    if symbol == "*":
        print("A multiplicação dos seus números é: ", number1 * number2)

    if symbol == "/":
        print("A divisão dos seus números é: ", number1 / number2)

    naoRespondidoLoop = True

    while naoRespondidoLoop:
        loopCalc = str(
            input("Você quer fazer outra operação? Responda com Sim ou Não: "))
        if loopCalc == "Não":
            repeat = False
            naoRespondidoLoop = False
        elif loopCalc == "Sim":
            repeat = True
            naoRespondidoLoop = False
    if repeat is False:
        print("Obrigado por usar a calculadora Ortsac!")
