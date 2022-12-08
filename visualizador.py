import tkinter as tk


class Visualizador:
    def __init__(self, parent, root=None) -> None:
        self.set_parent(parent)
        # Permite que os objetos sejam usados tanto como uma janela em si ou como um componente
        self._root: tk.Tk = root if root else tk.Tk()
    
    def get_parent(self):
        return self._parent
    
    def set_parent(self, parent):
        self._parent = parent
    
    def get_root(self):
        return self._root
    
    def set_root(self, root):
        self._root = root

    def aviso(self, texto: str, cor="red") -> None:
        """Exibe uma mensagem em vermelho no fim da tela"""
        aviso = tk.Label(self._root, text=texto, fg=cor, font=('Bahnschrift Light SemiCondensed', 15, 'bold'))
        aviso.pack()
        self._root.after(2000, aviso.destroy)
    
 
    def limpar_tela(self) -> None:
        """Remove todo o conteúdo de uma janela"""
        for widget in self._root.winfo_children():
            widget.destroy()
