# questao_2
def entrada_de_dados():
    valores_dos_dados = input(
        "Olá!\nPor favor, digite os dados que serão processados, separando-os por vírgula:\n")
    if not valores_dos_dados.strip():
        input("Nenhum dado foi inserido.\nPressione ENTER para sair.")
        return
    dados = valores_dos_dados.split(',')

    def checa_numero(dado):
        try:
            float(dado)
            return True
        except ValueError:
            return False

    print("\nDados numéricos:")
    for dado in dados:
        dado = dado.strip()
        if checa_numero(dado):
            print(dado)
    print("\nDados não-numéricos:")
    for dado in dados:
        dado = dado.strip()
        if not checa_numero(dado):
            print(dado)
    input("\nPressione ENTER para sair.")


entrada_de_dados()
