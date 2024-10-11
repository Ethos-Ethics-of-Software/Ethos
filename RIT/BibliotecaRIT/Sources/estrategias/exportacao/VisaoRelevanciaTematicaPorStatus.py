from RIT.BibliotecaRIT.Sources.entidades.Comentario import Comentario
from RIT.BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy

class VisaoRelevanciaTematicaPorStatus(VisaoStrategy):
   
   @staticmethod
   def exportarComentariosGitHub(idTopico: int, comentario: Comentario, csvFile, arg: str):
         csvFile.writerow([idTopico,comentario.id, comentario.mensagem, comentario.data,
                              comentario.loginAutor,comentario.tagsToString()])
