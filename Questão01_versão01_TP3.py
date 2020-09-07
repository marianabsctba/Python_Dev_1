#essa é a versão 01 da Questão 01.

print("\033[1;92m=~\033[0;0m" * 30)
print("""\033[1;94mBem-vindo ao SemCalote,
o seu programa para calcular o serviço!\033[0;0m""")
print("\033[1;92m=~\033[0;0m" * 30)


def minmax(valor, min, max):
    if min is not None:
        if valor < min:
            print('Valor inválido. Reinicie o programa.')
            exit(1)

    if max is not None:
        if valor > max:
            print('Valor inválido. Reinicie o programa.')
            exit(1)


def get_quantidade_pessoas():
    """
        Função para capturar e retornar numero de pessoas

        Numero de pessoas deve ser maior que zero
    """
    valor = int(input("Digite a quantidade de pessoas: "))
    minmax(valor, 0, None)
    return valor


def get_consumo():
    """
    """
    valor = float(input("Digite o valor do consumo: "))
    minmax(valor, 0, None)
    return valor


def get_gorjeta():
    """
    """
    valor = float(input("Digite o valor da gorjeta: "))
    minmax(valor, 0, 100)
    return valor


def total_consumo(consumo, gorjeta):
    return f"{consumo + consumo * (gorjeta / 100):.2f}".replace('.', ',')


def total_pessoa(qt_pessoa, consumo, gorjeta):
    return f"{(consumo + (consumo * (gorjeta / 100))) / qt_pessoa:.2f}".replace('.', ',')


consumo = get_consumo()
pessoas = get_quantidade_pessoas()
gorjeta = get_gorjeta()

print("\033[1;36m==\033[0;0m" * 30)
print("O valor do consumo, com taxa de serviço, é R$ {valor_consumo}.".format(
    valor_consumo=total_consumo(consumo, gorjeta)))
print("\033[1;36m==\033[0;0m" * 30)
print("O valor por pessoa é R$ {valor_pessoa}.".format(valor_pessoa=total_pessoa(pessoas, consumo, gorjeta)))

print("\033[1;36m==\033[0;0m" * 30)
print("\033[1;92m=~\033[0;0m" * 30)

print("""\033[1;94mFIM.
Obrigado por usar o SemCalote!
Volte sempre!\033[0;0m""")
print("\033[1;92m=~\033[0;0m" * 30)