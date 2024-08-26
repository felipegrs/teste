import os
def limpa():
    os.system('cls')
limpa()
#12- Elaborar uma função para calcular o fatorial de um número 
# utilizando recursão comcauda.
# A recursão de cauda é um tipo especial de recursão, no qual não existe 
#processamento a ser feito depois deencerrada a chamada recursiva. Sendo assim,
# não é necessário guardar o estado do processamento no momento dachamada 
# recursiva.
def fatorial(n, resultado=1):
    '''
    Função que lê um número inteiro n >= 0 e imprime n!
    '''
    if n == 0 or n == 1: # caso base: se n e 0 ou 1, oa fatorial e 1
        return resultado#retorna o resultado 
    else: # passo recursivo: calcula o fatorial de n - 1 e acumula o resultado
        return fatorial(n - 1, n * resultado)#chamada recursiva com o n - 1 e o novo resultado
# Função principal
def main():
    n = int(input("Digite um número inteiro: "))#le o numero inteiro do usuario
    resultado = fatorial(n)#calcula o fatorial usando a funçao recursiva
    print(20*"#")#imprime uma linha de separaçao
    print("Fatorial:", resultado)#imprime o reultado do fatorial
    print(20*"#")#imprime outra linha de separaçao
    #chama a funçao principal
    if __name__ == "__main__":
        main()