#!/usr/bin/python3

herois = ['superman','batman','flash',
'mulher maravilha','robin','thor']

heroi = 'capitao america'

if heroi in herois:
	print('ta na lista')
else:
	print('nao ta na lista')	

for heroi in herois:
	print(heroi)

for k in range(1,10):
	print(k)	



exit()
valor = list(range(2,15))
print (valor)

soma = 0
n = 0
while n < len(valor):
	soma += valor[n]
	n += 1

print('Media: {}'.format(soma/len(valor)))	


exit()
herois = ['superman','batman','flash',
'mulher maravilha','robin','thor']

print(herois)
print(herois[1:4])
print(herois[:4])
print(herois[:4:2])
print(herois[1:-1])
print(herois[::-1])


exit()
herois.sort(reverse=True)
print(herois)
print(sorted(herois))
print(herois)


exit()

herois = ['superman','batman','flash','mulher maravilha']
print(herois, len(herois))

herois[2]= 'arqueiro verde'
print(herois, len(herois))

herois.insert(2,'robin')
print(herois, len(herois))

del herois[0]
print(herois, len(herois))

pop_herois = herois.pop()
print(pop_herois, herois, len(herois))

pop_herois = herois.pop(0)
print(pop_herois, herois, len(herois))

herois.remove('robin')
print(herois, len(herois))

herois.append('thor')
print(herois, len(herois))

herois = []
print(herois, len(herois))

