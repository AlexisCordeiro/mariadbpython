import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'admin',
  'password': 'auladb1',
  'host': '172.31.23.1',
  'database': 'africa'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
    
while True:
    # Menu de opções
    print("Selecione uma opção:")
    print("1 - Cadastrar animal")
    print("2 - Editar animal")
    print("3 - Consultar animal")
    print("4 - Deletar animal")
    print('0 - Sair')

    # Obter a escolha do usuário
    opcao = input("Opção: ")


    # Definir as funções
    def cadastrar_animal():
        # Obter informações do animal a ser cadastrado
        raca = input("Raça: ")
        quantidade = input("Quantidade: ")
        risco_extincao = input("Risco de extinção (s/n): ")
        area = input("Localização (norte/sul/leste/oeste): ")

        # Executar consulta SQL para cadastrar o animal
        cursor = conn.cursor()
        query = "INSERT INTO animais_nativos (raca, quantidade, risco_extincao, area) VALUES (%s, %s, %s, %s)"
        values = (raca, quantidade, risco_extincao, area)
        cursor.execute(query, values)

        # Commit para salvar as alterações no banco de dados
        conn.commit()

        # Obter o ID do animal recém-cadastrado
        id_animal = cursor.lastrowid

        # Informar ao usuário que o animal foi cadastrado com sucesso
        print(f"Animal cadastrado com sucesso! ID do animal: {id_animal}")
    
    def editar_animal():
        # Obter informações do animal a ser editado
        id_animal = input("ID do animal a ser editado: ")
        raca = input("Raça: ")
        quantidade = input("Quantidade: ")
        risco_extincao = input("Risco de extinção (s/n): ")
        area = input("Localização (norte/sul/leste/oeste): ")

        # Executar consulta SQL para editar o animal
        cursor = conn.cursor()
        query = "UPDATE animais_nativos SET raca = %s, quantidade = %s, risco_extincao = %s, area = %s WHERE id_animal = %s"
        values = (raca, quantidade, risco_extincao, area, id_animal)
        cursor.execute(query, values)

        # Commit para salvar as alterações no banco de dados
        conn.commit()

        # Informar ao usuário que o animal foi editado com sucesso
        print("Animal editado com sucesso!")
    def consultar_animais():
        # Executar consulta SQL para obter todos os animais cadastrados
        cursor = conn.cursor()
        query = "SELECT * FROM animais_nativos"
        cursor.execute(query)

        # Exibir os resultados da consulta
        result = cursor.fetchall()
        for animal in result:
            print(animal)

    def deletar_animal():
        # Obter o ID do animal a ser deletado
        id_animal = input("ID do animal a ser deletado: ")

        # Executar consulta SQL para deletar o animal
        cursor = conn.cursor()
        query = "DELETE FROM animais_nativos WHERE id_animal = %s"
        values = (id_animal,)
        cursor.execute(query, values)

        # Commit para salvar as alterações no banco de dados
        conn.commit()

        # Verificar se o animal foi deletado com sucesso
        if cursor.rowcount == 1:
            print("Animal deletado com sucesso!")
        else:
            print("Animal não encontrado.")

    # Executar código correspondente à escolha do usuário
    if opcao == "1":
        cadastrar_animal()
    elif opcao == "2":
        editar_animal()
    elif opcao == "3":
        consultar_animais()
    elif opcao == "4":
        deletar_animal()
    elif opcao == '0':
        print("Programa encerrado.")
    break
else:
    print('Opção inválida!')

conn.close()







