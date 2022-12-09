from view.visualizador import Visualizador
from control.controlador_noticia import ControladorNoticia
import tkinter as tk

class VisualizadorNoticia(Visualizador):
    def __init__(self, id_noticia, parent, root=None):
        super().__init__(parent, root)
        self.__id_noticia: int = id_noticia
        self.controlador_noticia = ControladorNoticia()
        self.controlador_noticia.conectar_noticia(self.__id_noticia)
    
    def get_id_noticia(self) -> int:
        return self.__id_noticia

    def set_id_noticia(self, id_noticia) -> None:
        self.__id_noticia = id_noticia

    def construir(self):
        noticia = self.controlador_noticia.get_noticia()
        
        tk.Label(
            self._root,
            text=noticia.get_assunto(),
            font=("Calibri", 18, "bold")
            ).pack()
        
        tk.Label(
            self._root,
            text=noticia.get_texto(),
            font=("Verdana", 12, "italic"),
            justify="left",
            width=100,
            height=20,
            wraplength=800,
            bg="white",
            ).pack()


        if self._parent:
            tk.Button(
                self._root,
                text="Voltar",
                command=self._parent.construir
            ).pack()
        