from view.visualizador import Visualizador
from control.controlador_noticia import ControladorNoticia
import tkinter as tk

class VisualizadorMenu(Visualizador):
    def __init__(self, parent, root=None) -> None:
        super().__init__(parent, root)
        
        self.controlador = ControladorNoticia()
    
    def construir(self) -> None:
        def atualizar_tela():
            for child in caixa.winfo_children(): child.destroy()
            # Aplicar filtros
            filtros = {
                "inicio": (ano_inicio.get(), mes_inicio.get(), dia_inicio.get()),
                "fim": (ano_fim.get(), mes_fim.get(), dia_fim.get()),
                "assunto": assunto.get(),
                "categoria": categoria.get()
            }
            noticias = self.controlador.buscar_noticias_por_filtro(filtros)
            for noticia in noticias:
                tk.Label(caixa, text=noticia.assunto).pack()
        tk.Label(self._root, text="Menu", font=("Calibri", 18, "bold")).pack()

        # Data início
        tk.Label(self._root, text="Data início", font=("Calibri", 12, "bold")).pack()
        inicio = tk.Frame(self._root)
        inicio.pack()
        ano_inicio = tk.Entry(self._root, width=10, font=("Verdana", 18, "italic"))
        ano_inicio.pack(in_=inicio, side=tk.LEFT)
        mes_inicio = tk.Entry(self._root, width=10, font=("Verdana", 18, "italic"))
        mes_inicio.pack(in_=inicio, side=tk.LEFT)
        dia_inicio = tk.Entry(self._root, width=10, font=("Verdana", 18, "italic"))
        dia_inicio.pack(in_=inicio, side=tk.LEFT)

        tk.Label(self._root, text="Data fim", font=("Calibri", 12, "bold")).pack()
        fim = tk.Frame(self._root)
        fim.pack()
        ano_fim = tk.Entry(self._root, width=10, font=("Verdana", 18, "italic"))
        ano_fim.pack(in_=fim, side=tk.LEFT)
        mes_fim = tk.Entry(self._root, width=10, font=("Verdana", 18, "italic"))
        mes_fim.pack(in_=fim, side=tk.LEFT)
        dia_fim = tk.Entry(self._root, width=10, font=("Verdana", 18, "italic"))
        dia_fim.pack(in_=fim, side=tk.LEFT)

        # Assunto
        tk.Label(self._root, text="Assunto", font=("Calibri", 12, "bold")).pack()
        assunto = tk.Entry(self._root, width=25, font=("Verdana", 18, "italic"))
        assunto.pack()

        # Categoria
        tk.Label(self._root, text="Categoria", font=("Calibri", 12, "bold")).pack()
        categoria = tk.StringVar(self._root, "Escolha uma categoria")
        tk.OptionMenu(self._root, categoria, "Escolha uma categoria", "Esporte", "Política", "Economia").pack()

        

        caixa = tk.Frame(self._root)
        caixa.pack()

        tk.Button(
            self._root,
            text="Aplicar filtros",
            font=("Calibri", "12"),
            width=20,
            command=atualizar_tela
        ).pack()
    
    
