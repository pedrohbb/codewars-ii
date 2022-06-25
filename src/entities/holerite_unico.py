import os
import mysql.connector
from docs.db.connection import config
from entities.holerite import Holerite

class Holerite_Unico(Holerite):

    def __init__(self, mes_ano: str, matricula: int, faltas: float):
        super().__init__(mes_ano)
        self.__matricula: int = matricula
        self.__faltas: float = faltas
        self.__salario_base: float = self.salario_base()
        self.__valor_faltas: float = self.valor_faltas()
        self.__valor_comissao: float = self.valor_comissao()
        self.__base_de_calculo: float = self.base_de_calculo()
        self.__fgts: float = self.base_de_calculo * 0.08
        self.inserir_holerite_db()
        
    @property
    def matricula(self) -> int:
        return self.__matricula

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
    def fgts(self) -> float:
        return self.__fgts

    def salario_base(self) -> float:
        
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        consultar_salario = (
            f"SELECT salario_base FROM cargos RIGHT JOIN funcionarios USING (codigo_cargo) WHERE matricula = {self.matricula};")
        cursor.execute(consultar_salario)

        salario = cursor.fetchall()[0][0]

        cnx.close()

        return salario

    def calcular_inss(self, base_de_calculo: float) -> float:

        faixas_inss = [
                        (0, 1212, 0.075),
                        (1212.01, 2427.35, 0.09),
                        (2427.36, 3641.03, 0.12), 
                        (3641.04, 7087.22, 0.14)]

        inss = 0

        for faixa in faixas_inss:
            if base_de_calculo > faixa[0]:
                if base_de_calculo < faixa[1]:
                    inss += (base_de_calculo - faixa[0]) * faixa[2]
                else:
                    inss += (faixa[1] - faixa[0]) * faixa[2]
            else:
                break

        return round(inss, 2)

    def calcular_irrf(self) -> float:

        base_de_calculo -= self.calcular_inss(self.base_de_calculo)

        faixas_irrf = [(0, 1903.98, 0, 0), (1903.99, 2826.65, 0.075, 142.8),
                       (2826.66, 3751.05, 0.15, 354.8), (3751.06, 4664, 68, 0.225, 636, 13), (4664.69, 999999, 27.5, 869.36)]

        for faixa in faixas_irrf:
            if self.base_de_calculo > faixa[0] and self.base_de_calculo < faixa[1]:
                irrf = (self.base_de_calculo * faixa[2]) - faixa[3]

        return round(irrf, 2)

    def valor_faltas(self):

        valor_faltas = (self.salario_base / 22.5) * self.faltas
        return valor_faltas

    def valor_comissao(self):

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        consultar_comissao = (
            f"SELECT comissao FROM funcionarios WHERE matricula = {self.matricula};")
        cursor.execute(consultar_comissao)

        bool_comissao = cursor.fetchall()[0][0]

        if bool_comissao == True:
            consultar_valor_comissao = (
                f"SELECT c.comissao FROM cargos AS c RIGHT JOIN funcionarios AS f USING(codigo_cargo) WHERE matricula = {self.matricula};")

            cursor.execute(consultar_valor_comissao)

            valor_comissao = cursor.fetchall()[0][0]

        else:
            valor_comissao = 0

        cnx.close()

        return valor_comissao

    
    def inserir_holerite_db(self) -> None:
        
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        inserir_holerite = (
            f"INSERT INTO holerite (mes/ano, matricula, faltas, inss, irrf, fgts) VALUES ('{self.mes_ano}', {self.matricula}, {self.faltas}, {self.inss}, {self.irrf}, {self.fgts});")

        cursor.execute(inserir_holerite)
        
        cnx.close()
        

    def gerar_holerite(self) -> None:

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        consultar_nome = (
            f"SELECT nome, data_admissao, descricao FROM funcionarios JOIN cargos USING(codigo_cargo) WHERE matricula = {self.matricula};")

        cursor.execute(consultar_nome)

        nome_funcionario = cursor.fetchall()[0][0]
        
        

        cnx.close()
