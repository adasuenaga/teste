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

# joao_cc = Conta('joao','123', 30000)
# maria_cc = Conta('maria','222', 2000)
# joao_pp = Poupanca('joao','111', 100)

# joao_cc.transferir(3000,maria_cc)
# joao_cc.descrever()
# maria_cc.descrever()

# joao_cc.transferir(5000,joao_pp)
# joao_cc.descrever()
# joao_pp.descrever()

# joao_pp.render()
# joao_pp.descrever()

exit()

####################################################

class Conta():
	"""docstring for """

	def __init__(self, nome, saldo_cc, saldo_pp ):
		self.nome = nome
		self.saldo_cc = saldo_cc
		self.saldo_pp = saldo_pp

	def saque(self,saq,tipo):
		if tipo == 'cc':		
			self.saldo_cc -= saq
		else:
			self.saldo_pp -= saq			

	def deposito(self,dep,tipo):
		if tipo == 'cc':
			self.saldo_cc += dep
		else:
			self.saldo_pp += dep			

	def saldo_atual(self):
		print('{} seu saldo c/c = {}'.format(self.nome,str(self.saldo_cc)))
		print('{} seu saldo poupança = {}'.format(self.nome,str(self.saldo_pp)))


conta_corrente1 = Conta('joao',30,0)
conta_corrente2 = Conta('maria',2,0)

conta_corrente1.saque(3,'cc')
conta_corrente1.saque(5,'cc')
conta_corrente1.deposito(5,'pp')
conta_corrente1.saldo_atual()

conta_corrente2.deposito(3,'cc')
conta_corrente2.saldo_atual()

