from abc import ABC, abstractmethod

from RIT.BibliotecaRIT.Sources.enums.EnumTag import EnumTag

class PreProcessamentoStrategy(ABC):
    @classmethod
    @abstractmethod
    def contem(cls,string:str) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def getTag() -> EnumTag:
        pass
    
    @classmethod
    @abstractmethod
    def remover(cls,string:str) -> str:
        pass

