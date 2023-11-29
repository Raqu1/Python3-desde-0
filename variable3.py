#!/usr/bin/python3

indicador = False;
for var in range(1,6):
	num = int(input("Dime tu numero: "))
	if num % 2 == 0:
		indicador = True
if indicador:
	print("Has introducido algun numero par")
else:
	print("No has introducido ningun numero par")
