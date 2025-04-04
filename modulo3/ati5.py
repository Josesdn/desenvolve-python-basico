genero=(input("Qual o seu gênero, M para masculino e F para feminino:"))
idade= int(input("Qual a sua idade?:"))
tempo= int(input("Qual o seu tempo de serviço em anos?:"))
a=(genero== 'M' and idade>=65) or (genero=='F' and idade>=60)
b= tempo >=30

c= idade>=60 and tempo >=25
pode_aposentar= a or b or c
print(a,b,c, pode_aposentar)
