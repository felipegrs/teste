import os
def limpa():
    os.system('cls')
limpa()

#exemplo 2: trabalhamos com "strings". uma "string" fixa e digita uma frase, imprimindo o numero de caracteres nela
string = "0123456789abcdefghikj"#(1)
#impriir cada caractere da string em seu codigo ASCII
print("\nImprime caracteres em seu codigo ASCII na forma de tabela\n coluna=1 => caractere; coluna2 => seu codigo ASCII")
for char in string: #iterator
    print("%20c:%3d"%(char,ord(char)))#funçao ord(.) devolve codigo ASCII do caractere parametro
print(); #quebre a linha

#agora uma entrada de dados via teclado e pegando uma frse como "string" (o ENTER finaliza a frase)
print("Digite uma frase e tecle ENTER/CR")
string=input()#se usar python 2 precisa trocar 'input' por 'raw_input'
print("Foi digitada uma frase com %d caracteres: %s" % (len(string),string))
#observacao: se definiu um vetor como 'string' como em (1) acima, NAO e possivel alterar a 'string', por exemplo,
#o comando abaixo resulta erro 'TypeError: 'str' object does not support item assignment'
#string[2] = '+'#isso resultaria erro! experimente
