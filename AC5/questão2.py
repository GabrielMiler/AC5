def tamanho_número(x):
    a = str(x)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)


numero = int(input("Digite um número inteiro: "))

print(tamanho_número(numero))
