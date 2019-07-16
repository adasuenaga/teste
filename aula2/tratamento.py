#!/usr/bin/python3

## exceções

arq = 'arquivo.txt'

nomes = ['Robin\n','Mulher Maravailha\n','Superman\n']

with open(arq,'a') as arquivo:
	arquivo.writelines(nomes)

with open(arq) as arquivo:
	linhas = arquivo.read()
		
print(linhas)


exit()

arq = 'arquivo.txt'

with open(arq,'a') as arquivo:
	arquivo.write('Lanterna verde\n')

with open('arquivo.txt') as arquivo:
	linhas = arquivo.read()
		
print(linhas)

exit()

arq = 'arquivo.txt'

with open(arq,'w') as arquivo:
	arquivo.write('Batman\n')


with open('arquivo.txt') as arquivo:
	linhas = arquivo.readlines()
		
print(linhas)

exit()

with open('arquivo.txt') as arquivo:
	for linha in arquivo:
		print(linha)

exit()

with open('arquivo.txt') as arquivo:
	conteudo = arquivo.read()
	print(conteudo)

exit()


arquivo = open('arquivo.txt')
print(arquivo.read())
arquivo.close()


exit()

while True:


	try:
		n1 = int(input('Digite:'))
		n2 = int(input('Digite:'))		
		r = n1/n
	except ZeroDivisionError as e:
		print('Impossivel dividir por zero!')
	except NameError as e:
		print('Variavel Inexistente')
	except ValueError as e:
		print('Digite Numeros!')
		break		
	else:
		print(r)	


exit()

try:
	print(5/0)
except Exception as e:	
#except ZeroDivisionError as e:
	print(e)


