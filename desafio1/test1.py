import json

def calcular_comissao(valor_venda: float) -> tuple[str, float]:

    if valor_venda < 100:
        return "Não foi aplicada comissão sobre a venda", 0

    elif valor_venda < 500:
        return "1%", round(valor_venda * 0.01, 2)

    return "5%", round(valor_venda * 0.05, 2)


comissao_vendedor_total = {}

with open("desafio1/test1.json", "r", encoding="utf-8") as fp:
    vendas_gerais = json.load(fp)


for venda_unitaria in vendas_gerais["vendas"]:
    
    valor = venda_unitaria["valor"]
    comissao, valor_comissao = calcular_comissao(valor)
    vendedor = venda_unitaria["vendedor"]

    venda_unitaria["comissao"] = comissao
    venda_unitaria["comissaoSobreVenda"] = round(valor_comissao, 2)

    if vendedor not in comissao_vendedor_total:
        comissao_vendedor_total[vendedor] = 0.0
    comissao_vendedor_total[vendedor] = round(comissao_vendedor_total[vendedor] + valor_comissao, 2)

with open("desafio1/relatorio_vendas.json", "w", encoding="utf-8") as fp:
    json.dump(vendas_gerais, fp, indent=4, ensure_ascii=False)

print("Relatorio atualizado!")
print(comissao_vendedor_total)