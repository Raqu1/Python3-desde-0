#!/usr/bin/python3

cont = 0
for var in range(1,6):
	num = int(input("Dime tu numero: "))
	if num % 2 == 0:
		cont = cont +1
print("Has introducido ",cont," numero pares")
