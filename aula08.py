from aula07Televisao import Televisao
from aula07 import Calculadora
from aula08ContadorLetras import contador_letras


calculadora = Calculadora()
televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
print(calculadora.multiplicacao(50, 50))
lista = ['cachorro', 'gato', 'pato', 'elefante', 'mamute']
print(contador_letras(lista))