import datetime


class Noticia:
    def __init__(self, noticia) -> None:
        self.id: int = noticia["id"]
        self.assunto: str = noticia["assunto"]
        self.data: datetime = datetime.datetime(*noticia["data"])
        self.categoria: str = noticia["categoria"]
        self.texto: str = noticia["texto"]
