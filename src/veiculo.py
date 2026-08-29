class Veiculo:

    def __init__(self, placa: str, vaga: int, modelo: str = ""):
        self.placa = placa.upper().replace("-", "").replace(" ", "")
        self.vaga = vaga
        self.modelo = modelo

    def __repr__(self):
        return (
            f"Veiculo("
            f"placa={self.placa}, "
            f"vaga={self.vaga}, "
            f"modelo={self.modelo!r})"
        )

    def __eq__(self, outro):
        if not isinstance(outro, Veiculo):
            return False

        return self.placa == outro.placa