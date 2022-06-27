from src.exceptions.base_erros import BaseErros

class CampoVazioErro(BaseErros):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
