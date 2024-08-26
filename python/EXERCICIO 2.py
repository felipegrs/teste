import os
def limpa():
    os.system("cls")
limpa()

#2- Elaborar um programa Python para criptografar uma string utilizando a cifra de César.
#pede e adiciona um valor ao deslocamento, texto e texto criptografado
#pede os deslocamento
deslocamento = int(input("Digite o deslocamento: "))
#pede o texto a ser criptografado
texto = input('Digite o texto a ser criptografado: ')
texto_criptografado = ''
#criptografa o texto
for letra in texto:
 if letra.isupper():
    letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)
 elif letra.islower():
    letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)
 else: letra_criptografada = letra 
 texto_criptografado += letra_criptografada
 #exibe os resultados
 print('Texto criptografado:', texto_criptografado)