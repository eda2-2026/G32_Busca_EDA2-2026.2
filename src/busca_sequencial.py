from veiculo import Veiculo

class BuscaSequencial:

    def __init__(self):
        self.veiculos = []

    def inserir(self, veiculo: Veiculo):
        self.veiculos.append(veiculo)

    def buscar(self, placa: str):
        placa = placa.upper().replace("-", "")
        comparacoes = 0
        for v in self.veiculos:
            comparacoes += 1
            if v.placa == placa:
                return v, comparacoes
        return None, comparacoes

    def remover(self, placa: str) -> bool:
        placa = placa.upper().replace("-", "")
        for i, v in enumerate(self.veiculos):
            if v.placa == placa:
                del self.veiculos[i]
                return True
        return False

    def __len__(self):
        return len(self.veiculos)