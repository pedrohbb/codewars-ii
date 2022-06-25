from entities.matricula import Matricula

class Funcionario(Matricula):

    def __init__(self, matricula: int, nome: str, cpf: str, data_admissao: str, codigo_cargo: int, comissao: bool):
        super().__init__(matricula)
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_admissao: str = data_admissao
        self.__codigo_cargo: int = codigo_cargo
        self.__comissao: bool = comissao
        
    @property
    def matricula(self) -> str:
        setattr(self, 'matricula', )
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



