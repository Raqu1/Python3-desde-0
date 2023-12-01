#!/usr/bin/python3

import random
lista_numeros = []

#primer recorrido
for indice in range(1,11):
	lista_numeros.append(random.randint(1,10))

#segundo recorrido
for numero in lista_numeros:
	print(numero, " " ,numero ** 2, " " ,numero ** 3)
