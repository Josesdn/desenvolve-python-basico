pares = [num for num in range(20, 51) if num % 2 == 0]
quadrados = [num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
div = [num for num in range(1, 101) if num % 7 == 0]
paridade = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]

print(f"Números pares entre 20 e 50: {pares}")
print(f"Quadrados dos números de 1 a 9: {quadrados}")
print(f"Números entre 1 e 100 divisíveis por 7: {div}")
print(f"Paridade dos números em range(0, 30, 3): {paridade}")

