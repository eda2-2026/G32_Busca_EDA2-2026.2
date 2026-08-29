from src.veiculo import Veiculo
from src.arvore_binaria import ArvoreBinariaBusca


def mostrar_veiculo(veiculo):

    if veiculo is None:
        print("Veículo não encontrado.")
        return

    print("\nVeículo encontrado:")
    print(f"Placa:  {veiculo.placa}")
    print(f"Vaga:   {veiculo.vaga}")
    print(f"Modelo: {veiculo.modelo}")


def main():

    estacionamento = ArvoreBinariaBusca()

    veiculos = [
        Veiculo("ABC-1234", 10, "Honda Civic"),
        Veiculo("DEF-5678", 25, "Toyota Corolla"),
        Veiculo("GHI-9012", 5, "Fiat Argo"),
        Veiculo("JKL-3456", 18, "Volkswagen Polo"),
        Veiculo("MNO-7890", 30, "Chevrolet Onix"),
    ]

    for veiculo in veiculos:

        if estacionamento.inserir(veiculo):
            print(
                f"Veículo {veiculo.placa} "
                f"inserido na vaga {veiculo.vaga}."
            )
        else:
            print(
                f"A placa {veiculo.placa} "
                f"já está cadastrada."
            )

    print("\n-----------------------------------")
    print(f"Total de veículos: {len(estacionamento)}")
    print("-----------------------------------")

    placa = input("\nDigite a placa para buscar: ")

    veiculo, comparacoes = estacionamento.buscar(placa)

    mostrar_veiculo(veiculo)

    print(f"Comparações realizadas: {comparacoes}")

    print("\n-----------------------------------")
    print("VEÍCULOS POR ORDEM DE PLACA")
    print("-----------------------------------")

    for veiculo in estacionamento.em_ordem():

        print(
            f"Placa: {veiculo.placa} | "
            f"Vaga: {veiculo.vaga} | "
            f"Modelo: {veiculo.modelo}"
        )

    placa = input("\nDigite a placa para remover: ")

    if estacionamento.remover(placa):
        print("Veículo removido com sucesso.")
    else:
        print("Veículo não encontrado.")

    print(
        f"Veículos restantes: "
        f"{len(estacionamento)}"
    )


if __name__ == "__main__":
    main()