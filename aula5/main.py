
import os
from funcoes import *

opcoes = {
	0:sair,
	1:busca,
	2:cadastro,
	3:atualizacao,
	4:delecao,
	5:cria_tabela,
	6:drop_tabela
}

while True:
	try:
		os.system('clear')
		menu - open('menu.txt').read()
		print (menu)
		opt = int(input("Digite opcao: "))
		opcoes[opt]()
		input('Pressione qualquer tecla para continuar')
	except KeyboardInterrupt:
		sair()
	except Exception as e:
		print(e)
