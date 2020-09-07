#Essa é a versão 02 da questão 03.
# Aqui, diferentemente da versão 01, o programa é interrompido se a nota <0 ou >10.

print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)
print("\033[1;34mBEM-VINDO AO JURYMANFANTASY, O MELHOR PROGRAMA PARA JURADOS!\033[0;0m")
print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)

def minmax(n, min=None, max=None):
    if min is not None:
        if n < min:
            print('Valor menor do que zero. Programa reiniciado.')
            exit(1)

    if max is not None:
        if n > max:
            print('Valor maior do que 10. Programa reiniciado.')
            exit(1)

    if n == min:
        print('A nota é  igual a 0.')
        print("\033[1;34m==\033[1;92m==\033[0;0m" * 20)

    if n == max:
        print("A nota é igual a 10.")
        print("\033[1;34m==\033[1;92m==\033[0;0m" * 20)

    if n > min and n < max:
        print('A nota é maior do que 0 e menor do que 10.')
        print("\033[1;34m==\033[1;92m==\033[0;0m" * 20)


def get_aluno():
    nome = input("\nDigite o nome do participante: ").strip().upper()
    nota = float(input("Digite a nota do participante: "))
    minmax(nota, 0, 10)
    return (nome, nota)

list_aluno = []
maior_nota = 0
for i in range(0, 5):
    aluno = get_aluno()
    if aluno[1] > maior_nota:
        maior_nota = aluno[1]
    list_aluno.append(aluno)


for i in range(0, 5):
    if list_aluno[i][1] == maior_nota:
        print("\nO(a) participante {nome} é o(a) vencedor(a), pois possui a maior nota: {nota}".format(nome=list_aluno[i][0], nota=list_aluno[i][1]))

print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)
print("\033[1;34mObrigada pela preferência! Volte sempre!\033[0;0m")
print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)


