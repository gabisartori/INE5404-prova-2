class Usuario:
    def __init__(self, usuario: dict) -> None:
        self.id: int = usuario["id"]
        self.nome: str = usuario["nome"]
        self.senha: str = usuario["senha"]

    def get_id(self) -> int:
        return self.id
    
    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, nome: str) -> None:
        self.nome = nome
    
    def get_senha(self) -> str:
        return self.senha
    
    def set_senha(self, senha: str) -> None:
        self.senha = senha
    