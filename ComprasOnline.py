import necessarios as n

print("Olá! Esse é o Sistema de Compras Online para Roupas. O que você deseja fazer?")
print("Se deseja consultar todos os pedidos associados a uma conta, digite 1.")
print("Se deseja consultar todos os produtos contidos em um determinado carrinho de compras, digite 2.")
print("Se deseja consultar todos os dados (e a quantidade) de usuários cadastrados no sistema, digite 3.")
print("Se deseja consultar a forma de pagamento mais utilizada, digite 4.")
print("Se deseja filtrar os usuários por bairro, cidade, estado, digite 5.")
print("Se deseja consultar a média anual de vendas, digite 6.")
print("Se deseja consultar usuários que realizaram compras em todos os meses de um determinado ano, digite 7.")
print("Se deseja consultar a quantidade de itens em estoque, digite 8.")
print("Se deseja filtrar os produtos por masculino ou feminino, digite 9.")
print("Caso não seja nenhuma das opções anteriores, digite 0 para ir ao novo menu.")


print(n.select("nome, valor", "comprador", "id = 1"))

#Todos os pedidos associados a uma conta
#Todos os produtos contidos em um determinado carrinho de compras
#Dados (e a quantidade) de usuários cadastraos no sistema
#Forma de pagamento mais utilizada
#Filtrar usuários por bairro, cidade, estado
#Media anual de vendas
#Mês e ano com maior número de vendas
#Usuários que realizaram compras em todos os meses de um determinado ano