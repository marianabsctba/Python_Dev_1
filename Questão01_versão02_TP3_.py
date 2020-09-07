#Essa é a versão 02 da Questão 01, com if/elif/else aninhados... não é a minha preferência, mas fiz um exemplo.

def lin():
    print("\033[1;96m~=\033[0;0m" * 30)

def lin_2():
    print("\033[1;96m--\033[0;0m" * 30)

def lin_3():
    print("\033[1;96m==\033[0;0m" * 30)

lin()

print("""\033[1;34mOLÁ, BEM-VINDO(a) AO SEUBOLSO,
A SUA MELHOR OPÇÃO PARA DIVIDIR CONTAS DE RESTAURANTE!\033[0;0m""")

lin()



def calc():
    while True:
        consumo = float(input("Digite o valor do consumo: R$ "))
        if consumo < 0:
            lin_2()
            print("\033[1;91mOoops...Valor inválido. Programa interrompido.\033[0;0m")
            lin_2()
            exit()
        else:
            numero_pessoas = int(input("Digite o n° de pessoas que dividirão a conta: "))
            if numero_pessoas < 0:
                lin_2()
                print("\033[1;91mOoops...Valor inválido. Programa interrompido.\033[0;0m")
                lin_2()
                exit()
            else:
                percentual_servico = int(input("Digite o percentual do serviço (entre 0 a 100): % "))
                if percentual_servico < 0 or percentual_servico > 100:
                    print("\033[1;91mOoops...Valor inválido. Programa interrompido.\033[0;0m")
                    lin_2()
                    exit()
                else:
                    total_conta = consumo + consumo * (percentual_servico / 100)
                    valor_pessoa = total_conta / numero_pessoas
                    lin_3()
                    print(f"\033[1;34mO valor total da conta é de R$ {total_conta:.2f}\033[0;0m".replace(".", ","))
                    lin_3()
                    print(f"\033[1;34mO total da conta dividido por {numero_pessoas} pessoas é de R$ {valor_pessoa:.2f}\033[0;0m".replace(".", ","))
                    break


calc()

lin()
print("\033[1;34mOBRIGADO POR USAR SEUBOLSO. VOLTE SEMPRE!\033[0;0m")
lin()
