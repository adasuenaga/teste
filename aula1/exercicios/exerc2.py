#!/usr/bin/python3

# abaixo de 200 min cobra r$ 0.20 por min
# entre 200 e 400 min cobra R$ 0.18
# acima de 400 o preco é 0.15

minutos = int(input('minutos utilizados: '))

if minutos < 200:
	preco = 0.2
elif minutos <= 400:
	preco = 0.18
else:
	preco = 0.15

print ('Conta: R$ {:.2f}'.format(minutos*preco))


exit()
idade = int(input('Digite idade:'))

habilitacao = input ('Possui habilitacao:')

if habilitacao.lower().strip() == 'sim':
	habilitacao = True
if idade >= 18 and habilitacao == True:
	print('Pode dirigir')
else:
	print('Nao pode dirigir')	

exit()

velocidade = int(input('informe vel.:'))

if velocidade > 110:
	multa = (velocidade - 110) * 5
	print('multa: R$ {}'.format(multa))
