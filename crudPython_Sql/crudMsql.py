import mysql.connector

## CONEXAO MYSQL

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="surf2596",
    database="super_mega",
)

cursor = conexao.cursor()


## CRUD

produto = "Leite"
valor = 3

comando = f' DELETE FROM vendas WHERE nomeProduto = "{produto}"' ## OBRIGATORIO PARA O CRUD
cursor.execute(comando) ## OBRIGATORIO
conexao.commit() ## edita o banco de dados (CREATE, UPDATE, DELETE)


cursor.close()

conexao.close()

# CREATE
"""
produto = "Leite"
valor = 4

conexao.commit() ## edita o banco de dados (create, update, delete)
comando = f'INSERT INTO vendas (nomeProduto, valor) VALUES ("{produto}", {valor})' ## OBRIGATORIO PARA O CRUD 
cursor.execute(comando) ## OBRIGATORIO
"""

## READ

"""
produto = "Leite"
valor = 4

comando = f'SELECT* FROM vendas' ## OBRIGATORIO PARA O CRUD
cursor.execute(comando) ## OBRIGATORIO
##conexao.commit() ## edita o banco de dados (create, update, delete)
resultado = cursor.fetchall() ## Ler uma tabela ou informacao do banco de dados (READ) -- SELECT 
print(resultado)"""

## update
"""
produto = "Leite"
valor = 3

comando = f'UPDATE vendas SET valor = {valor} WHERE nomeProduto = "{produto}"' ## OBRIGATORIO PARA O CRUD
cursor.execute(comando) ## OBRIGATORIO
conexao.commit() ## edita o banco de dados (CREATE, UPDATE, DELETE)"""


## DELETE 
"""
produto = "Leite"   
valor = 3

comando = f' DELETE FROM vendas WHERE nomeProduto = "{produto}"' ## OBRIGATORIO PARA O CRUD
cursor.execute(comando) ## OBRIGATORIO
conexao.commit() ## edita o banco de dados (CREATE, UPDATE, DELETE)"""