#!/usr/bin/python3

resultado = 1

num = int(input("Dime tu numero: "))
contador = 2;
while contador <= num:
	resultado = resultado * contador;
	contador = contador +1;
print("El resultado es ",resultado)
