# main.py

# This is a simple Hello World program
print("Hello, World!")

# Abrindo o arquivo e lendo seu conteúdo em uma lista
with open(aleatorio_1k, 'r') as file:
    linhas = file.readlines()

# Removendo caracteres de nova linha
linhas = [linha.strip() for linha in linhas]

print(linhas)

