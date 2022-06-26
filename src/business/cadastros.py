import mysql.connector
from mysqlx import IntegrityError
from docs.db import connection
from src.entities.funcionarios import Funcionario


class Cadastro():

    def inserir(self) -> None:

        nome = input('Digite o nome do funcionário: ')
        cpf = int(input('Digite o CPF do funcionário: '))

        try:
            self.consultar(cpf)
            raise IntegrityError("Esse CPF já está cadastrado!")

        except IndexError:
            data_admissao = input('Digite a data de admissão do funcionário: ')
            codigo_cargo = int(input('Digite o cargo do funcionário: '))
            comissao = input('O funcionário possui comissão? S ou N: ')
            comissao = list(
                map(lambda x: 1 if comissao == 'S' else 0, comissao))[0]

        Funcionario(nome, cpf, data_admissao, codigo_cargo, comissao)

    def excluir(self, chave: int) -> None:
        """
        :chave: int - matrícula ou cpf
        """

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()
        assinatura_chave = Cadastro.assinatura(chave)

        try:
            self.consultar(chave)

            deletar_funcionario = (
                f"""DELETE FROM funcionarios WHERE {assinatura_chave} =
                {list(map(lambda x: str(chave) if x == 'cpf' else chave, assinatura_chave))[0]};""")

            cursor.execute(deletar_funcionario)

            cnx.commit()

            cnx.close()

            print('Funcionário excluído com sucesso!')
        
        except IndexError:
            print('Funcionário inexistente no cadastro. ')

    def consultar(self, chave: int):
        """
        :chave: int - matrícula ou cpf
        """

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        consultar_matricula = (f"""
                            SELECT matricula, nome, cpf, data_admissao, codigo_cargo, comissao 
                            FROM funcionarios WHERE {Cadastro.assinatura(chave)} = {chave};
        """)

        cursor.execute(consultar_matricula)

        try:
            query = cursor.fetchall()[0]
            campo = ['matricula', 'nome', 'cpf',
                     'data_admissao', 'codigo_cargo', 'comissao']

            resultado_consulta = {}
            for i in range(len(campo)):
                resultado_consulta[campo[i]] = query[i]

            cnx.close()

            return resultado_consulta

        except IndexError:
            raise IndexError('Funcionário inexistente no cadastro. ')

    def alterar(self):

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        chave = int(input("Insira a matrícula ou cpf do funcionário: "))

        try:
            self.consultar(chave)

            campos = ['nome', 'cpf',
                      'cargo', 'data_admissao', 'comissao']
            campo = campos[int(input(f"""
                            Digite 1 para modificar o NOME,
                                    2 para modificar o CPF,
                                    3 para modificar o CARGO,
                                    4 para modificar a DATA DE ADMISSÃO ou
                                    5 para modificar o RECEBER COMISSÃO:
            """)) - 1]

            novo_dado = input(f"{campo.capitalize()}: ")

            alterar_funcionario = (
                f"UPDATE funcionarios SET {campo} = '{novo_dado}' WHERE {Cadastro.assinatura(chave)} = {chave};")

            cursor.execute(alterar_funcionario)

            cnx.commit()

            cnx.close()

        except IndexError:
            print('Funcionário inexistente!')

    def listar(self):

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        consultar_dados = ("SELECT * FROM funcionarios;")

        cursor.execute(consultar_dados)

        resultado_consulta = cursor.fetchall()

        listagem = {}
        for elem in resultado_consulta:
            listagem[elem[0]] = elem[1]

        cnx.close()

        return listagem

    @staticmethod
    def assinatura(chave: int):

        if len(str(chave)) == 6:
            assinatura = 'matricula'
        if len(str(chave)) == 11:
            assinatura = 'cpf'
        return assinatura
