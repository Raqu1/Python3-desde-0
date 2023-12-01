#!/usr/bin/python3

nombres = []
edades = []

while True:
	nombre = input("Dime le nombre de un alumno: ")
	if nombre != "*":
		nombres.append(nombre)
		edades.append(int(input("Dime su edad: ")))
	if nombre == "*": break;

#calcula edad max
edad_max = max(edades)

#alumnos mayores de edad
print("Alumnos mayores de edad")
print("=======================")
for nombre,edad in zip(nombre,edades):
	if edad >= 18:
		print(nombre)

#alumnos mayores
print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombre,edades):
	if edad == edad_max:
		print(nombre)
