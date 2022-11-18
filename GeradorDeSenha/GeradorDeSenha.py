from random import choice
import string

Tamanho = int(input("Total de dígitos da senha: "))
Caracteres = string.ascii_letters + string.digits + string.punctuation
SenhaForte = ''
for i in range(Tamanho):
  SenhaForte += choice(Caracteres)

print(f"Senha gerada: {SenhaForte}")