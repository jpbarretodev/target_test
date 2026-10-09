import json, uuid

class Alteracao:

    def __init__(self, descricao: str):
        self.descricao = descricao
        self.hash_alteracao = str(uuid.uuid4())
    

with open("desafio2/test2.json", "r", encoding="utf-8") as fp:
    produtos = json.load(fp)

def validador_inteiro():

    while True:
        numero = input("Insira sua escolha (somente inteiros): ")
        try:
            numero = int(numero)
            return numero
        except ValueError:
            continue

def acessar_produto(estoque_geral, id_produto: int)-> dict:
    return next(p for p in estoque_geral["estoque"] if p["codigoProduto"] == id_produto)

def start(estoque_geral: dict):

    print("\nEstoque Atual:")
    for produto in estoque_geral["estoque"]:
        print(f"ID: {produto['codigoProduto']} | {produto['descricaoProduto']} | Quantidade: {produto['estoque']}")
    print()

    print("Escolha o id do produto que deseja alterar: ")
    id_produto = validador_inteiro()

    while True:
        if id_produto not in list(map(lambda produto: produto["codigoProduto"], estoque_geral["estoque"])):
            print("Escolha o id do produto que deseja alterar: ")
            id_produto = validador_inteiro()
            continue
        break

    dicionario_produto_selecionado = acessar_produto(estoque_geral, id_produto)

    print("O que deseja fazer? 1 - adicionar, 2 - retirar")
    acao = validador_inteiro()

    while True:
        if acao not in [1, 2]:
            print("O que deseja fazer? 1 - adicionar, 2 - retirar")
            acao = validador_inteiro()
            continue
        break

    print("insira a quantidade que deseja alterar: ")
    qntde = validador_inteiro()
    while qntde <= 0:
        print("A quantidade nao pode ser menor ou igual a 0. Insira novamente: ")
        qntde = validador_inteiro()
        continue

    if acao == 1:
        dicionario_produto_selecionado["estoque"] += qntde
    else:
        while qntde > dicionario_produto_selecionado["estoque"]:
            print("A quantidade nao pode ser maior que a do estoque. Insira novamente: ")
            qntde = validador_inteiro() 
        dicionario_produto_selecionado["estoque"] -= qntde
    

    while True:
        descricao = input("Insira a descrição da alteração (obrigatorio): ")

        if descricao:
            break

        print("Descrição não pode ser vazia")

    alteracao_produto = Alteracao(descricao=descricao)


    with open("desafio2/test2.json", "w", encoding="utf-8") as fp:
        json.dump(estoque_geral, fp, indent=4, ensure_ascii=False)

    print("=" * 50)
    print(f"""
    RESUMO DA MOVIMENTAÇÃO:\n
    Id do produto: {dicionario_produto_selecionado["codigoProduto"]}\n
    Descrição do produto: {dicionario_produto_selecionado["descricaoProduto"]}\n
    Estoque atual: {dicionario_produto_selecionado["estoque"]}\n
    Descrição da movimentação: {alteracao_produto.descricao}\n
    Id da movimentação: {alteracao_produto.hash_alteracao}\n    
    """)
    print("=" * 50)


start(produtos)