#!/usr/bin/python3

arq = 'arquivo.txt'

def cadastrar(**kwargs):
	with open(arq,'a') as arquivo:
		arquivo.write("{}\t{}\t{}\n".format(kwargs['cpf'],kwargs['nome'],kwargs['estado']))
		print('\nadicionado cadastro com sucesso')

def busca(cpf):
	dic = {}
	k = 0
	chaved = ['cpf','estado','nome']

	with open(arq,'r') as arquivo:
		for linha in arquivo:
			itens = linha.split('\t')

			itens[-1] = itens[-1][:-1]

			# for m in itens:
			# 	dic[chaved[k]] = m
			# 	k += 1
			# 	if k == 3:
			# 		k=0

			# if dic[chaved[0]] == cpf:
			# 	print('{}\t{}\t{}\n'.format(dic['cpf'],
			# 		dic['estado'],dic['nome']))
			# 	return dic
			# else:
			# 	print('nao encontrado')

			if itens[0] == str(cpf):
			 	print('{}\t{}\t{}\n'.format(itens[0],
			 		itens[1],itens[2]))
			 	break
		else:
			print('nao encontrado')



while True:

	opcao = int(input('Opções:\n0 - sair\n1 - cadastrar\n2 - buscar\n\nDigite a opção: '))

	if opcao == 0:
		print('saída')
		break

	elif opcao == 1:	
		print('cadastro')	
		lista = input ('digite \ nome-estado-cpf:').split(',')
		cadastrar(nome=lista[0],estado=lista[1],cpf=lista[2])

	elif opcao == 2:
		print('buscar')	
		busca(cpf=input('Digite cpf:'))	
