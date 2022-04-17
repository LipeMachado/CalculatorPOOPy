# ============================== Importações =================================

from os import sys
from os import system
from logica import *

# ================================ Classes ====================================


class Tabela:
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


class LimparTela:
    def limparTela():
        system("cls || clear")


class Main:
    def escolhasInput():
        rodando = True

        while rodando != False:

            Tabela.tabela()
            opcao = int(input("Informe um número de 0 a 9: "))
            LimparTela.limparTela()

            if opcao == 1:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Soma.somar(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 2:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Subtracao.subtracao(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 3:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Multiplicacao.multiplicacao(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 4:
                primeiroValor = float(input("\nInsira o primeiro valor: "))
                segundoValor = float(input("Insira o segundo valor : "))

                print("===================================")
                print(Divisao.divisao(primeiroValor, segundoValor))
                print("===================================\n")

            elif opcao == 5:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(PotenciacaoQuadratica.potenciacaoQuadratica(valor))
                print("===================================\n")

            elif opcao == 6:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(PotenciacaoCubica.potenciacaoCubica(valor))
                print("===================================\n")

            elif opcao == 7:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(RaizQuadrada.raizQuadrada(valor))
                print("===================================\n")

            elif opcao == 8:
                valor = float(input("\nInsira o valor: "))

                print("===================================")
                print(RaizCubica.raizCubica(valor))
                print("===================================\n")

            elif opcao == 9:
                valor = float(input("\nInsira o valora: "))

                print("===================================")
                print(Logaritmo.logaritmo(valor))
                print("===================================\n")

            elif opcao == 0:
                sys.exit()
                rodando = True
