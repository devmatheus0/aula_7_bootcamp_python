from etl import somar_valores_dos_produtos,ler_csv,filtrar_produtos_nao_entregues

path_do_arquivo = 'vendas.csv'

lista_de_produtos = ler_csv(path_do_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)