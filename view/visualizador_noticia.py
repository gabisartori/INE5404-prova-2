from view.visualizador import Visualizador
from control.controlador_noticia import ControladorNoticia
import tkinter as tk

class VisualizadorNoticia(Visualizador):
    def __init__(self, parent, root=None):
        super().__init__(parent, root)
        self.__id_noticia: int = 0
        self.controlador_noticia = ControladorNoticia()
        self.controlador_noticia.conectar_noticia(self.__id_noticia)
    
    def get_id_noticia(self) -> int:
        return self.__id_noticia

    def set_id_noticia(self, id_noticia) -> None:
        self.__id_noticia = id_noticia

    def construir(self):
        # noticia = self.controlador_noticia.get_noticia()
        # tk.Label(self._root, text=noticia.get_assunto()).pack()
        pass