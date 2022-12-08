class Usuario:
    def __init__(self, usuario: dict) -> None:
        self.__id: int = usuario["id"]
        self.__nome: str = usuario["nome"]
        self.__password: str = usuario["password"]

    def get_id(self) -> int:
        return self.__id
    
    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome: str) -> None:
        self.__nome = nome
    
    def get_password(self) -> str:
        return self.__password
    
    def set_password(self, password: str) -> None:
        self.__password = password
    