## **Hello!**  
##### Welcome to the explanation about the Simple-Calculator project! I did it as my first python project, and wanted to share with you!  
So first off all, let's see what is that calculator supposed to do:
1. Let you choose the type of the mathematical operation (addition, multiplication, etc).
2. Let you choose 2 numbers to the operation.
3. Give you the answer.
4. Ask if you want to do another operation.

This is pretty simple, and I plan to get in the future a calculator with visual things. But let's start coding!  
### Function One
So let's get the function number 1. To do that we just need some kind of explanation, showing each one of the symbols and their type of operations, and them let the person select which one of them use.
To show the symbols just do a normal print statement and you will be fine, in my case I just coded:  
``` python
print(""" Symbols for each operation:
Addition: +
Subtraction: -
Multiplication: *
Division: /
""")
# We use three quotation marks, to show them in separate lines!
```   
Now I will do a loop, using the python function:
```python 
while 
```
So basically we will do a variable, that you can name whatever you want, but I will name "isItNotChosen", after it lets make the code:
``` python
while isItNotChosen:
        symbol = str(input("Select an operation by typing its symbol: "))
        symbolList = ['-', '+', '*', '/']
        if symbol in symbolList:
            isItNotChosen = False
```   
What I am doing is say "While 'isItNotChosen' is true, ask the symbol, if the symbol is in the list 'symbolList', 'isItNotChosen' is false so you stop the loop", then you can get the symbol!  
So you finished the fuction one, congrats!  
### Function Two  
The function 2 is a bit more complicated them the one, for it we will need to get the numbers from the input, but check if they are really numbers and send an error message after it, so let's go!  
First, lets get the input, we can simply do it by using the input function, but in this case as we want an integer, lets put the input inside a parentheses, and right next to it, the int function, here is the code:  
``` python
number1 = int(input("What is the first number of your operation ?: "))
number2 = int(input("What is the second number of your operation ?: "))
```  
Now that we got the variable values, let's check if they are integers, and if not they will ask you again, I did that by using the functions try and except, here is the code:
``` python
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
```
What we are doing is say, "So, computer, think that the number is not a integer, and while its not try to ask the 2 numbers, now if you had the ValueError (the error that happens when the answer is not the specified in the input, in our case when its not a integer), you say that "This is not a number!", and as the number still not a integer, you ask again, but if there is no error, than the number is a integer, and you stop asking".  
You see? It's a little more complicated than the first, but you managed to get here, congratulations!  
### Function Three  
Now give the answer! To do it we check which symbol the var "symbol" has, and we relate it with the operation, by doing the math operation while printing!  
``` python
    if symbol == "+":
        print("The sum of their numbers is: ", number1 + number2)

    if symbol == "-":
        print("Subtracting your numbers is: ", number1 - number2)

    if symbol == "*":
        print("The multiplication of your numbers is: ", number1 * number2)

    if symbol == "/":
        print("The division of your numbers is: ", number1 / number2)
```  
We say "Hey, if the symbol that we got is '+' (for example), do the sum between number1 and number2"!  
### Function Four  
Then, we get to the final function, to do it I got a variable named "repeat" right after the symbols explanation in function one, and after it I got:
``` python
while repeat:
```  
And put inside this "while", all the code that we did after the "repeat" variable. And last but really not least, we do do this code:  
``` python
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
```
That says "The loop question is not answered, ask it, if it says No (in this case, if it has N), turn repeat to false, and the loop was answered, and if it says Yes (or it has any Y, or S), turn repeat to True, and the loop was answered, and if repeat is False, say 'Thanks for using the Ortsac Calculator 1.0!', but if the answer was not Yes, or No, the loop question was still no answered, so ask again".  
### Final  
Thanks for reading! It was really fun to write my first github README.md, I hope you understood the content, I am only 13 so it may be a little confusing, see ya!
