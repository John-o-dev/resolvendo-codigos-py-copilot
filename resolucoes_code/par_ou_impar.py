# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação

valor = int(input("Insira um número inteiro: "))

if valor % 2 == 0:
    print("O valor", valor, "É par")
else:
    print("O valor ", valor, "É impar")