#!/usr/bin/python3

notas = []

for indice in range(1,6):
	while True:
		nota = int(input("Introduce la nota %d:" % indice))
		if nota >= 0 and nota <= 10: break
	notas.append(nota)

#mostrar resultado

print("Notas: ",end="")
for nota in notas:
	print(nota," ",end="")
print()
print("Nota media: ",sum(notas)/len(notas))
print("Nota max: ",max(notas))
print("Nota min: ",min(notas))
