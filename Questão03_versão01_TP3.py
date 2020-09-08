#Essa é a versão 01 da Questão 03. Verifico com listas e imprimo os dados com elas.
#Essa versão verifica e imprime na tela se a nota é >= 0 ou >=10 e retorna o input caso os valores sejam <0 ou > 10.

def lin():
    print("\033[1;34m==\033[1;92m==\033[0;0m" * 20)

lin()

print("\033[1;34mBEM-VINDO AO JURYMANFANTASY, O MELHOR PROGRAMA PARA JURADOS!\033[0;0m")

lin()


def vencedor_concurso():

    temp = []
    princ = []

    while True:
        for p in range(1, 6):
            temp.append(str(input("\033[36m" + f"Digite o nome do {p}º candidato: " + "\033[0;0m")).upper().strip())
            nota = float(input(f"Digite a {p}ª nota: "))
            if nota > 0 and nota < 10:
                print("\033[32m" + "A nota é maior do zero e menor que 10." + "\033[0;0m")
            elif nota == 10:
                print("\033[32m" + "A nota é igual a 10." + "\033[0;0m")
            elif nota == 0:
                print("\033[32m" + "A nota é igual a zero." + "\033[0;0m")
            else:
                nota = float(input("\033[31m" + "Oops..." + "Digite uma nota válida (0 a 10): " + "\033[0;0m"))

            lin()

            temp.append(nota)
            if len(princ) == 0:
                mai = men = temp[1]
            else:
                if temp[1] > mai:
                    mai = temp[1]
                elif temp[1] < men:
                    men = temp[1]
            princ.append(temp[:])
            temp.clear()

        print("\033[34m" + f"Você cadastrou {len(princ)} pessoas." + "\033[0;0m")
        print("\033[33m" + f"A maior nota é {mai}, do(s) VENCEDOR(ES)", end=" ")
        for n in princ:
            if n[1] == mai:
                print(f"[{n[0]}]" + "\033[0;0m", end=" ")
        print("\033[31m" + f". A menor nota é {men}, do(a) participante", end=" ")
        for n in princ:
            if n[1] == men:
                print(f"[{n[0]}]." + "\033[0;0m")

                lin()

                print("Obrigado pela preferência! Volte sempre!")

                lin()
                exit()

vencedor_concurso()
print(vencedor_concurso())

