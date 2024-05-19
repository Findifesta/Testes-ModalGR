# Questão 1

def apenas_letras(nomes_completos):
    for char in nomes_completos:
        if not char.isalpha() and char != ' ' and char != ',':
            return False
    return True


def cracha(nome_completo):
    divisao_nome = nome_completo.split()
    nome_cracha = divisao_nome[-1].upper() + ", "
    for nome in divisao_nome[:-1]:
        if nome.lower() not in ['de', 'da', 'das', 'do', 'dos', 'e']:
            nome_cracha += nome.upper()[0] + '. '
    return nome_cracha.strip()


def inserir_nomes():
    nomes_completos = input(
        "Olá!\nPor favor, digite o nome completo de cada colaborador, separando-os por vírgula:\n")
    if not nomes_completos:
        input("Nenhum nome foi inserido.\nPressione ENTER para sair.")
        return
    if apenas_letras(nomes_completos):
        nomes = nomes_completos.split(',')
        print("\nIdentificação nos crachás:")
        for nome_completo in nomes:
            nome_cracha = cracha(nome_completo.strip())
            print(nome_cracha)
    else:
        print("\nOcorreu um erro de digitação e algum número ou símbolo foi inserido. Certifique-se de que os nomes possuam apenas letras.")
    input("\nPressione ENTER para sair.")


inserir_nomes()
