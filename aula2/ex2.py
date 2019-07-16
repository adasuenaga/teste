#!/usr/bin/python3

# calculadora +,-,*,/
# receber entrada pelo input
# 5 + 5







def soma(a,b):
	return a + b
def sub(a,b):
	return a - b
def mult(a,b):
	return a * b
def divisao(a,b):
	return a / b

operadores = '+-*/'
operacao = input('Digite: ')

for k in operacao:
	if k in operadores:
		o = k
		a,b = operacao.split(k)
		a = int(a)
		b = int(b)

dic = {'+':soma, '-':sub, '*':mult, '/':divisao}

z = dic[o](a,b)
print(z)

#if o == '+':
#	print(a+b)
#elif o == '-':
#	print(a-b)
#elif o == '*':
#	print(a*b)
#elif o == '/':
#	print(a/b)

exit()
#############################################################
def operacao(y):
	if y[1] == '+':
		resultado = int(y[0]) + int(y[2])
	elif y[1] == '-':
		resultado = int(y[0]) - int(y[2])
	elif y[1] == '*':
		resultado = int(y[0]) * int(y[2])
	elif y[1] == '/':
		resultado = int(y[0]) / int(y[2])
	return resultado

oper = input('digite operacao: ').split()

print(operacao(oper))

###################################################
