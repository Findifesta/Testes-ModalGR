# questao_2
def entrada_de_dados():
    valores_dos_dados = input(
        "Olá!\nPor favor, digite os dados que serão processados, separando-os por vírgula:\n")
    if not valores_dos_dados.strip():
        input("Nenhum dado foi inserido.\nPressione ENTER para sair.")
        return
    dados = valores_dos_dados.split(',')
    print("\nDados numéricos:")
    for dado in dados:
        dado = dado.strip()
        if dado.isdigit():
            print(dado)
    print("\nDados não-numéricos:")
    for dado in dados:
        dado = dado.strip()
        if not dado.isdigit():
            print(dado)
    input("\nPressione ENTER para sair.")


entrada_de_dados()
