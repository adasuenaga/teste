#!/usr/bin/python3


nome = input ('Digite nome do aluno:')
nota1 = float(input ('Digite nota 1:'))
nota2 = float(input ('Digite nota 2:'))
nota3 = float(input ('Digite nota 3:'))
nota4 = float(input ('Digite nota 4:'))

media = (nota1+nota2+nota3+nota4)/4

if media >= 7:
	situacao = 'aprovado'
elif media >=5 and media < 7:
	notae = float(input('nota exame:'))
	media = (media+notae)/2
	if media >= 5:
		situacao = 'aprovado' 
	else:
		situacao = 'reprovado'   
else:
	situacao = 'reprovado'

print (nome.title() + ' tem a media ' + str(media) + ' - ' + situacao )

