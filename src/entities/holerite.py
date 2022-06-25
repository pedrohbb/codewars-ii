import os
import mysql.connector

class Holerite():
  
  def __init__(self, mes_ano: str, matricula: int, faltas: float, inss: float, irrf: float):
    self.__mes_ano: str = mes_ano
    self.__matricula: int = matricula
    self.__faltas: float = faltas
    self.__inss: float = inss
    self.__irrf: float = irrf
    
  @staticmethod
  def calcular_inss(matricula: int):
    
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
        
        consultar_matricula = (
            f";")

        cursor.execute(consultar_matricula)

        matricula = cursor.fetchall()[0][0]

        cnx.close()

        return matricula

