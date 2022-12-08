class Noticia:
    def __init__(self, noticia) -> None:
        self.id: int = noticia["id"]
        self.assunto: str = noticia["assunto"]
        self.data: tuple(int) = noticia["data"]
        self.categoria: str = noticia["categoria"]
        self.texto: str = noticia["texto"]
