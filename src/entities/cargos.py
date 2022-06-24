from abc import ABC, abstractmethod


class Cargos(ABC):

    @abstractmethod
    def nome(self):
        """
        variável de classe referente ao nome do cargo.
        """    
        return ...

    @abstractmethod
    def codigo(self):
        """
        variável de classe referente ao código do cargo.
        """
        return ...
    
    @abstractmethod
    def atribuicao(self):
        """
        variável de classe referente à atribuição do cargo.
        """
        return ...
    
    
    @abstractmethod
    def salarioBase(self):
        """
        variável de classe referente ao salário do cargo.
        """
        return ...
    
    @abstractmethod
    def comissao(self):
        """
        variável de classe referente ao comissao do cargo.
        """
        return ...
    