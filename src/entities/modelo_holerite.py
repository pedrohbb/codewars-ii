import mysql.connector
from docs.db import connection
from src.business.cadastros import Cadastro


class Modelo_Holerite():

    def __init__(self, holerite, cadastro: Cadastro):
        self.__holerite = holerite
        self.__cadastro = cadastro

    @property
    def holerite(self):
        return self.__holerite

    @property
    def cadastro(self):
        return self.__cadastro

    def gerar_modelo(self):
        matricula = self.holerite.matricula
        mes_referencia = self.holerite.mes_ano

        dados_funcionario = self.cadastro.consultar(matricula)

        nome = dados_funcionario['nome']
        data_admissao = dados_funcionario['data_admissao']
        cargo = dados_funcionario['codigo_cargo']

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        consultar_salario = (
            f""" SELECT descricao, comissao FROM cargos WHERE codigo_cargo = {cargo}; """)

        cursor.execute(consultar_salario)

        resultado = cursor.fetchall()

        funcao, taxa_comissao = resultado[0]

        cnx.close()

        salario_base = self.holerite.salario_base
        base_de_calculo = self.holerite.base_de_calculo
        comissao = self.holerite.valor_comissao
        faltas = self.holerite.faltas
        valor_faltas = self.holerite.valor_faltas
        aliquota_inss = self.holerite.aliquota_inss
        inss = self.holerite.inss
        aliquota_irrf = self.holerite.aliquota_irrf
        irrf = self.holerite.irrf
        fgts = self.holerite.fgts
        salario_liquido = self.holerite.salario_liquido

        total_vencimentos = salario_base + comissao
        total_descontos = round(valor_faltas + inss + irrf, 2)
        base_calculo_irrf = round(base_de_calculo - inss, 2)
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
                        |Matricula   Nome do Funcionário                               Data de Admissão                        Função                  |""",
            f"""
                        |  {matricula}    {nome:50} {data_admissao} {funcao:>51} |""",
            f"""
                        |______________________________________________________________________________________________________________________________|""",
            f"""
                        |______________________________________________________________________________________________________________________________|""",
            f"""
                        |Código   | Descrição                                                | Referência |      Proventos      |      Descontos       |""",
            f"""
                        |______________________________________________________________________________________________________________________________|""",
            f"""
                        |     101 | Salário base                                             |      22,50 | R$ {salario_base:16.2f} |                      |""",
            f"""
                        |     203 | Comissão                                                 | {taxa_comissao:>9.2f}% | R$ {comissao:16.2f} |                      |""",
            f"""
                        |     303 | Faltas                                                   | {faltas:10.2f} |                     | R$ {valor_faltas:17.2f} |""",
            f"""
                        |     973 | INSS Folha                                               | {aliquota_inss:9.2f}% |                     | R$ {inss:17.2f} |""",
            f"""
                        |     978 | IRRF Folha                                               | {aliquota_irrf:9.2f}% |                     | R$ {irrf:17.2f} |""",
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
                        |                                                                                 | R$ {total_vencimentos:16.2f} | R$ {total_descontos:17.2f} |""",
            f"""
                        |_____________________________________________________________________|           |____________________________________________|""",
            f"""
                        |Salário Base|Base Cálc INSS|Base Cálc FGTS|FGTS do mês|Base Cálc IRRF|           |                                            |""",
            f"""
                        | R$ {salario_base:<8.2f}| R$ {base_de_calculo:9.2f} | R$ {base_de_calculo:9.2f} | R$ {fgts:6.2f} | R$ {base_calculo_irrf:9.2f} |           |  Líquido a receber: R$ {salario_liquido:<19.2f} |""",
            f"""
                        |______________________________________________________________________________________________________________________________|""",
        ]

        return modelo_holerite
