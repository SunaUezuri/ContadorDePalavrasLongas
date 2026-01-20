from contador_palavras_longas import contador_palavras_longas

texto: str = input("Digite um texto: ")
comprimento_minimo: int = int(input("Digite o comprimento mínimo das palavras a serem contadas: "))

palavras_longas: list[str] = contador_palavras_longas(texto, comprimento_minimo)

if not palavras_longas:
    print(f"Nenhuma palavra encontrada com comprimento maior ou igual a {comprimento_minimo}.")
else:
    print(f"Palavras com comprimento maior ou igual a {comprimento_minimo}:")
    for palavra in palavras_longas:
        print(palavra)