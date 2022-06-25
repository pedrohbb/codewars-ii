import os
import mysql.connector
from entities.funcionarios import Funcionario

class Cadastro():

    def __init__(self):
        self.__lista = []
    
    @property
    def lista(self):
        return self.__lista
    
    def inserir(self) -> None:
        
        nome = input('Digite o nome do funcionário: ')
        cpf = int(input('Digite o CPF do funcionário: '))
        data_admissao = input('Digite a data de admissão do funcionário: ')
        codigo_cargo = int(input('Digite o cargo do funcionário: '))
        comissao = input('O funcionário possui comissão? S ou N: ')
        comissao = list(map(lambda x: 1 if x == 'S' else 0, comissao))[0]
        
        Funcionario(nome, cpf, data_admissao, codigo_cargo, comissao)

    def excluir(self, chave: int or str) -> None:
        cnx = mysql.connector.connect(user='user', password='password',
                                      host='host',
                                      database='codewars-ii')
        cursor = cnx.cursor()
        
        if len(str(chave)) == 6:
            assinatura = 'matricula'
        if len(str(chave)) == 11:
            assinatura = 'cpf'
        if isinstance(chave, str):
            assinatura = 'nome'

        deletar_funcionario = (f"DELETE FROM funcionarios WHERE {assinatura} = {chave}")

        cursor.execute(deletar_funcionario)

        cnx.commit()

        cnx.close()

    def consultar(self, chave: int):
        cnx = mysql.connector.connect(user='user', password='password',
                                      host='host',
                                      database='code_wars_ii')
        cursor = cnx.cursor()

        if len(str(chave)) == 6:
            assinatura = 'matricula'
        if len(str(chave)) == 11:
            assinatura = 'cpf'

        consultar_matricula = (f"""
                            SELECT matricula, nome, cpf, cargo, salario_base, comissao 
                            FROM funcionarios WHERE {assinatura} = {chave};
        """)

        cursor.execute(consultar_matricula)

        query = cursor.fetchall()[0]

        campo = ['matricula', 'nome', 'cpf', 'cargo', 'data_admissao', 'comissao']

        resultado_consulta = {}
        for i in range(len(campo)):
            resultado_consulta[campo[i]] = query[i]
            
        cnx.close()

        return resultado_consulta

    def alterar(self):

        cnx = mysql.connector.connect(user='user', password='password',
                                      host='host',
                                      database='codewars-ii')
        cursor = cnx.cursor()
        
        chave = int(input("Insira a matrícula ou cpf do funcionário: "))

        campo = ['matricula', 'nome', 'cpf', 'cargo', 'data_admissao', 'comissao']
        campo = campo[int(input(f"""
                         Digite 1 para modificar a MATRÍCULA
                         Digite 2 para modificar o NOME
                         Digite 3 para modificar o CPF
                         Digite 4 para modificar o CARGO
                         Digite 5 para modificar a DATA DE ADMISSÃO
                         Digite 6 para modificar o RECEBER COMISSÃO
        """)) - 1]

        novo_dado = input(f"{campo.capitalize()}: ")

        if len(str(chave)) == 6:
            assinatura = 'matricula'
        if len(str(chave)) == 11:
            assinatura = 'cpf'

        if campo == 'cpf' or 'matricula':
            alterar_funcionario = (f"UPDATE funcionarios SET {campo} = {novo_dado} WHERE {assinatura} = {chave};")
        else:
            alterar_funcionario = (f"UPDATE funcionarios SET {campo} = '{novo_dado}' WHERE {assinatura} = {chave};")
        
        cursor.execute(alterar_funcionario)

        cnx.commit()

        cnx.close()


    def listagem(self):

        cnx = mysql.connector.connect(user='user', password='password',
                                    host='host',
                                    database='code_wars_ii')
        cursor = cnx.cursor()

        if len(str(chave)) == 6:
            assinatura = 'matricula'
        if len(str(chave)) == 11:
            assinatura = 'cpf'

        consultar_dados = (f"""SELECT matricula, nome, cpf, cargo, salario_base, comissao 
                                FROM funcionarios WHERE {assinatura} = {chave};""")

        cursor.execute(consultar_dados)

        resultado_consulta = cursor.fetchall()

        cnx.close()

        return resultado_consulta


