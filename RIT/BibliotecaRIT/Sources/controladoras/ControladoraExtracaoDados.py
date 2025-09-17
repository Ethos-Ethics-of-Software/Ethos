from RIT.BibliotecaRIT.Sources.Requisicao import Requisicao
from RIT.BibliotecaRIT.Sources.entidades.Comentario import Comentario
from RIT.BibliotecaRIT.Sources.entidades.Projeto import Projeto
from RIT.BibliotecaRIT.Sources.entidades.Topico import Topico
from RIT.BibliotecaRIT.Sources.estrategias.extracao.FiltroExtracaoIssuesAbertasFechadas import FiltroExtracaoIssuesAbertasFechadas
from RIT.BibliotecaRIT.Sources.estrategias.extracao.FiltroExtracaoIssuesAbertas import FiltroExtracaoIssuesAbertas
from RIT.BibliotecaRIT.Sources.estrategias.extracao.FiltroExtracaoIssuesFechadas import FiltroExtracaoIssuesFechadas



class ControladoraExtracaoDados:
    _requisicao = Requisicao
    _filtroExtracao = FiltroExtracaoIssuesAbertas
    
    @classmethod
    def setFiltroExtracaoPorTipoIssue(cls,tipoIssue):
        if tipoIssue == 2:
            cls._filtroExtracao=FiltroExtracaoIssuesFechadas
        elif tipoIssue == 3:
           cls._filtroExtracao =FiltroExtracaoIssuesAbertasFechadas
    
    @classmethod
    def numeroPaginas(cls, usuario, repositorio):
        url = cls._filtroExtracao.urlNumeroPaginas(usuario, repositorio)
        response = cls._requisicao.request(url=url)

        if "last" in response.links:
            return int(response.links['last']['url'].partition("&page=")[-1])
        elif "next" in response.links:
            paginas = 1
            while "next" in response.links:
                paginas += 1
                response = cls._requisicao.request(url=response.links["next"]["url"])
            return paginas
        else:
            return 1
    
    @classmethod
    def requisicaoIssuesPorPagina(cls,usuario, repositorio, numeroPagina) -> Projeto:
        url = cls._filtroExtracao.urlRequisicaoIssuesPorPagina(usuario,repositorio,numeroPagina)
        response = cls._requisicao.request(url=url).json()
        topicos=[]
        if response is not None:
            dadosIssues = response
            for j in range(len(dadosIssues)):
                # Inicializando uma Issue
                topico = Topico( dadosIssues[j]['created_at'], dadosIssues[j]['title'], dadosIssues[j]['body'], dadosIssues[j]['number'] ,dadosIssues[j]['html_url'],dadosIssues[j]['id'])

                # Requisitando os Comentários de cada Issue
                dadosComentarios = cls.__requisicaoComentariosPorIssue(usuario, repositorio, dadosIssues[j]['number'])
                comentarios = []

                for k in range(len(dadosComentarios)):
                    # Inserindo os Dados dos Comentários da Issue
                    comentario = Comentario(dadosComentarios[k]['id'], dadosComentarios[k]['user']['login'], dadosComentarios[k]['body'], dadosComentarios[k]['created_at'])
                    comentarios.append(comentario)

                # Inserindo Dados da Issue
                # Instanciando os Comentários na Issue, e Salvando a Issue na Lista
                topico.inserirComentarios(comentarios)
                topicos.append(topico)
            return Projeto(usuario, repositorio, topicos)        
        
    
    @classmethod
    def __requisicaoComentariosPorIssue(cls, usuario, repositorio, numeroIssue):
        url = 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues/'+str(numeroIssue)+'/comments'
        response = cls._requisicao.request(url=url).json()
        if response is not None:
            return response
  