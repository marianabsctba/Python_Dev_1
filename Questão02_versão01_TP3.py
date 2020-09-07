# Essa é a versão 01 da questão 02, que usa a idade em inteiros para fazer a verificação do eleitor.
# se a idade for inválida (<0) o programa pedirá uma válida.

import time

print("\033[1;32m==\033[0;0m" * 30)
print("Olá, esse é o simulador para eleitores \033[1;32mDemocratic\033[1;33mChoice.\033[0;0m")
print("""
\033[1;34mInstruções:\033[0;0m

1° - Digite o seu ano de nascimento no formato 'aaaa'.
2° - Datas de nascimento futuras não serão computadas.

\033[1;34mVamos lá? Verique se você é eleitor obrigatório ou não:\033[0;0m """)
print("\033[1;33m==\033[0;0m" * 30)



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

print("\033[1;33m==\033[0;0m" * 30)
print("Obrigado por usar \033[1;32mDemocratic\033[1;33mChoice\033[0;0m. Volte sempre!")
print("\033[1;33m==\033[0;0m" * 30)
