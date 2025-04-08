distancia=int(input("Digite a distancia dá entrega em KM:"))
peso=float(input("Digite o peso dá entrega em quilogramas:"))
if distancia <= 100:
    frete=peso
if 101 <= distancia <= 300:
    frete=peso*1.5
if distancia >300:
    frete=peso*2
if peso>10:
    frete=frete+10
print(f"Valor do frete: R${frete:.2f}")