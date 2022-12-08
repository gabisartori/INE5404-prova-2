class Noticia:
    def __init__(self, noticia) -> None:
        self.__id: int = noticia["id"]
        self.__assunto: str = noticia["assunto"]
        self.__texto: str = noticia["texto"]
        self.__data: int = noticia["data"]
        self.__categoria: str = noticia["categoria"]
