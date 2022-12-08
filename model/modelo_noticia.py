import datetime


class Noticia:
    def __init__(self, noticia) -> None:
        self.id: int = noticia["id"]
        self.assunto: str = noticia["assunto"]
        self.data: datetime = datetime.datetime(*noticia["data"])
        self.categoria: str = noticia["categoria"]
        self.texto: str = noticia["texto"]

    def get_id(self) -> int:
        return self.id
    
    def get_assunto(self) -> str:
        return self.assunto
    
    def get_data(self) -> datetime:
        return self.data
    
    def get_categoria(self) -> str:
        return self.categoria
    
    def get_texto(self) -> str:
        return self.texto
