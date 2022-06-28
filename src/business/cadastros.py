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
            count = 0
            for atrib in campos:
                if Cadastro.validacao(atrib) != count:
                    raise NotValidFormatError(f"{atrib} - campo em formato inválido")
                count += 1
            Funcionario(*campos)
            print("Funcionario cadastrado com sucesso\n")

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
            raise NotValidFormatError("Matrícula/cpf não reconhecida(o)\n")

        cursor.execute(deletar_funcionario)

        cnx.commit()

        cnx.close()

        print('Funcionário excluído com sucesso!\n')


    def alterar(self, chave, campo, dado):
        campos = ['nome', 'cpf', 'data_admissao', 'codigo_cargo', 'comissao']
        aux = [0,1,2,3,4]
        campos = dict(list(zip(campos,aux)))
        campos['invalido'] = -1


        cnx = mysql.connector.connect(**connection.config)
        cursor = cnx.cursor()

        self.consultar(chave)

        chave_tipo = Cadastro.validacao(chave)

        if chave_tipo == 1: 
            alterar_funcionario = (f"UPDATE funcionarios SET {campo} = '{dado}' WHERE cpf = '{chave}';")
        elif chave_tipo == 5:
            alterar_funcionario = (f"UPDATE funcionarios SET {campo} = {dado} WHERE matricula = {chave};")
        else:
            raise NotValidFormatError("Matrícula/cpf não reconhecida(o)")

        dado_tipo = Cadastro.validacao(dado)

        if campos[campo] != dado_tipo:
            raise NotValidFormatError(f"{campo} em formato inválido!")

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
        data_admissao = 2
        codigo_cargo = 3
        comissao = 4
        matricula = 5
        mes_ano = 6
        faltas = 7
        invalido = -1

        if isinstance(entry, int):
            if entry >= 100000:
                return matricula
        
        if isinstance(entry, float):
            if 0.03 <= entry <= 0.1:    
                return comissao
            if entry == 0 or (0.1 < entry <= 22.5):
                return faltas

        if entry == '1' or entry == '0':
            return comissao

        algs = set("0123456789")

        if set(entry).issubset(algs):
            if len(entry) == 2:
                return codigo_cargo
            elif len(entry) == 6:
                return matricula
            elif len(entry) == 11:
                return cpf
            else:
                return invalido
        
        if set(entry).issubset(algs.union(set("-"))):
            if (entry[4] == entry[7] == '-') and len(entry) == 10:
                return data_admissao           

        if set(entry).issubset(algs.union(set("/"))):
            if entry[2] == "/" and len(entry) == 7:
                return mes_ano

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