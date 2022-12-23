import MySQLdb
import mysql.connector
from mysql.connector import Error

global cursor

try:
	#parametros do banco
	host = "localhost"
	user = "root"
	password = ""
	db = "realizacao_testes" #trocar para o banco oficial
	port = 3306
	#conexão com o meu banco
	connection = MySQLdb.connect(host, user, password, db, port)
	if connection:
		#para realizar operações, conecto o cursor ao banco de dados para retorno das operações
		cursor = connection.cursor()

except Error as e:
	print("Erro na conexão: ", e)

#definindo a função para utilizar o SELECT, passando os campos, as tabelas e, caso precise, a clausula WHERE
def select(fields, tables, where = None):
	global cursor
	query = "SELECT " + fields + " FROM " + tables #como todos são strings, posso concatenar na consulta
	if(where): #se where for != de none
		query =  query + " WHERE " + where
	cursor.execute(query)
	return cursor.fetchall() #pego todos os resultados para retornar na função

