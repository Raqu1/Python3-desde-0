#!/usr/bin/python3

suma = 0
count = 0

while True:
	num = int(input("Numero (o para salir): "))
	suma = suma + num
	if num != 0:
		count = count + 1
	if num == 0:
		break
if count != 0:
	media = suma / count 	
else:
	media = 0

print("Suma: ",suma)
print("Media: ",media)
