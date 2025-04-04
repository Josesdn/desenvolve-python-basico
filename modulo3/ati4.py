
personagem = (input("Qual o personagem escolhido? guerreiro, mago ou arqueiro:"))
pontos_forca= int(input("Qual a pontuação de força do personagem?:"))
pontos_magia= int(input("Qual a pontuação de magia do personagem?:"))
valido = (
    (personagem == "guerreiro" and pontos_forca >= 15 and pontos_magia <= 10) or
    (personagem == "mago" and pontos_forca <= 10 and pontos_magia >= 15) or
    (personagem == "arqueiro" and 5 < pontos_forca <= 15 and 5 < pontos_magia <= 15)
)
print("Pontos de atributo consistentes com a classe escolhida:", valido)