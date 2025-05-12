urls = [
    "www.google.com",
    "www.facebook.com",
    "www.amazon.com",
    "www.microsoft.com"
]

dominios = []

for url in urls:
    nome_dominio = url[4:-4]  
    dominios.append(nome_dominio)

print(dominios)