#!/usr/bin/python3

class Circulo():
	def __init__(self,centro,radio):
		self.radio=radio
		self.centro=centro

	def mostrar(self):
		return "Centro{0}-Radio:{1}".format(self.centro.mostrar(),self.radio)
