def intercalar(lista1, lista2):#parametros das duas listas
    tam=min(len(lista1), len(lista2))#definir o tamanho
    listafinal=[]#lista intercalada

    for i in range(tam):#percorre os elementos da lista
        listafinal.append(lista1[i])
        listafinal.append(lista2[i]) 

    if len(lista1) > len(lista2):#para os casos de listas de tamanhos diferentes
        listafinal.extend(lista1[tam:])#vai do indice tam ate o final da lista
    else:
        listafinal.extend(lista2[tam:])

    return listafinal

def remdupl(listad):
    listafinal=[]

    for elemento in listad:
        if elemento not in listafinal:
            listafinal.append(elemento)
    return listafinal

lista1=[1, 3, 5, 7, 9]
lista2=[2, 4, 6, 8]
listad=[1, 2, 2, 4, 5, 7, 4, 9]

newlist=intercalar(lista1, lista2)
print(newlist)
listasemdupl=remdupl(listad)
print(listasemdupl)
