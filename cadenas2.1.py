#!/usr/bin/python3

cad = input("Introduce una cadena: ")

while True:
	car = input("Introduce un caracter: ")
	if len(car) > 1:
		print("Me tienes que da un solo caracter")
	if len(car) == 1: break

print("En la cadena" ,cad, "aparecen" ,cad.count(car), "veces el caracter" ,car)
