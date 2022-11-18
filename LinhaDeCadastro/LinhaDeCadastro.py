cadastro = []
tentativas=0
print('Por favor, cadastre-se!')
email0 = input('Email: ')
senha0 = input('Senha: ')

cadastro.append(email0)
cadastro.append(senha0)

print('Faça login! ')
while tentativas < 5:
    email1 = input('Entre seu email: ')
    senha1 = input('Entre sua senha: ')
    tentativas += 1

    if email1 not in cadastro or senha1 not in cadastro:
        print('Email/Senha inválidos!')
    else:
        print('Olá, seja bem-vindo!')
        break
else:
    print('Tente novamente mais tarde!')