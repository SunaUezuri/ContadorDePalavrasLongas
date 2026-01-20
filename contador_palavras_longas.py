def contador_palavras_longas(texto: str, comprimento_minimo: int) -> list[str]:
    """
    Conta o número de palavras em um texto que têm um comprimento maior ou igual ao especificado.

    Parâmetros:
    texto (str): O texto a ser analisado.
    comprimento_minimo (int): O comprimento mínimo das palavras a serem contadas.

    Retorna:
    int: O número de palavras que atendem ao critério de comprimento.
    """
    palavras = texto.split()
    palavras_longas = []
    for palavra in palavras:
        if len(palavra) >= comprimento_minimo:
            palavras_longas.append(palavra)
    return palavras_longas