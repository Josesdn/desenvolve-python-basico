
def obter_numeros():
    numeros = []
    while True:
        try:
            num = int(input("Digite um número inteiro (ou digite 'fim' para encerrar): "))
            numeros.append(num)
        except ValueError:
            if input("Digite 'fim' para terminar ou qualquer outra tecla para continuar: ").lower() == 'fim':
                break
    return numeros

numeros = obter_numeros()
if len(numeros) < 4:
    print("É necessário inserir pelo menos 4 números inteiros.")
else:
    print("\nLista original:", numeros)
    print("\nOs 3 primeiros elementos:", numeros[:3])
    print("\nOs 2 últimos elementos:", numeros[-2:])
    print("\nLista invertida:", numeros[::-1])
    print("\nElementos de índice par:", numeros[::2])
    print("\nElementos de índice ímpar:", numeros[1::2])

