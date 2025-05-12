import random
lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:")
print(lista)

max_negativos = 0
indice_max_negativos = (0, 0)

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        negativos = sum(1 for x in lista[i:j] if x < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            indice_max_negativos = (i, j)
print(f"\nIntervalo com a maior quantidade de números negativos: {lista[indice_max_negativos[0]:indice_max_negativos[1]]}")

del lista[indice_max_negativos[0]:indice_max_negativos[1]]

print("\nLista após a deleção do intervalo:")
print(lista)
