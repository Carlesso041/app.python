def criar_lista_pecas():
    lista_pecas = []
    while True:
        peca = input("Digite o nome da peça automotiva (ou digite 'fim' para sair): ")
        if peca.lower() == 'fim':
            break
        lista_pecas.append(peca)
    return lista_pecas

def main():
    print("Bem-vindo! Por favor, insira as peças automotivas:")
    pecas = criar_lista_pecas()
    print("\nLista de peças automotivas inseridas:")
    for index, peca in enumerate(pecas, start=1):
        print(f"{index}. {peca}")

if __name__ == "__main__":
    main()