valor = int(input("Digite um valor:"))
notas_100= valor//100
valor %= 100

notas_50= valor//50
valor %= 50

notas_20= valor//20
valor %= 20

notas_10= valor//10
valor %= 10

notas_5= valor//5
valor %= 5

notas_2= valor//2
valor %= 2

notas_1= valor//1
valor %= 1

print(f"{notas_100} Notas(s) de 100")
print(f"{notas_50} Notas(s) de 50")
print(f"{notas_20} Notas(s) de 20")
print(f"{notas_10} Notas(s) de 10")
print(f"{notas_5} Notas(s) de 5")
print(f"{notas_2} Notas(s) de 2")
print(f"{notas_1} Notas(s) de 1")

