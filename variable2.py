#!/usr/bin/python3

suma = 0
for var in range(1,6):
	num = int(input("Dime tu numero: "))
	if num % 2 == 0:
		suma = suma + num
print("La suma de los numeros pares es ",suma)
