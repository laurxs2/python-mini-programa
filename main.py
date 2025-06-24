tipo_de_consulta = input("Insira o numero da consulta desejada:\n"
                        "1 - Soma de orcamento\n" 
                        "2 - Texto em caixa alta\n" 
                        "3 - Cálculo de parcelamento e juros\n"
                        )

#soma de valores
if tipo_de_consulta == '1':
    soma = 0.0
    while True:
        soma_orcamento = input("Digite um número no formato <000.00> ou 'fim' para encerrar: ")
        if soma_orcamento.lower() == 'fim':
            break 
        valores = soma_orcamento.replace(',', '.')
        try:
            numero = float(soma_orcamento) 
            soma += numero  
        except ValueError:
            print("Valor inválido! Insira um número.")
    print(f"A soma total é: {soma:.2f}")

#texto em caixa alta
if tipo_de_consulta == '2':
    texto = input("Insira o texto a ser transformado:")
    print(texto.upper())

#calculo de parcelamentos e juros
if tipo_de_consulta == '3':
    calculo_de = input("Selecione a opção:\n" \
                 "1 - Parcelas\n"\
                 "2 - Juros\n"\
                 "3 - Desconto\n"
                )
    
    #calculo de parcelas
    if calculo_de == "1": 
        valor_para_parcelar = input("Insira o valor a ser parcelado: ")
        numero_parcelas = input("Insira o número de parcelas: ")
        valor_parc_replace = valor_para_parcelar.replace(',', '.')

        try:
            valor_parcelarfloat = float(valor_para_parcelar) 
            parcelasfloat = float(numero_parcelas) 

        except ValueError:
            print("Valor inválido! Insira um número.")

        resultado = valor_parcelarfloat / parcelasfloat
        print(resultado, "em", numero_parcelas, "parcelas.")

    #calculo de % juros
    if calculo_de == "2":
        valor_sem_juros = input("Insira o valor a ser calculado: ")
        porcentagem_juros = input("Insira a porcentagem a ser adicionada: ")

        valor_juros_replace = valor_sem_juros.replace(',', '.')

        try:
            valor_jurosfloat = float(valor_sem_juros) 
            porcentagem_jurosfloat = float(porcentagem_juros) 
        except ValueError:
            print("Valor inválido! Insira um número.")

        adicao_juros =  valor_jurosfloat + (valor_jurosfloat * porcentagem_jurosfloat / 100)
        print("O valor com juros é: ", adicao_juros)

    #calculo de % de desconto
    if calculo_de == "3":
        valor_sem_desconto = input("Insira o valor a ser calculado: ")
        porcentagem_desconto = input("Insira a porcentagem a ser descontada: ")

        valor_sem_desconto_replace = valor_sem_desconto.replace(',', '.')

        try:
            valor_sem_descontofloat = float(valor_sem_desconto) 
            porcentagem_descontofloat = float(porcentagem_desconto) 
        except ValueError:
            print("Valor inválido! Insira um número.")

        calc_desconto = valor_sem_descontofloat - ( valor_sem_descontofloat * porcentagem_descontofloat / 100)
        print("O valor com desconto é de: ", calc_desconto)
