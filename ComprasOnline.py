import necessarios as n
import time
from time import sleep

while True:
	n.menu()
	escolha = input()
	if(escolha == 'x'):
		break
	elif(int(escolha) not in range(0,10)):
		print()
		print("Opção inválida, por favor, tente novamente. Irei te redirecionar para o menu inicial.")
		print()
		time.sleep(5)
		continue
	else: 
		escolha = int(escolha)
		if(escolha == 1): 
			#Todos os pedidos associados a uma conta
			print("Ok! Vou apresentar os números das contas que temos para que você escolha uma e então apresento os pedidos associados a ela")
			print(n.select("num_conta", "conta"))
			conta_desejada = input()
			print(f"Os pedidos associados a {conta_desejada} são:")
			query = (f"SELECT * FROM pedido WHERE id_conta = '{conta_desejada}'")
			n.cursor.execute(query)
			listinha = n.cursor.fetchall()

		if(escolha == 2):
			#Todos os produtos contidos em um determinado carrinho de compras
			print()

		if(escolha == 3): #OK
			#Dados (e a quantidade) dos usu ́arios cadastrados no sistema
			print("Ótima escolha! Vamos ver os dados dos usuários e, ao final, a quantidade")
			time.sleep(3)
			listinha = n.select("*", "cliente")

			for linha in listinha:
				print("ID: ", linha[0])
				print("Nome completo: ", linha[1])
				print("CPF: ", linha[2])	
				print("Endereço: ", linha[3])
				print("CEP: ", linha[4])
				print("Bairro: ", linha[5])
				print("Cidade: ", linha[6])
				print("Estado: ", linha[7])
				print("Data de Nascimento: ", linha[8])
				print("Sexo: ", linha[9])
				print("Telefone: ", linha[10])
				print()
			quantidade = n.select_count("*", "cliente")
			time.sleep(2)
			print("Quantidade: ", quantidade)
			print("Deseja continuar? Digite s para voltar ao menu ou x para sair")
			opcao = input()
			if(opcao == 's'):
				continue
			else:
				break
		
		if(escolha == 4):
			#Forma de pagamento mais utilizada
			print()

		if(escolha == 5): #OK
			#Filtrar usuarios por bairro, cidade e estado
			print("Tá bem! Vamos por partes. De qual estado você deseja saber? Pode colocar apenas a sigla")
			time.sleep(2)
			estados = {'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas', 'BA': 'Bahia', 'CE': 'Ceará', 'ES': 'Espírito Santo', 'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'MG': 'Minas Gerais', 'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 'PE': 'Pernambuco', 'PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RS': 'Rio Grande do Sul ', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina', 'SP': 'São Paulo', 'SE': 'Sergipe', 'TO': 'Tocantins', 'DF': 'Distrito Federal',}
			for chave in estados.keys():
				print(f'{chave}: {estados[chave]}')
				#time.sleep(0.25)
			print("Digite a sigla:")
			sigla = input().upper()
			while(sigla not in estados):
				print("Acho que você digitou algo errado... Vamos tentar novamente?")
				sigla = input().upper()
			print()
			""" query = (f"SELECT bairro, cidade  FROM cliente WHERE estado = '{sigla}'")
			n.cursor.execute(query) """
		 	#listinha = n.cursor.fetchall()
			consulta = n.select("bairro, cidade", "cliente")
			print(consulta)
			listinha = n.select_filtro(consulta, "cliente", "estado", sigla)
			
			if(not listinha):
				print("Hm, desculpe, ainda não há clientes neste estado")
				print()
				print("Deseja continuar? Digite s para voltar ao menu ou x para sair")
				opcao = input()
				if(opcao == 's'):
					print()
					continue
				else:
					break
			else:
				print("Ok, agora vou apresentar as cidades e bairros disponíveis em", sigla)
				print()
				for linha in listinha:
					print("Bairro:", linha[0]," Cidade:", linha[1])
					print()
				print("Agora escolha a Cidade: ")
				cidade = input().capitalize()
				print()
				print("Ok! E o bairro: ")
				bairro = input().capitalize()
				print()
				query = (f"SELECT id_cliente, nome_completo, cpf, sexo, telefone FROM cliente WHERE bairro = '{bairro}' AND cidade = '{cidade}'")
				n.cursor.execute(query)
				users = n.cursor.fetchall()
				if(users):
					for linha in users:
						print("ID: ", linha[0])
						print("Nome completo: ", linha[1])
						print("Sexo: ", linha[2])
						print("Telefone: ", linha[3])
						print()
					print("Deseja continuar? Digite s para voltar ao menu ou x para sair")
					opcao = input()
					if(opcao == 's'):
						continue
					else:
						break
				else:
					print("Algo está errado, tente novamente!")
					print("Deseja continuar? Digite s para voltar ao menu ou x para sair")
					opcao = input()
					if(opcao == 's'):
						continue
					else:
						break

		if(escolha == 6):
			#Media anual de vendas
			print()
		
		if(escolha == 7):
			#Mes e ano com maior numero de vendas
			print()

		if(escolha == 8):
			#Usuarios que realizaram compras em todos os meses de um determinado ano
			print()

		if(escolha == 9):		
			#Outros tipos de consultas
			n.menu_adicionais()
			opcao = input()
			if(opcao == 'x'):
				break
			else:
				int(opcao)
				if(opcao == 1):
					#consulta adicional 1
					print()
				
				if(opcao == 2):
					#consulta adicional 2
					print()
				
				else:
					continue
		
		else:
			#Novo menu de manipulação
			n.menu_manipulacao()
			opcao = input()
			if(opcao == 'x'):
				break
			else:
				int(opcao)
				if(opcao == 1):
					#inserção
					print()
				
				if(opcao == 2):
					#atualização
					print()
				
				if(opcao == 3):
					#deleção
					print()
				
				else:
					continue
				