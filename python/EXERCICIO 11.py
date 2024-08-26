import os
def limpa():
    os.system('cls')
limpa()

#11- Elaborar em Python uma agenda de Contatos. Um contato tem os seguintes atributos:
#nome, telefone e e-mail.
class Contato:#cria uma classe para os contatos
    def __init__(self, nome, endereco, email):
        #inicidor da classe contato
        self.nome = nome#atributo nome do contato
        self.endereco = endereco#atributo endereço do contato
        self.email = email#atributo email do contato
class Agenda:#cria uma classe para a agenda de contato
    def __init__(self):
        #iniciador da classe agenda
        self.contatos = []# cria uma lista vazia para armazenar os contatos
    def adicionar_contato(self, contato):
        #metodo para adicionar contato a agenda
        self.contatos.append(contato)#adiciona o contato a lista
    def remover_contato(self, contato):
        #metodo para remover o contato da agenda
        self.contatos.remove(contato)#remove o contato da agenda
    def listar_contatos(self):
        #metodo para lsitar os contatos da agenda
        for contato in self.contatos:#percorre a lsita de contatos
            print("Nome:", contato.nome)#imprime o nome do contato
            print("Endereço:", contato.endereco)#imprime o endereço do contato
            print("E-mail:", contato.email)#imprime o email do contato
agenda = Agenda() #cria uma nova lista vazia
#cria alguns contatos
contato1 = Contato("João", "Rua A, 123", "joao@example.com")
contato2 = Contato("Maria", "Rua B, 456", "maria@example.com")
#adiciona os contatos a agenda
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
#lista os contatos da agenda
agenda.listar_contatos()
#remove um contato da agenda
agenda.remover_contato(contato1)
#lista novamente os contatos
agenda.listar_contatos()