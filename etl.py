import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo: str) -> list[dict]:
    """
    Função que le um arquivo csv e retorna uma lista de dicionarios para cada linha do arquivo csv
    """
    dados = []
    with open(nome_do_arquivo, mode='r',encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produtos in lista:
        if produtos['entregue'] == 'False': #usando método get produtos.get('entregue')
            lista_com_produtos_filtrados.append(produtos)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Função que soma os valores do csv
    """
    valor_total = 0
    for produtos in lista_com_produtos_filtrados:
        valor_total += int(produtos['preco']) 
    return valor_total