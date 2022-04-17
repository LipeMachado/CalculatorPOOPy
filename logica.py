# ============================== Importações =================================

from math import sqrt, log

# ============================== Classes =================================


class Soma:
    def somar(primeiroValor, segundoValor):
        resultado = primeiroValor + segundoValor
        return f"Resultado da soma é: {resultado}"


class Subtracao:
    def subtracao(primeiroValor, segundoValor):
        resultado = primeiroValor - segundoValor
        return f"Resultado da subtração é: {resultado}"


class Multiplicacao:
    def multiplicacao(primeiroValor, segundoValor):
        resultado = primeiroValor * segundoValor
        return f"Resultado da multiplicação é: {resultado}"


class Divisao:
    def divisao(primeiroValor, segundoValor):
        resultado = primeiroValor / segundoValor
        return f"Resultado da divisão é: {resultado}"


class PotenciacaoQuadratica:
    def potenciacaoQuadratica(valor):
        resultado = valor ** 2
        return f"Resultado da potenciação quadratica é: {resultado}"


class PotenciacaoCubica:
    def potenciacaoCubica(valor):
        resultado = valor ** 3
        return f"Resultado da potenciação ao cubo é: {resultado}"


class RaizQuadrada:
    def raizQuadrada(valor):
        resultado = sqrt(valor)
        return f"Resultado da potenciação ao cubo é: {resultado}"


class RaizCubica:
    def raizCubica(valor):
        resultado = pow(valor, 1/3)
        return f"Resultado da potenciação ao cubo é: {resultado}"


class Logaritmo:
    def logaritmo(valor):
        resultado = log(valor)
        return f"Resultado da potenciação ao cubo é: {resultado}"
