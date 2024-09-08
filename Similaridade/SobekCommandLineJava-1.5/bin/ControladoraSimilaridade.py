from SimilaridadeCossenos import SimilaridadeCossenos
from SimilaridadeGrafos import SimilaridadeGrafos
from controladoraSOBEK import ControladoraSOBEK

class ControladoraSimilaridade:
    
    @classmethod
    def calcularSimilaridade(cls, texto1, texto2, tipoCalculo):
        
        if (tipoCalculo == 1):
            similaridade = SimilaridadeCossenos.simCossenos(texto1, texto2)
        
        if (tipoCalculo == 2):
            print("------------------------------------------------------------")
            print("Português - pt")
            print("Inglês - en")
            idioma = input("Digite o idioma do texto: ")
            if (idioma != "pt" and idioma != "en"):
                print("Idioma Inválido!")
                return
            print("------------------------------------------------------------")
            
            texto1 = ControladoraSOBEK.gerarGrafo(texto1, idioma)
            texto2 = ControladoraSOBEK.gerarGrafo(texto2, idioma)
            similaridade = SimilaridadeGrafos.simGrafos(texto1, texto2, idioma)
        
        return similaridade
        