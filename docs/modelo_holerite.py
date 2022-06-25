def modelo_holerite(matricula, nome, mes_referencia, data_admissao, funcao, salario_base, base_de_calculo, taxa_comissao, comissao, faltas, valor_faltas, aliquota_inss, inss, aliquota_irrf, irrf, fgts, liquido_salario):

    total_vencimentos = salario_base + comissao
    total_descontos = valor_faltas + inss + irrf
    base_calculo_irrf = base_de_calculo - inss
    aliquota_inss = aliquota_inss * 100
    aliquota_irrf = aliquota_irrf * 100
    taxa_comissao = taxa_comissao * 100

    modelo_holerite = [
        f"""
________________________________________________________________________________________________________________________________""",
        f"""
|Empresa XPTO Alimentos                                                                          Recibo de Pagamento de Salário|""",
        f"""
| Endereço: Rua XV de Novembro, 15, Centro                                                       Mês de referência: {mes_referencia}    |""",
        f"""
|CNPJ: 12.345.678/0001-00                                                                                                      |""",
        f"""
|______________________________________________________________________________________________________________________________|""",
        f"""
|______________________________________________________________________________________________________________________________|""",
        f"""
|Matricula   Nome do Funcionário                                       Data de Admissão                Função                  |""",
        f"""
|  {matricula}   {nome}                                            {data_admissao}                      {funcao}    |""",
        f"""
|______________________________________________________________________________________________________________________________|""",
        f"""
|______________________________________________________________________________________________________________________________|""",
        f"""
|Código   | Descrição                                                | Referência |        Proventos    |      Descontos       |""",
        f"""
|______________________________________________________________________________________________________________________________|""",
        f"""
|     101 | Salário base                                             |      22,50 |          R$ {salario_base:0.2f} |                      |""",
        f"""
|     203 | Comissão                                                 |     {taxa_comissao:0.2f}% |          R$ {comissao:0.2f} |                      |""",
        f"""
|     303 | Faltas                                                   |       {faltas:0.2f} |                     |            R$ {valor_faltas:0.2f} |""",
        f"""
|     973 | INSS Folha                                               |     {aliquota_inss:0.2f}% |                     |            R$ {inss:0.2f} |""",
        f"""
|     978 | IRRF Folha                                               |      {aliquota_irrf:0.2f}% |                     |            R$ {irrf:0.2f} |""",
        f"""
|         |                                                          |            |                     |                      |""",
        f"""
|         |                                                          |            |                     |                      |""",
        f"""
|         |                                                          |            |                     |                      |""",
        f"""
|______________________________________________________________________________________________________________________________|""",
        f"""
|                                                                                 | Total Vencimentos   | Total Descontos      |""",
        f"""
|                                                                                 |         R$ {total_vencimentos:0.2f}  |           R$ {total_descontos:0.2f} |""",
        f"""
|_____________________________________________________________________|           |____________________________________________|""",
        f"""
|Salário Base|Base Cálc INSS|Base Cálc FGTS|FGTS do mês|Base Cálc IRRF|           |                                            |""",
        f"""
| R$ {salario_base:0.2f} |  R$ {base_de_calculo:0.2f}  |  R$ {base_de_calculo:0.2f}  | R$ {fgts:0.2f}  |  R$ {base_calculo_irrf:0.2f} |           |  Líquido a receber:      R$ {liquido_salario:0.2f}        |""",
        f"""
|______________________________________________________________________________________________________________________________|""",
    ]

    return modelo_holerite


# TESTE
modelo = modelo_holerite(100001, 'Fulano de Tal', '06/2022', '01/01/2021',
                         'Especialista em Business Intelligence', 3090, 3900, 0.1, 1000, 5, 800, 0.12, 890, 0.09, 320, 800, 2500)
for linha in modelo:
    print(linha)
