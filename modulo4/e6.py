n= int(input("quantidade de experimentos:"))
contador=0
soma_sapo, soma_rato, soma_coelho =0,0,0
while contador<n:
    quant_animais= int(input("quantidade de animais usados:"))
    tipo=(input("Tipo de animal S,R,C :"))
    if tipo=='S':
        soma_sapo+=quant_animais
    elif tipo=='R':
        soma_rato +=quant_animais
    elif tipo=='C':
        soma_coelho+=quant_animais
    contador+=1
print("total de cobaias:",soma_coelho+soma_rato+soma_sapo)
print("total de ratos:",soma_rato)
print("total de coelhos",soma_coelho)
print("total de sapos:",soma_sapo)
