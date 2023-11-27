#!/usr/bin/python3
horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minuto de salida: "))
segpartida = int(input("Segundo de partida: "))
segviaje = int(input("Tiempo que has tardado en segundos: "))
#Converitr las horas y minutos en segundos y sumarlas
seginicial = horapartida * 3600 + minpartida * 60 + segpartida;
#Mas los segundos que ha tardado el viaje
segfinal = seginicial + segviaje;
#Pasamos de vuelta de hora, minutos y segundos
horallegada = segfinal // 3600;
minllegada = (segfinal // 3600) % 60;
segllegada = (segfinal % 3600) % 60;
#Imprimir hora de llegada
print("Hora de llegada: ")
print(horallegada,":",minllegada,":",segllegada)
