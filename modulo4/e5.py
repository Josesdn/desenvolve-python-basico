quantidade=int(input("Digite a quantidade de respondente:"))
contador=0
soma=0
while contador<quantidade:
    idade=int(input("Digita a idade"))
    contador +=1
    soma +=idade
media=soma/quantidade
print(media)