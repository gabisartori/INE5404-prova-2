import tkinter as tk
from view.visualizador import Visualizador
from view.visualizador_cadastro import VisualizadorCadastro
from view.visualizador_menu import VisualizadorMenu
from control.controlador_login import ControladorLogin


class VisualizadorLogin(Visualizador):

    def __init__(self, parent, root=None):
        super().__init__(parent, root)

        # Associações
        self.controlador_login = ControladorLogin()

    def construir(self):
        """Constrói a tela"""
        self.limpar_tela()
        self._root.geometry("1280x720")

        self.controlador_login.conectar_banco()

        tk.Label(
            text="Menu",
            font=("Calibri", 25, "bold"),
            foreground="black",
            width=50,
            height=8).pack()

        tk.Label(
            self._root,
            text='Email:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        nome = tk.Entry(self._root, width=25, font=("Verdana", 18, "italic"))
        nome.pack()

        tk.Label(
            self._root,
            text='Senha:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        senha = tk.Entry(self._root, width=25, font=("Verdana", 18, "italic"))
        senha.pack()
        senha["show"] = "*"

        tk.Button(
            self._root,
            text='Entrar',
            font=('Calibri', '12'),
            width=20,
            command=lambda: self.fazer_login(nome.get(), senha.get())
        ).pack()

        tk.Button(
            self._root,
            text='Cadastrar-se',
            font=('Calibri', '12'),
            width=20,
            command=self.tela_cadastro
        ).pack()

        if self._parent:
            tk.Button(
                self._root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self._parent.construir
            ).pack()

    def fazer_login(self, nome: str, senha: str) -> None:
        """Verifica se o usuário existe e se a senha está correta, caso esteja, abre o menu do usuário"""
        # Busca pelo usuário no banco de dados
        usuario = self.controlador_login.buscar_usuario_por_nome(nome)

        # Caso a busca por um usário não tenha retornado uma mensagem de erro
        if not isinstance(usuario, str):
            if usuario.get_senha() == senha:
                self.tela_noticias()
            else:
                self.aviso("Senha incorreta!")
        # Caso a busca por um usário tenha retornado uma mensagem de erro
        else:
            self.aviso(usuario)

    def tela_cadastro(self) -> None:
        """Contrói a tela de cadastro na janela atual"""
        self.limpar_tela()
        VisualizadorCadastro(self, self._root).construir()

    def tela_noticias(self) -> None:
        """Contrói a tela de notícias na janela atual"""
        self.limpar_tela()
        VisualizadorMenu(self, self._root).construir()

if __name__ == "__main__":
    a = VisualizadorLogin(None)
    a.construir()
    a.get_root().mainloop()
