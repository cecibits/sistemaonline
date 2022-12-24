import MySQLdb
import mysql.connector
from mysql.connector import Error

global cursor

def menu():
	print("Olá! Esse é o Sistema de Compras Online para Roupas. O que você deseja fazer?")
	#time.sleep(1)
	print("Se deseja consultar todos os pedidos associados a uma conta, digite 1.")
	#time.sleep(1)
	print("Se deseja consultar todos os produtos contidos em um determinado carrinho de compras, digite 2.")
	#time.sleep(1)
	print("Se deseja consultar todos os dados (e a quantidade) de usuários cadastrados no sistema, digite 3.")
	#time.sleep(1)
	print("Se deseja consultar a forma de pagamento mais utilizada, digite 4.")
	#time.sleep(1)
	print("Se deseja filtrar os usuários por bairro, cidade, estado, digite 5.")
	#time.sleep(1)
	print("Se deseja consultar a média anual de vendas, digite 6.")
	#time.sleep(1)
	print("Se deseja consultar mês e ano com maior número de vendas, digite 7.")
	#time.sleep(1)
	print("Se deseja consultar usuários que realizaram compras em todos os meses de um determinado ano, digite 8.")
	#time.sleep(1)
	print("Se deseja visualizar outros tipos de consulta, digite 9.")
	#time.sleep(1)
	print("Caso não deseje nenhuma das opções anteriores, digite 0 para ir ao novo menu.")
	#time.sleep(1)
	print("E se quiser sair, pode apertar a tecla x.")

def menu_manipulacao():
	print("Agora estamos no menu de manipulação")
	#time.sleep(1)
	print("Se deseja inserir novos dados, digite 1.")
	#time.sleep(1)
	print("Se deseja atualizar alguma informação, digite 2.")
	#time.sleep(1)
	print("Se deseja deletar algum dado, digite 3.")
	#time.sleep(1)
	print("Caso deseje voltar ao menu anterior, digite 0.")
	#time.sleep(1)
	print("E se quiser sair, pode apertar a tecla x.")

def menu_adicionais():
	print("Agora estamos em consultas adicionais")
	#time.sleep(1)
	print("Se deseja , digite 1.")
	#time.sleep(1)
	print("Se deseja , digite 2.")
	print("Caso deseje voltar ao menu anterior, digite 0.")
	#time.sleep(1)
	print("E se quiser sair, pode apertar a tecla x.")

try:
	#parametros do banco
	host = "localhost"
	user = "root"
	password = "password" #sem senha no note
	db = "Compras_Online" #trocar para o banco oficial
	port = 3306
	#conexão com o meu banco
	connection = MySQLdb.connect(host, user, password, db, port)
	if connection:
		#para realizar operações, conecto o cursor ao banco de dados para retorno das operações
		cursor = connection.cursor()

except Error as e:
	print("Erro na conexão: ", e)

#definindo função para filtragens
def filtro(tables, column, value):
	query = "SELECT * FROM %s WHERE %s = %s", (tables, column, value)
	cursor.execute(query)
	return cursor.fetchall()

#definindo função para campos específicos com filtragem
def select(fields, tables, where = None):
	query = "SELECT " + fields + " FROM " + tables #como todos são strings, posso concatenar na consulta
	if(where):
		query = query + " WHERE %s", filtro(tables, column, value)
	cursor.execute(query)
	return cursor.fetchall() #pego todos os resultados para retornar na função

#definindo função para utilizar o SELECT simples
def select(fields, tables, where = None):
	query = "SELECT " + fields + " FROM " + tables #como todos são strings, posso concatenar na consulta
	if(where):
		query = query + " WHERE %s = %s", (column, value)
	cursor.execute(query)
	return cursor.fetchall() #pego todos os resultados para retornar na função

#definindo função para contagem de tuplas
def select_count(fields, tables, where = None):
	query = "SELECT count(" + fields +") FROM " + tables
	if(where):
		query =  query + " WHERE " + where
	cursor.execute(query)
	quantidade = cursor.fetchone() #pego todos os resultados para retornar na função
	total = quantidade[0]
	return total

