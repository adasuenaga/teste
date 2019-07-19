import psycopg2

try:
	con = psycopg2.connect('host=localhost'+
		' dbname=gotham user=batman' +
		' password=gotham123')
	cur = con.cursor()

except Exception as e:
	print('Erro {}'.format(e))

def cadastrar(**kwargs):
	cur.execute("insert into usuarios (nome,cpf,estado) values ('"
	+kwargs['nome']+"',"+kwargs['cpf']+",'"+kwargs['estado']	+"');")	
	print('\nadicionado cadastro com sucesso')

def busca(**kwargs):
	cur.execute("select * from usuarios where nome='"+kwargs['nome']+"';")
	print(cur.fetchall())

def deletar(**kwargs):
	cur.execute("delete from usuarios where nome='"+kwargs['nome']+"';")
	print('\nexcluido com sucesso')	

while True:

	opcao = int(input("Opções:\n0. Sair\n1.Buscar pelo nome\n2.Cadastrar\n3.Atualizar\n4.Deletar\n5.Criar tabela 'usuarios'\n6.Dropar tabela 'usuarios'\n7.Lista tabela\nOpção: "))

	if opcao == 0:
		cur.close()
		con.close()
		break

	elif opcao == 1:
		busca(nome=input('Digite nome:'))	

	elif opcao == 2:	
		print('cadastro')	
		lista = input ('digite \ nome-cpf-estado:').split(',')
		cadastrar(nome=lista[0],cpf=lista[1],estado=lista[2])

	elif opcao == 3:	
		con.commit()

	elif opcao == 4:
		deletar(nome=input('Digite nome:'))	

	elif opcao == 5:
		cur.execute('create table usuarios (nome varchar, '+
		'cpf int, estado varchar);')
		print('\ntabela criada com sucesso')	

	elif opcao == 6:
		cur.execute('drop table usuarios;')
		print('\ntabela excluida com sucesso')	

	elif opcao == 7:
		cur.execute("select * from usuarios;")
		print(cur.fetchall())
