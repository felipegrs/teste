import os
def limpa():
    os.system('cls')
limpa()

#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
#calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar
#se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão
#escrever a mensagem 'Saldo Negativo'.

numeroDaConta = int(input("Informe o numero da conta: "))
saldo = float(input("Informe o saldo da conta: R$"))
debito = float(input("Informe o valor de debito da conta: R$"))
credito = float(input("Informe o valor de credito da conta: R$"))
status = 0 
saldoAtual = saldo - debito + credito
print("Numero da conta: ",numeroDaConta)
print("Seu saldo atual é de: R$",saldoAtual)
if saldoAtual>=0:
    print("Status da conta: Positivo")
else:
   print("Status da conta: Negativo")
