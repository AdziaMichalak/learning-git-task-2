print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

x = int(input("Insert the first number:"))
y = int(input("Insert the second number:"))
z = input("What type of operator you want to use(+,-,*,/,**)")

operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}

if z == "+":
    print(operators["+"])
elif z == "-":
    print(operators["-"])
elif z == "*":
    print(operators["*"])
elif z == "/":
    print(operators["/"])
elif z == "**":
    print(operators["**"])
else:
    print("Error: operator not found(make sure you used the designated operators)")

import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything