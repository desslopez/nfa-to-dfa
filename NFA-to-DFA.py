#Desiree Lopez Ramirez A01371590
#Sandra Rodriguez Oseguera A01371995

import re

fname = input("Introduce el nombre del archivo: ")
file = open(fname, 'r')
estados = file.read().strip('{}').split('),')
file.close()
lista_edos=[]

for item in estados:
    #lista_edos.append(re.sub('[(,)]', '', item)) Si queremos tratarlo como string

    #Si queremos tratarlo como lista con listas dentro
    item = item.strip('()').split(',')
    lista_edos.append(item)

print(lista_edos)
lista_edos2 = [lista_edos[0]]

#para tener agrupadas todas las transiciones del mismo estado a otro con el mismo simbolo
for i in range(1,len(lista_edos)):
    flag=0
    for j in range(0,len(lista_edos2)):
        if ( lista_edos2[j][1] == lista_edos[i][1] and lista_edos2[j][0] == lista_edos[i][0]):
            lista_edos2[j][2]+=lista_edos[i][2]
            flag = 1
    if flag == 0:
        lista_edos2.append(lista_edos[i])

print (lista_edos2)