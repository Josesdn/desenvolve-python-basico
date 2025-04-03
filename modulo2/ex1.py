largura= int(input ("Diga a largura do terreno em numeros inteiros:"))
comprimento = int(input ("Diga o comprimento do terreno em numeros inteiros:"))
preco_m2= float(input("preço do metro quadrado da região:" ))
area_m2= largura*comprimento
preco_total=preco_m2*area_m2
print(f"o terreno {area_m2}M2 e custa {preco_total}")

