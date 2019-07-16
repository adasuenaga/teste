#!/usr/bin/python3



palavra = input ('Digite:')

vogais = 'aeiou'
troca =''

for k in palavra:
	if k in vogais:
		troca +=  '*'
	else:
		troca += k
				
print(troca)				

exit()
for k in palavra:
	if k in vogais:
		palavra = palavra.replace(k,'*')

print(palavra)



exit()


palavra = input ('Digite uma palavra:')

if palavra == palavra[::-1]:
	print ('Essa palavra é palindromo')
