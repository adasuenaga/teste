#!/usr/bin/python3

class Carro():
	def __init__(self,marca,modelo,ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.hodometro = 0
		self.gasolina = 0
	def descrever(self):
		print('{} {} {}'.format(self.marca,self.modelo,self.ano,))

	def ler_hodometro(self):
		print('Este carro rodou {} km'.format(self.hodometro))

	def atualiza_hodometro(self,kms):
		if kms >= self.hodometro:
			self.hodometro = kms
		else:
			print('Nao é possivel diminuir km')

	def incrementa_hodometro(self,kms):
		if kms >= 0:
			self.hodometro += kms
		else:
			print('Nao é possivel diminuir km')

	def enche_tanque(self):
		self.gasolina = 100
		print('Gasolina: {}'.format(self.gasolina))

class Bateria():
	def __init__(self,bateria):
		self.bateria = bateria

	def descrever_bateria(self):
		print('Bateria: {}'.format(self.bateria))

	def calculo_distancia(self):
		calculo = self.bateria * 2
		print(('Esse carro possui {} Km/h' + 
			' de bateria').format(calculo))

class Eletrico(Carro):
	def __init__(self,marca,modelo,ano):
		super().__init__(marca,modelo,ano)
		self.bateria = Bateria(100)

	def descrever_bateria(self):
		print('Bateria: {}'.format(self.bateria))

	def enche_tanque(self):
		print('Esse carro é eletrico')

c1 = Carro('VW','fusca','1980')
c2 = Eletrico('Tesla','model s','2016')

print('c1: {}'.format(c1.gasolina))
c1.enche_tanque()
print('c1: {}'.format(c1.gasolina))

# c2.descrever_bateria()
# print('c2: {}'.format(c2.gasolina))
# c2.enche_tanque()
# print('c2: {}'.format(c2.gasolina))

c2.bateria.descrever_bateria()
c2.bateria.calculo_distancia()


exit()


class User():
	def __init__(self,nome,sobrenome,username,passwd):
		self.nome = nome
		self.sobrenome = sobrenome
		self.username = username
		self.passwd = passwd		
		self.tentativas = 0
	def descrever(self):
		print('{} {} '.format(self.nome,
			self.sobrenome))

	def saudacao(self):
		print('ola {} {}'.format(self.nome,self.sobrenome))

	def reseta_tentativas(self):
		self.tentativas = 0
		print('Tentativas: {}'.format(self.tentativas))		

	def incrementa_tentativas(self):
		self.tentativas += 1
		print('Tentativas: {}'.format(self.tentativas))

	def login(self,usuario,senha):
		if usuario == self.username and senha == self.passwd:
			print ('Logado com sucesso')
			self.reseta_tentativas()
		else:
				self.incrementa_tentativas()

resultado = User('adaine','suenaga','batman','robin')

while True:

	usuario = input('Usuário: ')
	senhas = input('Senha: ')
	resultado.login(usuario,senhas)

exit()

class Carro():
	def __init__(self,marca,modelo,ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.hodometro = 0
	def descrever(self):
		print('{} {} {}'.format(self.marca,self.modelo,self.ano,))

	def ler_hodometro(self):
		print('Este carro rodou {} km'.format(self.hodometro))

	def atualiza_hodometro(self,kms):
		if kms >= self.hodometro:
			self.hodometro = kms
		else:
			print('Nao é possivel diminuir km')

	def incrementa_hodometro(self,kms):
		if kms >= 0:
			self.hodometro += kms
		else:
			print('Nao é possivel diminuir km')

meu_carro = Carro('VW','fusca','1980')
meu_carro.descrever()
meu_carro.atualiza_hodometro(30000)
meu_carro.ler_hodometro()
meu_carro.incrementa_hodometro(100)
meu_carro.ler_hodometro()

exit()

class Restaurante():
	def __init__(self, nome, tipo, aberto):
		self.nome = nome
		self.tipo = tipo
		self.aberto = aberto

	def descrever(self):
		print(('{} é um Restaurante de ' +
			'comida {} e está {}').format(
			self.nome,self.tipo,self.aberto))		

	def status(self):
		if self.aberto == True:
			print('{} está aberto'.format(self.nome))
		else:
			print('{} está fechado'.format(self.nome))

primeiro = Restaurante('Mcdonalds','fast food',True)
segundo = Restaurante('Outback','australiana',False)
terceiro = Restaurante('Marianas','brasileira',True)

primeiro.descrever()
segundo.descrever()
terceiro.descrever()

primeiro.status()
segundo.status()
terceiro.status()

exit()

class Usuario():
	"""docstring for Cachorro"""

	def __init__(self, nome, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome

	def descrever(self):
		print('nome: {}\nsobrenome: {}'.format(self.nome,self.sobrenome))		

	def saudacao(self):
		print(' ola, {}'.format(self.nome)+' '+format(self.sobrenome))

usu = Usuario('gabriele','suenaga')
usu.descrever()
usu.saudacao()

exit()

class Cachorro():
	"""docstring for Cachorro"""
	dono = None

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def descrever(self):
		print('nome: {}\nidade: {}'.format(self.nome,self.idade))		

	def sentar(self):
		print('{} esta sentado'.format(self.nome))

	def rolar(self):
		print('{} esta rolando de um lado para o outro'.format(self.nome))

meu_cachorro = Cachorro('jake',2)
print('O dono é {}'.format(meu_cachorro.dono))
meu_cachorro.dono = 'joao'
print('O dono é {}'.format(meu_cachorro.dono))
meu_cachorro.descrever()
meu_cachorro.sentar()
meu_cachorro.rolar()

