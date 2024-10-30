def soma(valor_1:float, valor_2:float =10) -> float: #10 vira o valor defaul se esse parâmetro n for passado
    """
    Doc string, serve para comentar e documentar partes do código.
    """
    valor_3 = valor_1+valor_2
    return valor_3

print(soma(2,5))
print(soma(2))