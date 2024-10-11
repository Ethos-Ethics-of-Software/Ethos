from RIT.BibliotecaRIT.Sources.entidades.Comentario import Comentario
from RIT.BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy


class VisaoRelevanciaTematicaPorAutor(VisaoStrategy):

    @staticmethod
    def exportarComentariosGitHub(idTopico:int, comentario:Comentario, csvFile, arg:str):

        if(comentario.loginAutor == arg):
            csvFile.writerow([idTopico, comentario.id, comentario.mensagem, comentario.data,
                                comentario.loginAutor,comentario.tagsToString()])