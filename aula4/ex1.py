#!/usr/bin/python3



#####################################################
import time,random
from subprocess import run, PIPE
from datetime import datetime
from pasta.som import qual_nota

b = False

while b == False:
	f = random.randint(264,528)
	b = qual_nota(f)


exit()
####################################################
import time,random
from subprocess import run, PIPE
from datetime import datetime

r = run(['apt','install','-y','sl'],stdout=PIPE,
	stderr=PIPE)
#print(r)

r = run(['ls','-l'],stdout=PIPE,
	stderr=PIPE)
#print(r)

if r.returncode != 0:
	print('Deu ruim')
else:
	print('ok')

k = 0
while k != 505:
	 k = random.randint(100,999)
	 #print(k)

vogais = 'aeiouAEIOU'
print(random.choice(vogais))
time.sleep(5)
print(random.choice(vogais))

print(datetime.now())