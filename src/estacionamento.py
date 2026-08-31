from typing import Tuple, List
from src.veiculo import Veiculo
from src.arvore_binaria import ArvoreBinariaBusca
from src.busca_sequencial import BuscaSequencial

class Estacionamento:
    def __init__(self, total_vagas: int):
        self.total_vagas = total_vagas
        self.abb = ArvoreBinariaBusca()
        self.sequencial = BuscaSequencial()

    def vagas_disponiveis(self) -> int:
        return self.total_vagas - len(self.abb)

    def inserir_veiculo(self, placa: str, vaga: int, modelo: str) -> Tuple[bool, str]:
        if self.vagas_disponiveis() <= 0:
            return False, "Erro: Estacionamento lotado."

        veiculo = Veiculo(placa, vaga, modelo)
        
        if self.abb.inserir(veiculo):
            self.sequencial.inserir(veiculo)
            return True, f"Sucesso: Veículo {veiculo.placa} estacionado na vaga {veiculo.vaga}."
        else:
            return False, f"Erro: A placa {veiculo.placa} já está cadastrada."

    def buscar_veiculo(self, placa: str) -> Tuple[Veiculo, int, int]:
        veiculo_abb, comp_abb = self.abb.buscar(placa)
        _, comp_seq = self.sequencial.buscar(placa)
        return veiculo_abb, comp_abb, comp_seq

    def remover_veiculo(self, placa: str) -> Tuple[bool, str]:
        if self.abb.remover(placa):
            self.sequencial.remover(placa)
            return True, "Sucesso: Veículo removido e vaga liberada."
        return False, "Erro: Veículo não encontrado."

    def listar_veiculos(self) -> List[Veiculo]:
        return self.abb.em_ordem()