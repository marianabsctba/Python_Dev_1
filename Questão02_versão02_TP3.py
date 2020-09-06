print("\033[1;32m==\033[0;0m" * 30)
print("Olá, esse é o simulador para eleitores \033[1;32mDemocratic\033[1;33mChoice.\033[0;0m")
print("""
\033[1;34mInstruções:\033[0;0m

1° - Digite o seu ano de nascimento no formato 'aaaa'.
2° - Datas de nascimento futuras não serão computadas.

\033[1;34mVamos lá? Verique se você é eleitor obrigatório ou não:\033[0;0m """)
print("\033[1;33m==\033[0;0m" * 30)

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 0:
        return f"\033[1;31mValor inválido. Reinicie o programa e tente novamente.\033[0;0m"
    elif idade < 16:
        return f"\033[1;32mDesculpe, com a idade de {idade} anos, ainda não é possível votar\033[0;0m."
    elif 16 <= idade < 18 or idade >= 70:
        return f"\033[1;33mCom a idade de {idade} anos, o voto é facultativo\033[0;0m."
    else:
        return f"\033[1;34mCom a idade de {idade} anos, o voto é obrigatório.\033[0;0m"


nascimento = int(input("Em que ano você nasceu? "))
print(voto(nascimento))
print("\033[1;33m==\033[0;0m" * 30)
print("Obrigado por usar \033[1;32mDemocratic\033[1;33mChoice\033[0;0m. Volte sempre!")
print("\033[1;33m==\033[0;0m" * 30)