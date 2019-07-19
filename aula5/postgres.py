
import psycopg2

try:
	con = psycopg2.connect('host=localhost'+
		' dbname=gotham user=batman' +
		' password=gotham123')
	cur = con.cursor()

except Exception as e:
	print('Erro {}'.format(e))


# cur.execute('create table herois (id serial, '+
# 	'nome varchar, idade int);')

# cur.execute('insert into herois (nome,idade) '+
# 	'values (\'batman\',80);')
# cur.execute('insert into herois (nome,idade) '+
# 	'values (\'robin\',20);')
# cur.execute('insert into herois (nome,idade) '+
# 	'values (\'asa noturna\',30);')

# cur.execute('update herois set nome=\'asa notuna\' ' 
# 	+'where nome=\'asa noturna\';')

# cur.execute('delete from herois '
# 	+'where nome=\'asa notuna\';')

cur.execute('select * from viloes order by 1;');
#print(cur.fetchone())
for k in cur.fetchall():
	print(k)

#print(cur.fetchall())

con.commit()
cur.close()
con.close()
