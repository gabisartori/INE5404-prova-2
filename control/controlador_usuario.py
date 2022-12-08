from model.modelo_usuario import Usuario
import json


class ControladorUsuario:
    def __init__(self, db="usuarios") -> None:
        self.__db = db
        self.__usuarios: list[Usuario] | None = None

    def conectar_banco(self) -> None:
        """Atualiza a lista de usuários se baseando no banco de dados"""
        try:
            with open(f"{self.__db}.json") as arquivo:
                self.__usuarios = [Usuario(usr) for usr in json.load(arquivo)]
        except FileNotFoundError:
            with open(f"{self.__db}.json", 'w') as arquivo:
                json.dump([], arquivo)
                self.__usuarios = []

    def buscar_usuario_por_id(self, id: int) -> Usuario:
        for usuario in self.__usuarios:
            if usuario.get_id() == id:
                return usuario
        
    def buscar_usuario_por_nome(self, nome: str) -> Usuario | str:
        for usuario in self.__usuarios:
            if usuario.get_nome() == nome:
                return usuario
        return "Usuário não encontrado"

    def atualizar_usuario(self, id: int, novo_nome: str, nova_senha: str) -> Usuario | str:
        # Verifica se o novo nome já está em uso
        if not isinstance(self.buscar_usuario_por_nome(novo_nome), str):
            # Verifica se o novo nome é o mesmo do usuário que está sendo atualizado
            if self.buscar_usuario_por_nome(novo_nome).get_id() != id:
                return "Já existe um usuário com esse nome"
        
        # Altera os dados do usuário
        usuario = [usr for usr in self.__usuarios if usr.get_id() == id][0]
        if novo_nome:
            usuario.set_nome(novo_nome)
        if nova_senha:
            usuario.set_senha(*nova_senha)

        # salvando as alterações no banco de dados
        with open(f"{self.__db}.json", 'w') as arquivo:
            json.dump(self.__usuarios, arquivo, default=lambda usr: usr.__dict__)

        return usuario

    def remover_usuario(self, id: int) -> Usuario | str:
        usuario = self.buscar_usuario_por_id(id)
        self.__usuarios.remove(usuario)
        with open(f"{self.__db}.json", 'w') as arquivo:
            json.dump(self.__usuarios, arquivo, default=lambda usr: usr.__dict__)
        return usuario

    def get_usuarios(self) -> list[Usuario]:
        return self.__usuarios
    
    def get_db(self) -> str:
        return self.__db
    
    def set_db(self, db: str) -> None:
        self.__db = db

    