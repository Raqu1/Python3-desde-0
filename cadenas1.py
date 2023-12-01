#!/usr/bin/python3

cad = str(input("Introduce una cadena: "))
subcad = str(input("Introduce una subcadena: "))

if cad.startwith(subcad):
	print("La cadena empieza por la subcadena")
else:
	print("La cadena NO comienza con la subcadena")
