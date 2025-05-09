from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoStrategy import PreProcessamentoStrategy
from RIT.BibliotecaRIT.Sources.enums.EnumTag import EnumTag
import re


class PreProcessamentoImagemMarkdown(PreProcessamentoStrategy):
    _regExp = "!\[[^\]]*\]\((?:\S+)\s*(\"(?:\\.|[^\"\\\])*\"|'(?:\\.|[^'\\\])*'|\((?:\\.|[^)\\\])*\)*)?\)"

    @classmethod
    def contem(cls, string: str) -> bool:
        return True if re.search(cls._regExp, string) is not None else False

    @staticmethod
    def getTag() -> EnumTag:
        return EnumTag.IMAGEM

    @classmethod
    def remover(cls,string:str) -> str:
        return re.sub(cls._regExp,'',string)
