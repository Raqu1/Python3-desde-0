#!/usr/bin/python3

cont = 0
posicion = 0
cad = input("Introduce una cadena: ")

#elimino la los posibles espacion que hayan en la cadena
cad = cad.strip()

#busco los espacios
posicion = cad.find(" ", posicion)

while posicion != -1:
	cont = cont + 1
	while cad[posicion + 1] == " ":
		posicion = posicion + 1
	posicion = cad.find(" ", posicion + 1)
print("La frase tiene" ,cont + 1, "palabras.")
