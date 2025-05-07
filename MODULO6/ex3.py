import random
lista1=[]
lista2=[]
for i in range(20):
    num=random.randint(0,50)
    lista1.append(num)         
    lista2.append(num) 
num_comum= list(set(lista1) & set(lista2))
for num in set(lista1):
    print(f"Elemento {num} aparece {lista1.count(num)} vezes na lista1.")
for num in set(lista2):
    print(f"Elemento {num} aparece {lista2.count(num)} vezes na lista2.")
print("Lista 1",lista1)
print("Lista 2",lista2)
print("intersecção ordenada",num_comum)