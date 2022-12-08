from model.modelo_noticia import Noticia
import datetime
import json

class ControladorNoticia:
    def __init__(self):
        # Composição
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
    
    def buscar_noticias_por_filtro(self, filtros):
        try:
            inicio = datetime.datetime(*[int(a) for a in filtros["inicio"]])
        except:
            inicio = None
        try:
            fim = datetime.datetime(*[int(a) for a in filtros["fim"]])
        except:
            fim = None
        assunto = filtros["assunto"]
        categoria = filtros["categoria"]

        todas = self.get_noticias()
        if isinstance(todas, str):
            return todas

        if assunto:
            todas = [noticia for noticia in todas if assunto.lower() in noticia.assunto.lower()]

        if categoria and categoria != "Escolha uma categoria":
            todas = [noticia for noticia in todas if noticia.categoria.lower() == categoria.lower()]

        if inicio:
            todas = [noticia for noticia in todas if noticia.data >= inicio]

        if fim:
            todas = [noticia for noticia in todas if noticia.data <= fim]
        return todas

    @staticmethod
    def get_noticias():
        try:
            with open("db/noticias.json", "r") as arquivo:
                noticias = json.load(arquivo)
                return [Noticia(noticia) for noticia in noticias]
        except FileNotFoundError:
            return "DB não encontrado."