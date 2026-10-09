from datetime import datetime, date

while True:

    valor_atual_divida = input("Insira o valor atual da dívida: ")

    try:
        valor_atual_divida = float(valor_atual_divida)
        break
    except ValueError:
        print("O valor deve ser do tipo 00.00\n")

while True:

    try:
        data_vencimento = input("Insira a data do vencimento (dd/mm/aaaa): ")
        data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y").date()
        if data_vencimento >= date.today():
            print("A data não pode ser a mesma e nem maior que a data de hoje. Insira novamente:\n ")
            continue
        break
    except ValueError:
        print("Data inválida ou formato incorreto. Use o formato dd/mm/aaaa.\n")

diferenca_datas = (date.today() - data_vencimento).days

divida_com_juros = ((diferenca_datas * 0.025) * valor_atual_divida) + valor_atual_divida

print(f"\nValor da dívida atualizada com {diferenca_datas} dias de atraso: R$ {divida_com_juros:.2f}")