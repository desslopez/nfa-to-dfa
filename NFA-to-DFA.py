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
    item=item.strip('()').split(',')
    lista_edos.append(item)

print(lista_edos)
