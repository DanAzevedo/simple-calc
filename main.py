import os
import sys


def calc(operator, x, y):
    cases = {
        "+": lambda a, b: print(f"{a} + {b} =", a + b),
        "-": lambda a, b: print(f"{a} - {b} =", a - b),
        "*": lambda a, b: print(f"{a} * {b} =", a * b),
        "/": lambda a, b: print(f"{a} / {b} =", a / b),
        "**": lambda a, b: print(f"{a} ** {b} =", a ** b),
    }
    return cases[operator](x, y)


def newOp():
    new = str(input("Deseja fazer outra operação? S/N: "))
    if new == "S" or new == "s":
        menu()
    elif new == "N" or new == "n":
        if new == "N" or new == 'n':
            op = str(input("Tem certeza que deseja sair? S/N: "))
            if op == "S" or op == 's':
                print("Saindo da calculadora...")
                sys.exit()
            else:
                menu()
    else:
        print("Opção inválida!")


def menu():
    os.system('clear')
    op = 1
    while op:
        print('========================================')
        print("0 : Soma ")
        print("1 : Subtração ")
        print("2 : Multiplicação ")
        print("3 : Divisão ")
        print("4 : Exponenciação ")
        print("9 : Sair")
        print('========================================')
        op = int(input('| : Escolha sua opção: '))

        if op == 0:
            print(calc("+", float(input("Priemiro número:\n")), float(input("Segundo número:\n"))))
            newOp()
        elif op == 1:
            print(calc("-", float(input("Priemiro número:\n")), float(input("Segundo número:\n"))))
            newOp()
        elif op == 2:
            print(calc("*", float(input("Priemiro número:\n")), float(input("Segundo número:\n"))))
            newOp()
        elif op == 3:
            print(calc("/", float(input("Priemiro número:\n")), float(input("Segundo número:\n"))))
            newOp()
        elif op == 4:
            print(calc("**", float(input("Priemiro número:\n")), float(input("Segundo número:\n"))))
            newOp()
        elif op == 9:
            op = str(input("Tem certeza que deseja sair? S/N: \n"))
            if op == "S" or op == 's':
                print("Saindo da calculadora...")
                sys.exit()
            else:
                menu()
        else:
            print("Opção inválida!")


menu()
