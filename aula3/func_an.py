#!/usr/bin/python3

# função anonima

t = (15,30,5,0)
print(t)

ft = list(map(lambda n : float(5/9)*(n-32), t))
ct = list(map(lambda n : float(9/5)*n+32, ft))

print('F: {}\nC: {}'.format(ft,ct))

exit()
##############################################

def temp_c(n):
	return (9/5)*n+32

def temp_f(n):
	return (5/9)*(n-32)

t = (15,30,5,0)
print(t)

ft = list(map(temp_f, t))
print(ft)

ct = list(map(temp_c, ft))
print(ct)

exit()

#############################################

def quadrado(n):
	return n**2

def raiz(n):
	return n ** (0.5)

f = [quadrado,raiz]

for k in range(0,26):
	valores = list(map(lambda x : x(k), f))
	print(valores)
print('\n')

[print(list(map(lambda x : x(k), 
	f))) for k in range(0,26)]


exit()

############################################

n1 = [1,2,3]
n2 = [4,5,6]

r = list(map(lambda x,y : x * y, n1, n2))

print(r)

exit()
#############################################

num = (1,2,3,4,5)
r = list(map(lambda n : 2 * n, num))
print(r)

exit()

#############################################

import math

l1 = [1,4,9,16,25]
l2 = list(map(math.sqrt, l1))

print(l2)

exit()

#############################################

def dobro(n):
	return 2 * n
num = (1,2,3,4,5)

r = map(dobro, num)
print(list(r))

exit()

##############################################

calcula = {'soma':lambda x,y : x + y,
			'subtracao':lambda x,y : x - y,
			'divisao':lambda x,y : x * y,
			'multiplicacao':lambda x,y : x / y}

funcao = calcula['soma']
print(funcao(10,3))
print(calcula['soma'](10,3))


exit()

#####################################################

frase = 'joao foi para a escola'.split()

tamanho = lambda frase : [len(palavra) for palavra in frase]
print(tamanho(frase))


################################################

def tamanho(frase):
	return [len(palavra) for palavra in frase]

frase = 'joao foi para a escola'.split()
print(tamanho(frase))


exit()

#################################################

def multiplica(n):
	return lambda a : a * n

dobro = multiplica(2)	
triplo = multiplica(3)

print(dobro(12))	
print(triplo(12))	

exit()

#################################################

x = lambda a,b : a + b

a = x(5,3)

print(a)

exit()

###############################################

def exemplo(a):
	return a+10

x = lambda a : a + 10	

print(x(5))

###############################################

def cadastra(par1,par2):
	return par1 + str(par2)

def busca():
	pass

a = 'joao'
b = 20
x = cadastra(a,b)
print(x)

