#!/usr/bin/python3

suma = 0
count = 0

num = int(input("Numero (o para salir): "))
while num != 0:
	suma = suma + num
	count = count + 1
	num = int(input("Numero (o para salir): "))

if count > 0:
	media = suma / count 	
else:
	media = 0

print("Suma: ",suma)
print("Media: ",media)
