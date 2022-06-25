from business.cadastros import Cadastro
from entities.holerite_unico import Holerite_Unico

class Holerite():
    
    def __init__(self, mes_ano: str):
        self.__mes_ano = mes_ano        
        
    @property
    def mes_ano(self) -> str:
        return self.__mes_ano
    
    @staticmethod
    def gerar_todos_holerites(cadastro: Cadastro, mes_ano: str) -> None:
        lista_funcionarios = cadastro.listar()
        for matricula, nome in lista_funcionarios:
            holerite = Holerite_Unico(mes_ano, matricula, 0)
            holerite.gerar_holerite()
