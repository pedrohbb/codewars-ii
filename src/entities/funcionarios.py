import os
import mysql.connector


class Funcionario():

    def __init__(self, nome: str, cpf: str, data_admissao: str, codigo_cargo: int, comissao: bool):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_admissao: str = data_admissao
        self.__codigo_cargo: int = codigo_cargo
        self.__comissao: bool = comissao
        self.__matricula: int = self.gerar_matricula(
            nome, cpf, data_admissao, codigo_cargo, comissao)

    @staticmethod
    def gerar_matricula(nome, cpf, data_admissao, codigo_cargo, comissao) -> int:
        
        # AO FINAL REMOVER DAQUI A CONSULTA E COLOCAR UMA CONSULTA GERAL PARA TODOS

        user = os.getenv('USER')
        password = os.getenv('PASSWORD')
        host = os.getenv('HOST')
        database = os.getenv('DATABASE')

        cnx = mysql.connector.connect(user=user,
                                      password=password,
                                      host=host,
                                      database=database)
        
        # TERMINA AQUI A CONSULTA
        
        cursor = cnx.cursor()
        
        insert_funcionario = (
            f"INSERT INTO funcionarios (nome, cpf, data_admissao, codigo_cargo, comissao) VALUES ('{nome}', {cpf}, '{data_admissao}', {codigo_cargo}, {comissao});")

        cursor.execute(insert_funcionario)
        cnx.commit()

        cursor = cnx.cursor()

        consultar_matricula = (
            f"SELECT matricula FROM funcionarios WHERE cpf = {cpf} AND data_admissao = '{data_admissao}';")

        cursor.execute(consultar_matricula)

        matricula = cursor.fetchall()[0][0]

        cnx.close()

        return matricula

    @property
    def matricula(self):
        return self.__matricula

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_admissao(self) -> str:
        return self.__data_admissao

    @property
    def codigo_cargo(self) -> int:
        return self.__codigo_cargo

    @property
    def comissao(self) -> bool:
        return self.__comissao