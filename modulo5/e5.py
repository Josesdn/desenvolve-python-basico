import emoji

print("Lista de Emojis disponíveis:")
print(":grinning_face: 😃")
print(":red_heart: ❤️")
print(":thumbs_up: 👍")
print(":face_with_tears_of_joy: 😂")
print(":thinking_face: 🤔")
print(":clapping_hands: 👏")
print(":fire: 🔥")

print("\nDigite sua frase usando os códigos dos emojis entre dois-pontos (:)!")
frase = input("Exemplo: Olá! Estou muito feliz hoje :grinning_face: :clapping_hands:\n\nDigite sua frase: ")

frase_emojizada = emoji.emojize(frase, language='alias')

print("\nFrase com emojis:")
print(frase_emojizada)
