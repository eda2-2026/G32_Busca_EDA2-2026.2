from veiculo import Veiculo


class NoArvore:
    def __init__(self, veiculo: Veiculo):
        self.veiculo = veiculo
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    
    def __init__(self):
        self.raiz = None
        self._quantidade = 0

    def inserir(self, veiculo: Veiculo):
        self.raiz = self._inserir(self.raiz, veiculo)
        self._quantidade += 1

    def _inserir(self, no, veiculo):
        if no is None:
            return NoArvore(veiculo)
        if veiculo.placa < no.veiculo.placa:
            no.esquerda = self._inserir(no.esquerda, veiculo)
        elif veiculo.placa > no.veiculo.placa:
            no.direita = self._inserir(no.direita, veiculo)
        return no

    def buscar(self, placa: str):
        """Retorna (veiculo, numero_de_comparacoes)."""
        placa = placa.upper().replace("-", "")
        no = self.raiz
        comparacoes = 0
        while no is not None:
            comparacoes += 1
            if placa == no.veiculo.placa:
                return no.veiculo, comparacoes
            elif placa < no.veiculo.placa:
                no = no.esquerda
            else:
                no = no.direita
        return None, comparacoes

    def remover(self, placa: str) -> bool:
        placa = placa.upper().replace("-", "")
        self.raiz, removido = self._remover(self.raiz, placa)
        if removido:
            self._quantidade -= 1
        return removido

    def _remover(self, no, placa):
        if no is None:
            return no, False
        if placa < no.veiculo.placa:
            no.esquerda, removido = self._remover(no.esquerda, placa)
        elif placa > no.veiculo.placa:
            no.direita, removido = self._remover(no.direita, placa)
        else:
            removido = True
            if no.esquerda is None:
                return no.direita, removido
            if no.direita is None:
                return no.esquerda, removido
            sucessor = no.direita
            while sucessor.esquerda:
                sucessor = sucessor.esquerda
            no.veiculo = sucessor.veiculo
            no.direita, _ = self._remover(no.direita, sucessor.veiculo.placa)
        return no, removido

    def __len__(self):
        return self._quantidade