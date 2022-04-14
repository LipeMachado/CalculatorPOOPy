# -*- coding: utf-8 -*-
from os import system
from os import sys
from math import sqrt, log


class Calculadora:
    def __init__(self):
        self.limparTela()
        self.menuOpcoes()

    def limparTela(self):
        system("cls || clear")

    def menuOpcoes(self):
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

        opcao = int(input("Informe um número de 0 a 9: "))

        if opcao == 1:
            primeiroValor = float(input("\nInsira o primeiro valor: "))
            segundoValor = float(input("Insira o segundo valor : "))

            print(self.somar(primeiroValor, segundoValor))
            self.menuOpcoes()

        elif opcao == 2:
            primeiroValor = float(input("\nInsira o primeiro valor: "))
            segundoValor = float(input("Insira o segundo valor : "))

            print(self.subtracao(primeiroValor, segundoValor))
            self.menuOpcoes()

        elif opcao == 3:
            primeiroValor = float(input("\nInsira o primeiro valor: "))
            segundoValor = float(input("Insira o segundo valor : "))

            print(self.multiplicacao(primeiroValor, segundoValor))
            self.menuOpcoes()

        elif opcao == 4:
            primeiroValor = float(input("\nInsira o primeiro valor: "))
            segundoValor = float(input("Insira o segundo valor : "))

            print(self.divisao(primeiroValor, segundoValor))
            self.menuOpcoes()

        elif opcao == 5:
            valor = float(input("\nInsira o valor: "))

            print(self.potenciacaoQuadratica(valor))
            self.menuOpcoes()

        elif opcao == 6:
            valor = float(input("\nInsira o valor: "))

            print(self.potenciacaoCubica(valor))
            self.menuOpcoes()

        elif opcao == 7:
            valor = float(input("\nInsira o valor: "))

            print(self.raizQuadrada(valor))
            self.menuOpcoes()

        elif opcao == 8:
            valor = float(input("\nInsira o valor: "))

            print(self.raizCubica(valor))
            self.menuOpcoes()

        elif opcao == 9:
            valor = float(input("\nInsira o valor: "))

            print(self.logaritmo(valor))
            self.menuOpcoes()

        elif opcao == 0:
            sys.exit()

    def somar(self, primeiroValor, segundoValor):
        self.resultado = primeiroValor + segundoValor
        return f"Resultado da soma é: {self.resultado}"

    def subtracao(self, primeiroValor, segundoValor):
        self.resultado = primeiroValor - segundoValor
        return f"Resultado da subtração é: {self.resultado}"

    def multiplicacao(self, primeiroValor, segundoValor):
        self.resultado = primeiroValor * segundoValor
        return f"Resultado da multiplicação é: {self.resultado}"

    def divisao(self, primeiroValor, segundoValor):
        self.resultado = primeiroValor / segundoValor
        return f"Resultado da divisão é: {self.resultado}"

    def potenciacaoQuadratica(self, valor):
        self.resultado = valor ** 2
        return f"Resultado da potenciação quadratica é: {self.resultado}"

    def potenciacaoCubica(self, valor):
        self.resultado = valor ** 3
        return f"Resultado da potenciação ao cubo é: {self.resultado}"

    def raizQuadrada(self, valor):
        self.resultado = sqrt(valor)
        return f"Resultado da potenciação ao cubo é: {self.resultado}"

    def raizCubica(self, valor):
        self.resultado = pow(valor, 1/3)
        return f"Resultado da potenciação ao cubo é: {self.resultado}"

    def logaritmo(self, valor):
        self.resultado = log(valor)
        return f"Resultado da potenciação ao cubo é: {self.resultado}"


if __name__ == '__main__':
    Calculadora()
