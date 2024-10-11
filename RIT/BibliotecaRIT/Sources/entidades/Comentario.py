from RIT.BibliotecaRIT.Sources.entidades.Tags import Tags

class Comentario:
    def __init__(self, id, loginAutor, mensagem, data):
        self._id = id
        self._loginAutor = loginAutor
        self._mensagem = mensagem
        self._data = data
        self._tags = Tags()
          
    
    def setTags(self,tags:Tags):
        self._tags = tags
    
    #@property

    @property
    def mensagem(self):
        return self._mensagem
    
    def setMensagem(self,mensagem:str):
        self._mensagem = mensagem
    
    @property
    def data(self):
        return self._data
    
    @property
    def loginAutor(self):
        return self._loginAutor
    
    @property
    def id(self):
        return self._id
    
    @property
    def tags(self):
        return self._tags

    def tagsToString(self):
        return self._tags.toString()