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
        comissao = list(map(lambda x: 1 if comissao == 'S' else 0, comissao))[0]
        
        Funcionario(nome, cpf, data_admissao, codigo_cargo, comissao)
        
        
        
        # cnx = mysql.connector.connect(user='user', password='password',
        #                               host='host',
        #                               database='codewars-ii')

        # cursor = cnx.cursor()
        
        # insert_funcionario = (
        #     f"""INSERT INTO funcionarios (nome, cpf, data_admissao, codigo_cargo, comissao) 
        #     VALUES ('{nome}', {funcionario.cpf}, '{funcionario.data_admissao}', {funcionario.codigo_cargo},{funcionario.comissao});""")

        # cursor.execute(insert_funcionario)
        # cnx.commit()

        # cursor = cnx.cursor()



    def exclusao(self, chave: Funcionario or int) -> None:
        cnx = mysql.connector.connect(user='user', password='password',
                                      host='host',
                                      database='codewars-ii')
        cursor = cnx.cursor()
        
        if isinstance(chave, Funcionario):
            chave = chave.matricula

        deletar_funcionario = (f"DELETE FROM funcionarios WHERE matricula = {chave}")

        cursor.execute(deletar_funcionario, [chave])

        cnx.commit()

        cursor.close()
        cnx.close()

    def consulta(self, funcionario: Funcionario):
        cnx = mysql.connector.connect(user='user', password='password',
                                      host='host',
                                      database='codewars-ii')
        cursor = cnx.cursor()
       
        consultar_matricula = (
            f"SELECT matricula FROM funcionarios WHERE cpf = {cpf} AND data_admissao = '{data_admissao}';")

        cursor.execute(consultar_funcionario, {
            "nome": funcionario.nome,
            "cpf": funcionario.cpf,
            "data_admissao": funcionario.data_admissao,
            "codigo_cargo": funcionario.cpf,
            "comissao": funcionario.comissao
        })

        cnx.commit()

        cursor.close()
        cnx.close()

    
    # def consulta(self, chave: str or int):
    #     return self.lista[]

    # def alteracao(self, chave: str or int):

    
    # def assinatura(chave: str or int):
    #     if isinstance(chave, str):
    #         nome = chave
    #         result_query = consultas.inseri