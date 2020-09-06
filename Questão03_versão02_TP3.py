print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)
print("\033[1;34mBEM-VINDO AO JURYMANFANTASY, O MELHOR PROGRAMA PARA JURADOS!\033[0;0m")
print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)

def minmax(n, min=None, max=None):
    if min is not None:
        if n < min:
            print('Valor inválido. Programa reiniciado.')
            exit(1)

    if max is not None:
        if n > max:
            print('Valor inválido. Programa reiniciado.')
            exit(1)


def get_aluno():
    nome = input("\nDigite o nome do participante: ").strip().upper()
    nota = float(input("\nDigite a nota do participante: "))
    print("\033[1;34m==\033[1;92m==\033[0;0m" * 20)

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
        print("\nO(a) participante {nome} é o vencedor, pois possui a maior nota: {nota}".format(nome=list_aluno[i][0], nota=list_aluno[i][1]))

print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)
print("\033[1;34mObrigada pela preferência! Volte sempre!\033[0;0m")
print("\033[1;34m=~\033[1;92m=~\033[0;0m" * 20)


