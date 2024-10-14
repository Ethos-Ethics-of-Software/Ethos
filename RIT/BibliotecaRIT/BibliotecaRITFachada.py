from copy import deepcopy
from RIT.BibliotecaRIT.Sources.Requisicao import Requisicao
from RIT.BibliotecaRIT.Sources.Requisicao import Requisicao
from RIT.BibliotecaRIT.Sources.controladoras.ControladoraExportacaoDados import ControladoraExportacaoDados
from RIT.BibliotecaRIT.Sources.controladoras.ControladoraExtracaoDados import ControladoraExtracaoDados
from RIT.BibliotecaRIT.Sources.controladoras.ControladoraPreProcessamento import ControladoraPreProcessamento
from RIT.BibliotecaRIT.Sources.entidades.Projeto import Projeto
from RIT.BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorData import VisaoRelevanciaTematicaPorData
from RIT.BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorAutor import VisaoRelevanciaTematicaPorAutor


class BibliotecaRITFachada:

    @classmethod
    def initTokens(cls, tokens):
        Requisicao.init_tokens(tokens=tokens)
    
    @classmethod
    def extrairDadosGitHub(cls,usuario, repositorio, visao=3, arg="", pagInicial=1):

        tipoIssue = visao if visao < 4 else 3
        ControladoraExtracaoDados.setFiltroExtracaoPorTipoIssue(tipoIssue)
        qtdPaginas = ControladoraExtracaoDados.numeroPaginas(usuario,repositorio)
        for i in range(pagInicial,qtdPaginas+1):
            print(f'-- Extraindo os dados da página {i}/{qtdPaginas} do repositório {repositorio} --')
            projeto = ControladoraExtracaoDados.requisicaoIssuesPorPagina(usuario,repositorio,i)
            
            print(f'-- Pré-processando os dados da página {i}/{qtdPaginas} do repositório {repositorio} --')
            projetoPreProcessado = cls.__preProcessarProjeto(projeto)
     
            print(f'-- Exportando dados da página {i}/{qtdPaginas} do repositório {repositorio} --')
            cls.__gerarCSVGitHub(projeto, visao, i, arg)
            
            print('\033[92m' + f'Página {i}/{qtdPaginas} do repositório {repositorio} finalizada' + '\033[0m')
            print()

    @staticmethod
    def __preProcessarProjeto(projeto:Projeto)-> Projeto:
        copiaProjeto = deepcopy(projeto)
        preProcessamento = ControladoraPreProcessamento
        for i in range(len(projeto.topicos)):
            topico = copiaProjeto.topicos[i]
            descricaoPreProcessada = preProcessamento.processar(topico.descricao)[0]
            topico.setDescricao(descricaoPreProcessada)
            for j in range(len(topico.listaComentarios)):
                comentario = topico.listaComentarios[j]
                comentarioPreProcessado, tags = preProcessamento.processar(comentario.mensagem)
                projeto.topicos[i].listaComentarios[j].setTags(tags)
                comentario.setMensagem(comentarioPreProcessado)
        return copiaProjeto

    @staticmethod
    def __gerarCSVGitHub(projeto:Projeto, visao,numPagina, arg ):
        if(visao == 4):
            ControladoraExportacaoDados.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorAutor)
        elif(visao == 5):
            ControladoraExportacaoDados.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorData)
        return ControladoraExportacaoDados.gerarCSVs(projeto,visao,numPagina,arg)
    
    
