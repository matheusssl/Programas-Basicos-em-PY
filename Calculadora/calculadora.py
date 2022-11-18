n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print("+ para Adição")
print("- para Subtração")
print("* para Multiplicação")
print("/ para Divisão")
print("** para Potenciação")

operacao = input('Digite a operação desejada: ')
resultado = 0

if operacao == ('+'):
    resultado = n1 + n2

elif operacao == ('-'):
    resultado = n1 - n2

elif operacao == ('*'):
    resultado = n1 * n2

elif operacao == ('/'):
    resultado = n1 / n2

elif operacao == ('**'):
    resultado = n1 ** n2

else:
    print('Operação não disponível, encerrando calculadora!!!')

print(n1, operacao, n2, '=', resultado)
