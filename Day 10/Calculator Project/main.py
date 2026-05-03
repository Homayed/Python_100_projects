from distutils.command.config import config
from email.charset import add_alias


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


def calculator():
    num1 = int(input("first number?"))
    is_continue = True

    while is_continue:

        num2 = int(input("second number?"))
        operator = input("What's your chosen operator")
        result = dictionary[operator](num1, num2)
        print(result)
        conti = input("do you want to continue? Y/N")
        if conti == "Y":
            num1 = result
        else:
            is_continue = False
            calculator()


#Gets function from the dictionary key
calculator()

