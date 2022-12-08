from control.controlador_usuario import ControladorUsuario


class ControladorLogin(ControladorUsuario):
    def __init__(self, db="db/usuarios") -> None:
        super().__init__(db)
        self.conectar_banco()

    def verificar_senha(self, nome: str, senha: str) -> bool:
        """Checa se a senha passada bate com a senha salva no banco de dados"""
        usuario = self.buscar_usuario_por_nome(nome)
        if isinstance(usuario, str):
            return False
        return usuario.get_senha() == senha
