import os
def limpa():
    os.system('cls')
limpa()

#exemplo 3: construindo um vetor e imprimindo seus elementos via um apontador
import copy
def copiar(ist_tpl):#funcao para copiar elemnetos de lista/tupla gerando lista nova
    lista=[]
    for item in ist_tpl : lista.append(item)
    return lista

lista = [1,2,[3]]#define lista com 3 elementos, sendo o terceiro uma lista com 1 elemento
aux = lista
aux[2] = -1#alterou lista[2]
print("Lista: lista = %s"%lista)

lista = [1,2,[3]]#lista
print("Lista: lista = %s"%lista)
aux1 = copy.copy(lista)#copiar com funcao "copy(.)" de biblioteca "copy"
aux2 = list(lista)#copiar com gerar de lista "list(.)"
aux3 = copiar(lista)#copiar com funcao local "copiar(.)"

aux1[2] = -1 #NAO alterou lista[2]
aux2[2] = -1 #NAO alterou lista[2]
aux3[2] = -1 #NAO alteoru lista[2]
print("aux1=%s, lista=%s"%(aux1, lista))
print("aux2=%s, lista=%s"%(aux2, lista))
print("aux3=%s, lista=%s"%(aux3, lista))

tupla = [1,2,[3]]#tupla
print("Tupla: tuopla = %s"%tupla)
aux1 = copy.copy(tupla)#usar funcao 'copy' de biblioteca 'copy'
aux2 = list(tupla)
aux3 = copiar(tupla)
print("aux1=%s, tupla=%s"%(aux1, tupla))
print("aux2=%s, tupla=%s"%(aux2, tupla))
print("aux3=%s, tupla=%s"%(aux3, tupla))
