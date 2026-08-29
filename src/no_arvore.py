from .veiculo import Veiculo


class NoArvore:

    def __init__(self, veiculo: Veiculo):
        self.veiculo = veiculo
        self.esquerda = None
        self.direita = None