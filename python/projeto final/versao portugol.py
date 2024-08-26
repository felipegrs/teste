import os
def limpa():
    os.system('cls')
limpa()
import time

print("Bem Vindo a Gedeon!")
print("Informe a opcao que deseja:")
opcao = int(input("[1]Informar o valor fixo dos gastos de passede onibus\n[2]Informar um valor personalizado dos gastos de passe de onibus\n"))
limpa()

match opcao:
    case 1:
        print("Valor gasto por passe: R$5,5")
        print("Valor gasto por dia: R$11")
        print("Valor gasto em media por mes: R$220")
        time.sleep(2)
        limpa()
        mes = 1
        valorPasseMensal = 220
        total = 0
        while mes <= 12:
            print(f"Valor gasto no {mes}º mes: R${valorPasseMensal}")
            total = total+valorPasseMensal
            time.sleep(0.5)
            if mes == 5:
                print("A partir do sexto mes o valor dos passe teve um aumento de 4,5%")
                aumento = valorPasseMensal*0.045
                valorPasseMensal = valorPasseMensal+aumento
                valorPasseMensal.__round__(2)
            mes+=1
        media = mes/12
        print(f"Media gasta por mes: R${media}")
        print(f"Valor gasto ao total no fim do ano: R${total}")
        print("Obrigado por usar nosso programa ;D")
    
    case 2:
        print("Obs.: Nosso programa irá calcular o seu gasto total com passe de ônibus no ano a partir\ndos dias em que você pegou ônibus no mês levando em consideração que gastou 2 passes por dia.\n-Valor do passe nos primeiros meses: R$5,50\n-Valor a partir do 6º mês (aumento de 4,5%): R$5.74 \n")
        dias = []
        mes = 1
        valorPasse = 5.5
        for i in range(13):
            diasUteis =  int(input(f"Quantos dias voce pegou onibus no {mes}º mes?"))
            dias.append(diasUteis)
            totalMes = valorPasse*diasUteis
            if dias > 31:
                print("Informe um valor valido")
                i-=1
            if mes == 5:
                aumento = valorPasse*0.045
                valorPasse = valorPasse+aumento
                valorPasse.__round__(2)
            i+=1
