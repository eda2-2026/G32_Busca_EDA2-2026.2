from .veiculo import Veiculo
from .no_arvore import NoArvore


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
        self._quantidade = 0

    def inserir(self, veiculo: Veiculo) -> bool:
        self.raiz, inserido = self._inserir(
            self.raiz,
            veiculo
        )

        if inserido:
            self._quantidade += 1

        return inserido

    def _inserir(self, no, veiculo):

        if no is None:
            return NoArvore(veiculo), True

        if veiculo.placa < no.veiculo.placa:
            no.esquerda, inserido = self._inserir(
                no.esquerda,
                veiculo
            )
            return no, inserido

        elif veiculo.placa > no.veiculo.placa:
            no.direita, inserido = self._inserir(
                no.direita,
                veiculo
            )
            return no, inserido

        else:
            return no, False

    def buscar(self, placa: str):
        placa = self._normalizar_placa(placa)

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
        placa = self._normalizar_placa(placa)

        self.raiz, removido = self._remover(
            self.raiz,
            placa
        )

        if removido:
            self._quantidade -= 1

        return removido

    def _remover(self, no, placa):

        if no is None:
            return None, False

        if placa < no.veiculo.placa:
            no.esquerda, removido = self._remover(
                no.esquerda,
                placa
            )
            return no, removido

        elif placa > no.veiculo.placa:
            no.direita, removido = self._remover(
                no.direita,
                placa
            )
            return no, removido

        else:

            if no.esquerda is None:
                return no.direita, True

            if no.direita is None:
                return no.esquerda, True

            sucessor = self._menor_no(no.direita)

            no.veiculo = sucessor.veiculo

            no.direita, _ = self._remover(
                no.direita,
                sucessor.veiculo.placa
            )

            return no, True

    def _menor_no(self, no):

        atual = no

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual

    def em_ordem(self):

        resultado = []

        self._em_ordem(
            self.raiz,
            resultado
        )

        return resultado

    def _em_ordem(self, no, resultado):

        if no is None:
            return

        self._em_ordem(
            no.esquerda,
            resultado
        )

        resultado.append(no.veiculo)

        self._em_ordem(
            no.direita,
            resultado
        )

    @staticmethod
    def _normalizar_placa(placa: str) -> str:
        return (
            placa
            .upper()
            .replace("-", "")
            .replace(" ", "")
        )

    def __len__(self):
        return self._quantidade

    def esta_vazia(self):
        return self.raiz is None