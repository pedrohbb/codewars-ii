import os
import mysql.connector
from entities.funcionarios import Funcionario

class Matricula():

    def __init__(self, matricula: int):
        self.__matricula: int = matricula

    @property
    def matricula(self) -> int:
        return self.__matricula

    def gerar_matricula(funcionario: Funcionario):
        cnx = mysql.connector.connect(user=os.getenv('USER'),
                                      password=os.getenv('PASSWORD'),
                                      host=os.getenv('HOST'),
                                      database=os.getenv('DATABASE'))
        cursor = cnx.cursor()

        insert_funcionario = (
            f"INSERT INTO funcionarios (nome, cpf, data_admissao, codigo_cargo, comissao) VALUES ({funcionario.nome}, {funcionario.cpf}, {funcionario.data_admissao}, {funcionario.codigo_cargo}, {funcionario.comissao});")

        cursor.execute(insert_funcionario)

        matricula = (
            f"SELECT matricula FROM funcionarios WHERE cpf = {funcionario.cpf} AND data_admissao = {funcionario.data_admissao};")

        cursor.execute(matricula)

        print(cursor)
        print(type(cursor))

        cursor.close()
        cnx.close()
