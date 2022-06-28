import mysql.connector
from db import connection
from src.entities.modelo_holerite import Modelo_Holerite
from src.business.cadastros import Cadastro


class Holerite():

    def __init__(self, mes_ano: str, matricula: int, faltas):
        self.__mes_ano = mes_ano
        self.__matricula: int = matricula
        self.__salario_base: float = self.consultar_salario_base()
        self.__faltas: float = faltas
        self.__valor_faltas: float = round(
            (self.salario_base / 22.5) * self.faltas, 2)
        self.__valor_comissao: float = self.consultar_valor_comissao()
        self.__base_de_calculo: float = self.calcular_base_de_calculo()
        self.__fgts: float = round(self.base_de_calculo * 0.08, 2)
        self.__inss, self.__aliquota_inss = self.calcular_inss()
        self.__irrf, self.__aliquota_irrf = self.calcular_irrf()
        self.__salario_liquido: float = self.calcular_salario_liquido()

    @property
    def matricula(self) -> int:
        return self.__matricula

    @property
    def mes_ano(self) -> str:
        return self.__mes_ano

    @property
    def faltas(self) -> float:
        return self.__faltas

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def valor_faltas(self) -> float:
        return self.__valor_faltas

    @property
    def valor_comissao(self) -> float:
        return self.__valor_comissao

    @property
    def base_de_calculo(self) -> float:
        return self.__base_de_calculo

    @property
    def inss(self) -> float:
        return self.__inss

    @property
    def irrf(self) -> float:
        return self.__irrf

    @property
    def aliquota_inss(self) -> float:
        return self.__aliquota_inss

    @property
    def aliquota_irrf(self) -> float:
        return self.__aliquota_irrf

    @property
    def fgts(self) -> float:
        return self.__fgts

    @property
    def salario_liquido(self) -> float:
        return self.__salario_liquido

    def consultar_salario_base(self) -> float:

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        consultar_salario = (f""" SELECT salario_base FROM cargos \
                            RIGHT JOIN funcionarios USING (codigo_cargo) WHERE matricula = {self.matricula}; \
        """)

        cursor.execute(consultar_salario)

        try:
            salario = cursor.fetchall()[0][0]

            cnx.close()

            return salario

        except IndexError:
            print('Funcionário inexistente!')
            return('')

    def consultar_valor_comissao(self):

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        consultar_comissao = (
            f"SELECT comissao FROM funcionarios WHERE matricula = {self.matricula};")

        cursor.execute(consultar_comissao)

        bool_comissao = cursor.fetchall()[0][0]

        if bool_comissao == True:
            consultar_valor_comissao = (f"""
                        SELECT c.comissao FROM cargos AS c RIGHT JOIN funcionarios AS f USING(codigo_cargo) 
                        WHERE matricula = {self.matricula};
            """)

            cursor.execute(consultar_valor_comissao)

            valor_comissao = cursor.fetchall()[0][0]

        else:
            valor_comissao = 0

        cnx.close()

        return round(valor_comissao, 2)

    def calcular_base_de_calculo(self):
        add_eventual = 0  # input("Adicionais eventuais (hora extra etc): ")
        return round(self.salario_base + self.valor_comissao + add_eventual - self.valor_faltas, 2)

    def calcular_inss(self) -> float:

        faixas_inss = [
            (0, 1212, 0.075),
            (1212.01, 2427.35, 0.09),
            (2427.36, 3641.03, 0.12),
            (3641.04, 7087.22, 0.14)]

        inss = 0

        for faixa in faixas_inss:
            if self.base_de_calculo > faixa[0]:
                if self.base_de_calculo < faixa[1]:
                    inss += (self.base_de_calculo - faixa[0]) * faixa[2]
                    aliquota_inss = faixa[2]
                else:
                    inss += (faixa[1] - faixa[0]) * faixa[2]
                    aliquota_inss = faixa[2]
            else:
                break

        return round(inss, 2), round(aliquota_inss, 4)

    def calcular_irrf(self) -> float:

        aux = self.base_de_calculo - self.calcular_inss()[0]

        faixas_irrf = [
            (0, 1903.98, 0, 0),
            (1903.99, 2826.65, 0.075, 142.8),
            (2826.66, 3751.05, 0.15, 354.8),
            (3751.06, 4664.68, 0.225, 636, 13),
            (4664.69, 999999, 0.275, 869.36)]

        for faixa in faixas_irrf:
            if aux > faixa[0] and aux < faixa[1]:
                irrf = (aux * faixa[2]) - faixa[3]
                aliquota_irrf = faixa[2]

        return round(irrf, 2), round(aliquota_irrf, 4)

    def calcular_salario_liquido(self) -> float:

        proventos = self.salario_base + self.valor_comissao
        descontos = self.valor_faltas + self.inss + self.irrf
        salario_liquido = proventos - descontos
        return round(salario_liquido, 2)

    def inserir_holerite_db(self) -> None:

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        inserir_holerite = (f""" \
                        INSERT INTO holerite (mes_ano, matricula, faltas, inss, irrf, fgts, salario_liquido) \
                        VALUES ('{self.mes_ano}', {self.matricula}, {self.faltas}, {self.inss}, {self.irrf}, {self.fgts}, {self.salario_liquido});
        """)

        cursor.execute(inserir_holerite)

        cnx.commit()

        cnx.close()

    def gerar_holerite(self) -> None:

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        consultar_holerite = (
            f"SELECT * FROM holerite WHERE matricula = {self.matricula} AND mes_ano = '{self.mes_ano}';")

        cursor.execute(consultar_holerite)

        try:
            cursor.fetchall()[0][0]
        except IndexError:
            self.inserir_holerite_db()

        cadastro = Cadastro()
        holerite = Modelo_Holerite(self, cadastro)
        modelo_holerite = holerite.gerar_modelo()

        for linha in modelo_holerite:
            print(linha)

        cnx.close()


def gerar_todos_holerites(cadastro: Cadastro, mes_ano: str) -> None:
    lista_funcionarios = cadastro.listar()
    if len(lista_funcionarios) == 0:
        print('Não há nenhum funcionário cadastrado!')

    else:
        for matricula in lista_funcionarios.keys():
            holerite = Holerite(mes_ano, matricula, 0)
            holerite.gerar_holerite()
            print('\n' + ' '*24 + '#'*128)
