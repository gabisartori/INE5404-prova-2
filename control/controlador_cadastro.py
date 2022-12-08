from model.modelo_usuario import Usuario
from control.controlador_usuario import ControladorUsuario
import json 


class ControladorCadastro(ControladorUsuario):
    def __init__(self, db: str = "db/usuarios") -> None:
        super().__init__(db)
        self.conectar_banco()
        try:
            with open("db/contador.txt") as arquivo:
                self.__contador_id = int(arquivo.read())
        except FileNotFoundError:
            with open("db/contador.txt", 'w') as arquivo:
                arquivo.write("1")
            self.__contador_id = 1

    def cadastrar_usuario(self, nome: str, senha: str) -> Usuario | str:
        """Recebe os dados do usuário, cria um objeto do tipo Usuario e o adiciona ao banco de dados"""
        if not isinstance(self.buscar_usuario_por_nome(nome), str):
            return "Já existe um usuário com esse nome"
        
        usuario = Usuario({'id': self.__contador_id, 'nome': nome, 'senha': senha})

        # Incrementa o contador de id
        self.__contador_id += 1
        with open("db/contador.txt", "w") as arquivo:
            arquivo.write(str(self.__contador_id))
        usr = Usuario({'id': self.__contador_id, 'nome': nome, 'senha': senha})
        self.get_usuarios().append(usr)
        
        with open(f'{self.get_db()}.json', 'w') as arquivo:
            json.dump(self.get_usuarios(), arquivo, default=lambda usr: usr.__dict__)

        return usuario
