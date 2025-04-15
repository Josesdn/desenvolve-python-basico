import random
import math
contador=0
n=int(input("Digite um número:"))

while contador<n:
    num = random.randint(0,100)
    print("o número gerado é:",num)
    contador+=1
    soma+=num
raiz = math.sqrt(soma)
print("A raiz quadrada dá soma dos valores é:",raiz)

