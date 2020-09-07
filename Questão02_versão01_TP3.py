# Essa é a versão 01 da questão 02, que usa a idade em inteiros para fazer a verificação do eleitor.
# se a idade for inválida (<0) o programa pedirá uma válida.

def lin():
    print("\033[1;33m==\033[0;0m" * 30)

lin()

print("Olá, esse é o simulador para eleitores \033[1;32mDemocratic\033[1;33mChoice.\033[0;0m")
print("""
\033[1;34mInstruções:\033[0;0m


1° - Digite a sua idade em inteiros, no formato "NN", "14", "85" (exemplos).
2° - Idades inferiores a zero não serão computadas.

\033[1;34mVamos lá? Verique se você é eleitor obrigatório ou não:\033[0;0m """)

lin()



def voto(idade):
    while True:
        if idade < 0:
            idade = int(input("Idade inválida. Digite uma idade válida: "))
        elif idade < 16:
            return f"Desculpe, com {idade} anos, ainda não é possível votar."
        elif 16 <= idade < 18 or idade >= 70:
            return f"Com a idade de {idade} anos, o voto é facultativo."
        else:
            return f"Com a idade de {idade} anos, o voto é obrigatório."



eleitor = int(input("Qual a sua idade? "))

print(voto(eleitor))

lin()

print("Obrigado por usar \033[1;32mDemocratic\033[1;33mChoice\033[0;0m. Volte sempre!")

lin()
