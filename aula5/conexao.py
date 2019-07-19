
import psycopg2

try:
	con = psycopg2.connect('host=localhost'+
		' dbname=gotham user=batman' +
		' password=gotham123')
	cur = con.cursor()

except Exception as e:
	print('Erro {}'.format(e))