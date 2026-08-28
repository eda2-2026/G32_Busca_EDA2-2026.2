class Veiculo:
    
    def __init__(self, placa: str, vaga: int, modelo: str = ""):
        self.placa = placa.upper().replace("-", "")
        self.vaga = vaga
        self.modelo = modelo

    def __repr__(self):
        return f"Veiculo(placa={self.placa}, vaga={self.vaga}, modelo={self.modelo!r})"

    def __eq__(self, outro):
        return isinstance(outro, Veiculo) and self.placa == outro.placa