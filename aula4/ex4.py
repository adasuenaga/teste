#!/usr/bin/python3

class Conta():
	def __init__(self,titular,numero,saldo):
		self.titular = titular
		self.numero = numero
		self.saldo = saldo
	def descrever(self):
		print(('Titular: {}\n CC: {}\n' +
			'Saldo: {}\n').format(self.titular,self.numero,self.saldo))
	def saque(self,valor):
		self.saldo -= valor	
		return self.saldo
	def deposito(self,valor):
		self.saldo += valor	
		return self.saldo
	def transferir(self,valor,conta):
		self.saque(valor)
		conta.deposito(valor)

class Poupanca(Conta):
	def __init__(self,titular,numero,saldo):
		super().__init__(titular,numero,saldo)
		self.juros = 1.006
	def descrever(self):
		print(('Titular: {}\n Poupança: {}\n' +
			'Saldo: {}\n').format(self.titular,self.numero,self.saldo))
	def render(self):
		self.saldo *= self.juros
		return self.saldo