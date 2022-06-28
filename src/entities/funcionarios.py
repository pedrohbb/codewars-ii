from db import connection
import mysql.connector


class Funcionario():

    def __init__(self, nome: str, cpf: str, data_admissao: str, codigo_cargo: int, comissao: bool):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_admissao: str = data_admissao
        self.__codigo_cargo: int = codigo_cargo
        self.__comissao: bool = comissao
        self.__matricula: int = Funcionario.matricular(
            nome, cpf, data_admissao, codigo_cargo, comissao)

    @staticmethod
    def matricular(nome: str, cpf: str, data_admissao: str, codigo_cargo: int, comissao: str) -> int:

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        insert_funcionario = (f"""INSERT INTO funcionarios (nome, cpf, data_admissao, codigo_cargo, comissao)\
                            VALUES ('{nome}', '{cpf}', '{data_admissao}', {codigo_cargo}, '{comissao}');\
                            """)

        cursor.execute(insert_funcionario)

        cnx.commit()

        cursor = cnx.cursor()

        consultar_matricula = (f"""SELECT matricula FROM funcionarios WHERE cpf = '{str(cpf)}'\
                            AND data_admissao = '{data_admissao}';""")

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
