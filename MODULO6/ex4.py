def receber_lista(nome_lista):
    tamanho = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {tamanho} elementos da {nome_lista}:")
    for i in range(tamanho):
        numero = int(input())
        lista.append(numero)
    return lista
lista1 = receber_lista("lista 1")
lista2 = receber_lista("lista 2")

lista_intercalada = []

min_len = min(len(lista1), len(lista2))

for i in range(min_len):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
lista_intercalada.extend(lista1[min_len:])
lista_intercalada.extend(lista2[min_len:])