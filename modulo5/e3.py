import random

while True:
    num=random.randint(1,10)
    palpite=int(input("Adivinhe um número de 1 a 10:"))
    if palpite<num:
        print("palpite baixo")
    elif palpite>num:
        print("Palpite alto")
    else:
        print("Parabens, você acertou!!")
        break