import os
def limpa():
    os.system('cls')
limpa()

import sqlite3

#conecta ao banco de dados(ou cria um novo)
conn = sqlite3.connect('passagens_onibus.db')
cursor = conn.cursor()

#criaçao das tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuarios(
               UsuarioID INTEGER PRIMARY KEY AUTOINCREMENT,
               Nome TEXT NOT NULL,
               Email TEXT NOT NULL UNIQUE,
               Senha TEXT NOT NULL,
               Nivel INTEGER DEFAULT 1
    )              
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Compras(
               CompraID INTEGER PRIMARY KEY AUTOINCREMENT,
               UsuarioID INTEGER,
               DataCompra DATE NOT NULL,
               Valor DECIMAL(10,2) NOT NULL,
               FOREIGN KEY(UsuarioID) REFERENCES  Usuarios(UsuarioID)           
    )
''')

conn.commit

import hashlib
from datetime import datetime
#funçao para hash de senha
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
#funçao para adicionar usuario
def adicionar_usuario(nome, email, senha, nivel=1):
    senha_hashed = hash_senha(senha)
    try:
        cursor.execute('''
        INSERT INTO Usuarios(Nome, Email, Senha, Nivel)
                       values(?,?,?,?)
        ''',(nome, email, senha_hashed, nivel))
        conn.commit()
        print("Usuario adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: Email ja existe.")

#funçao para registrar compra
def registrar_compra(usuario_id, valor):
    data_compra = datetime.now().strftime('%d-%m-%Y')
    cursor.execute('''
    INSERT INTO Compras (UsuarioID, DataCompra, Valor)
                   VALUES(?,?,?)
    ''',(usuario_id, data_compra, valor))
    conn.commit()
    print("Compra registrada com sucesso.")
#funçao para calcular gastos
def calcular_gastos(usuario_id):
    cursor.execute('''
    SELECT SUM(Valor) FROM Compras WHERE UsuarioID = ?
    ''', (usuario_id))
    total_gasto = cursor.fetchone()[0]
    return total_gasto if total_gasto else 0.0
#funçao para listar usuarios
def listar_usuarios():
    cursor.execute('''
    select UsuarioID, Nome, Email, Nivel FROM Usuarios
    ''')
    return cursor.fetchall()

#funçao para obter ID do usuario pelo email
def obter_usuario_id(email):
    cursor.execute('SELECT UsuarioID FROM Usuarios WHERE Email = ?', (email))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None

#funcao interativa para adicionar novo usuario
def input_adicionar_usuario():
    nome = input("Digite o nome do usuario: ")
    email = input("Digite o email do usuario: ")
    senha = input("Digite a senha do usuario: ")
    nivel = input("Digite o nivel do usuario (padrão é 1): ") or 1
    adicionar_usuario(nome, email, senha, int(nivel))

def input_registrar_compra():
    email = input("Digite o email do usuario que fez a compra: ")
    usuario_id = obter_usuario_id(email)
    if usuario_id:
        valor = float(input("Digite o valor da compra: R$"))
        registrar_compra(usuario_id,  valor)
    else:
        print("Erro: Usuario não encontrado.")

#menu interativo
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo usuario")
        print("2. Registrar nova compra")
        print("3. Calcular gastos de um usuario")
        print("4. Listar todos os usuarios")
        print("5. Sair")
        opcao = input("Escolha uma opcao: ")
        limpa()
        if opcao == '1':
            input_adicionar_usuario()
        elif opcao == '2':
            input_registrar_compra()
        elif opcao == '3':
            email = input("Digite o email do usuario: ")
            usuario_id = obter_usuario_id(email)
            if usuario_id:
                total_gasto = calcular_gastos(usuario_id)
                print(f"Total gasto pelo usuario {email}: R${total_gasto:.2}")
            else:
                print("Erro: Usuario não encontrado.")
        elif opcao == '4':
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Nivel: {usuario[3]}")
        elif opcao == '5':
            break
        else:
            print("Opção invalida. Tente novamente.")

#executa o menu interativo
menu()

#fecha a conexão
conn.close
