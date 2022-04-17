# -*- coding: utf-8 -*-

# ============================== Importações =================================

from os import system
from os import sys
from math import sqrt, log

# ============================== Classes =================================


class MenuOpcoes():

    def limparTela():
        system("cls || clear")

    def tabela():
        print("===================================\n"
              "|            0 - Sair             |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|            1 - Soma             |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|          2 - Subtração          |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|        3 - Multiplicação        |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|           4 - Divisão           |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|  5 - Elevar número ao quadrado  |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|    6 - Elevar número ao cubo    |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|        7 - Raiz quadrada        |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|         8 - Raiz cúbica         |\n"
              "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\n"
              "|          9 - Logaritmo          |\n"
              "===================================\n")


class Logica():

    def somar(primeiroValor, segundoValor):
        resultado = primeiroValor + segundoValor
        return f"Resultado da soma é: {resultado}"

    def subtracao(primeiroValor, segundoValor):
        resultado = primeiroValor - segundoValor
        return f"Resultado da subtração é: {resultado}"

    def multiplicacao(primeiroValor, segundoValor):
        resultado = primeiroValor * segundoValor
        return f"Resultado da multiplicação é: {resultado}"

    def divisao(primeiroValor, segundoValor):
        resultado = primeiroValor / segundoValor
        return f"Resultado da divisão é: {resultado}"

    def potenciacaoQuadratica(valor):
        resultado = valor ** 2
        return f"Resultado da potenciação quadratica é: {resultado}"

    def potenciacaoCubica(valor):
        resultado = valor ** 3
        return f"Resultado da potenciação ao cubo é: {resultado}"

    def raizQuadrada(valor):
        resultado = sqrt(valor)
        return f"Resultado da potenciação ao cubo é: {resultado}"

    def raizCubica(valor):
        resultado = pow(valor, 1/3)
        return f"Resultado da potenciação ao cubo é: {resultado}"

    def logaritmo(valor):
        resultado = log(valor)
        return f"Resultado da potenciação ao cubo é: {resultado}"


class Calculadora():
    def __init__(self):
        rodando = True

        while rodando != False:

            MenuOpcoes.tabela()
            opcao = int(input("Informe um número de 0 a 9: "))
            MenuOpcoes.limparTela()

            if opcao == 1:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Logica.somar(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 2:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Logica.subtracao(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 3:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Logica.multiplicacao(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 4:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Logica.divisao(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 5:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(Logica.potenciacaoQuadratica(valor))
                print("===================================\n")

            elif opcao == 6:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(Logica.potenciacaoCubica(valor))
                print("===================================\n")

            elif opcao == 7:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(Logica.raizQuadrada(valor))
                print("===================================\n")

            elif opcao == 8:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(Logica.raizCubica(valor))
                print("===================================\n")

            elif opcao == 9:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(Logica.logaritmo(valor))
                print("===================================\n")

            elif opcao == 0:
                sys.exit()
                rodando = True


class Historico():
    def historico(self):
        self.teste


if __name__ == '__main__':
    Calculadora()
