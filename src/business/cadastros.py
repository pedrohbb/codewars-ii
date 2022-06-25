from entities.funcionarios import Funcionario


class Cadastro():

    def __init__(self):
        self.__lista = []

    def inserir(self, funcionario: Funcionario):
        self.__lista.append(funcionario)
