from RIT.BibliotecaRIT.Sources.entidades.Tags import Tags
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoCaminho import PreProcessamentoCaminho
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoCodigoInlineHTML import PreProcessamentoCodigoInlineHTML
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoCodigoInlineMardown import PreProcessamentoCodigoInlineMarkdown
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoTrechoCodigoHTML import PreProcessamentoTrechoCodigoHTML
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoDetailsHTML import  PreProcessamentoDetailsHTML
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoTrechoCodigoMarkdown import  PreProcessamentoTrechoCodigoMarkdown
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoEmail import PreProcessamentoEmail
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoEmoji import PreProcessamentoEmoji
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.imagem.PreProcessamentoImagemHTML import PreProcessamentoImagemHTML
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoNomeUsuario import PreProcessamentoNomeUsuario
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.imagem.PreProcessamentoImagemMarkdown import  PreProcessamentoImagemMarkdown
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.url.PreProcessamentoURL import PreProcessamentoURL
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.url.PreProcessamentoURLHTML import PreProcessamentoURLHTML
from RIT.BibliotecaRIT.Sources.estrategias.preProcessamento.url.PreProcessamentoURLMarkdown import PreProcessamentoURLMarkdown

class ControladoraPreProcessamento:
    # **CUIDADO**: Alterar a sequência pode alterar o resultado do pré-processamento
    _estrategias = [
        PreProcessamentoEmail,
        PreProcessamentoEmoji,
        PreProcessamentoNomeUsuario,
        PreProcessamentoImagemHTML,
        PreProcessamentoImagemMarkdown,
        PreProcessamentoDetailsHTML,
        PreProcessamentoTrechoCodigoHTML,
        PreProcessamentoCodigoInlineHTML,
        PreProcessamentoTrechoCodigoMarkdown,
        PreProcessamentoCodigoInlineMarkdown,
        PreProcessamentoURLMarkdown,
        PreProcessamentoURLHTML,
        PreProcessamentoURL,
        PreProcessamentoCaminho, 
    ]

    @classmethod
    def processar(cls, mensagem: str):
        tags = Tags()
        for estrategia in cls._estrategias:
            if estrategia.contem(mensagem):
                tag = estrategia.getTag()
                tags.addTag(tag)
                mensagem = estrategia.remover(
                    mensagem)
        return mensagem, tags

