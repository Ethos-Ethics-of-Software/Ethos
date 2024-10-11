from abc import ABC, abstractmethod

from RIT.BibliotecaRIT.Sources.entidades.Comentario import Comentario

class VisaoStrategy(ABC):

    @staticmethod
    @abstractmethod
    def exportarComentariosGitHub(idTopico:int,comentario:Comentario,csvFile,arg:str):
        pass