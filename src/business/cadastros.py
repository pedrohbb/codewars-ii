import mysql.connector
from db import connection
from src.entities.funcionarios import Funcionario
from src.exceptions.not_found_error import NotFoundError
from src.exceptions.duplicated_entry_error import DuplicatedEntryError
from src.exceptions.not_valid_format_error import NotValidFormatError


class Cadastro():

    def consultar(self, chave: int):
        """
        :chave: int - matrícula ou cpf
        """

        chave_tipo = Cadastro.validacao(chave)

        if chave_tipo == 1: 
            consultar_chave = (f"""\
                            SELECT matricula, nome, cpf, data_admissao, codigo_cargo, comissao\
                            FROM funcionarios WHERE cpf = '{chave}';\
        """)
        elif chave_tipo == 5:
            consultar_chave = (f"""\
                            SELECT matricula, nome, cpf, data_admissao, codigo_cargo, comissao\
                            FROM funcionarios WHERE matricula = {chave};\
        """)
        else:
            raise NotValidFormatError("Matrícula/cpf não reconhecida(o)")

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        cursor.execute(consultar_chave)

        query = cursor.fetchall()
        
        if len(query) == 0:
            raise NotFoundError('Funcionário inexistente no cadastro.') 
        else:
            query = query[0]
        
        campos = ['matricula', 'nome', 'cpf', 'data_admissao', 'codigo_cargo', 'comissao']
        resultado_consulta = {}
        for i in range(len(campos)):
            resultado_consulta[campos[i]] = query[i]

        cnx.close()

        return resultado_consulta

    def inserir(self, nome, cpf, data_admissao, codigo_cargo, comissao) -> None:  

        try:
            self.consultar(cpf)
            raise DuplicatedEntryError("Esse CPF já está cadastrado!")
        except NotFoundError:
            campos = (nome, cpf, data_admissao, codigo_cargo, comissao)
            for atrib in campos:
                if Cadastro.validacao(atrib) == -1:
                    raise NotValidFormatError(f"{atrib} em formato inválido")
            Funcionario(*campos)
            print("Funcionario cadastrado com sucesso")

    def excluir(self, chave: int) -> None:
        """
        :chave: int - matrícula ou cpf
        """

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        self.consultar(chave)

        chave_tipo = Cadastro.validacao(chave)

        if chave_tipo == 1: 
            deletar_funcionario = (f"DELETE FROM funcionarios WHERE cpf = '{chave}';")
        elif chave_tipo == 5:
            deletar_funcionario = (f"DELETE FROM funcionarios WHERE matricula = {chave};")
        else:
            raise NotValidFormatError("Matrícula/cpf não reconhecida(o)")

        cursor.execute(deletar_funcionario)

        cnx.commit()

        cnx.close()

        print('Funcionário excluído com sucesso!')


    def alterar(self, chave, campo, dado):

        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        self.consultar(chave)

        chave_tipo = Cadastro.validacao(chave)

        dado_tipo = Cadastro.validacao(dado)

        if dado_tipo == 1: 
            alterar_funcionario = (f"UPDATE funcionarios SET {campo} = '{dado}' WHERE cpf = '{chave}';")
        elif chave_tipo == 5:
            alterar_funcionario = (f"UPDATE funcionarios SET {campo} = {dado} WHERE matricula = {chave};")
        else:
            raise NotValidFormatError("Matrícula/cpf não reconhecida(o)")

        cursor.execute(alterar_funcionario)

        cnx.commit()

        cnx.close()

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
    def validacao(entry):
        nome = 0
        cpf = 1
        date = 2
        cargo = 3
        comissao = 4
        matricula = 5
        invalido = -1
        
        entry = str(entry)

        if entry == '1' or entry == '0':
            return comissao

        algs = set("0123456789")

        if set(entry).issubset(algs):
            if len(entry) == 2:
                return cargo
            elif len(entry) == 6:
                return matricula
            elif len(entry) == 11:
                return cpf
            else:
                return invalido
        
        if set(entry).issubset(algs.union(set("-"))):
            if entry.count('-') == 2:
                if entry[4] == entry[7] == '-':
                    return date           

        noums_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "'" + " "
        noums_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
        noums_chars += ("ãõáéíóúäëïöü" + "ãõáéíóúäëïöü".upper())
        noums_chars = set(noums_chars)

        if set(entry).issubset(noums_chars):
            if set(entry).issubset(set("'" + " ")):
                return invalido
            else:
                return nome
        else:
            return invalido