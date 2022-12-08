from model.modelo_noticia import Noticia
import json

class ControladorNoticia:
    def __init__(self):
        self.__noticia: Noticia | None = None

    def conectar_noticia(self, noticia_id: int) -> Noticia | str:
        try:
            with open("db/noticias.json", "r") as arquivo:
                noticias = json.load(arquivo)
                for noticia in noticias:
                    if noticia["id"] == noticia_id:
                        self.__noticia = Noticia(noticia)
                        return self.__noticia
        except FileNotFoundError:
            return "Notícia não encontrada."
    
    def get_noticia(self) -> Noticia | None:
        return self.__noticia
    