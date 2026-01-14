import random

print("🔑  Gerador de Chave")

lyrics = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

todos_caracteres = lyrics + lyrics.upper() + numbers

tamanho = int(input("Quantos caracteres terá a senha: "))

senha = ""

while len(senha) < tamanho:
    senha += random.choice(todos_caracteres)


print("Senha gerada:", senha)
    