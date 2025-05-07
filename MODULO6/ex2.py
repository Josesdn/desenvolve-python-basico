import random
elementos=[]
num_elementos = random.randint(5,20)
for i in range(num_elementos):
   elementos.append[random.randint(1,10)]
soma = sum(elementos)
media = soma / len(elementos)

print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", media)