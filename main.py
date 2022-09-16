from replit import clear
from art import logo


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("what is the first number? \n"))
    for operation in operations:
        print(operation)
        keep_on = True
    while keep_on:
        symbol = input("Choose a operation from the line above \n")
        num2 = float(input("what is the next number? \n"))
        cal_function = operations[symbol]
        answer = cal_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        if input(
                f"Type 'y' to contiue the Calculation with the {answer} and type 'n' to clear the current Calculation \n"
        ).lower() == "y":
            num1 = answer
        else:
            keep_on = False
            clear()
            calculator()


calculator()
