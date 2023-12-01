#!/usr/bin/python3

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

if cad.find(subcad) > -1:
	input("La cadena contiene la subcadena.")
else:
	input("La cadena no contiene la subcadena.")

#otra forma

if subcad in cad:
	input("La cadena contiene la subcadena.")
else:
	input("La cadena no contiene la subcadena.")

