from src.veiculo import Veiculo
from src.arvore_binaria import ArvoreBinariaBusca
from src.estacionamento import Estacionamento

def exibir_menu():
    print("\n" + "="*40)
    print(" SISTEMA DE ESTACIONAMENTO ".center(40))
    print("="*40)
    print("1. Registrar entrada de veículo")
    print("2. Buscar veículo por placa (com Benchmark)")
    print("3. Registrar saída de veículo")
    print("4. Listar veículos estacionados (Em Ordem)")
    print("0. Sair do sistema")
    print("="*40)

def main():
    try:
        capacidade = int(input("Defina a capacidade máxima do estacionamento: "))
    except ValueError:
        print("Valor inválido. Iniciando com 50 vagas.")
        capacidade = 50

    patio = Estacionamento(total_vagas=capacidade)

    while True:
        print(f"\nVagas disponíveis: {patio.vagas_disponiveis()} / {patio.total_vagas}")
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            placa = input("Placa do veículo: ")
            try:
                vaga = int(input("Número da vaga: "))
                modelo = input("Modelo do veículo: ")
                sucesso, msg = patio.inserir_veiculo(placa, vaga, modelo)
                print(msg)
            except ValueError:
                print("Erro: A vaga deve ser um número inteiro.")

        elif opcao == '2':
            placa = input("Digite a placa para busca: ")
            veiculo, comp_abb, comp_seq = patio.buscar_veiculo(placa)
            
            if veiculo:
                print(f"\nVeículo Encontrado: {veiculo.modelo} | Vaga: {veiculo.vaga}")
                print("-" * 30)
                print("📊 RESULTADOS DO BENCHMARK")
                print(f"Busca ABB (O(log n)): {comp_abb} comparações")
                print(f"Busca Sequencial (O(n)): {comp_seq} comparações")
                print("-" * 30)
            else:
                print("Veículo não encontrado.")

        elif opcao == '3':
            placa = input("Digite a placa do veículo que está saindo: ")
            sucesso, msg = patio.remover_veiculo(placa)
            print(msg)

        elif opcao == '4':
            veiculos = patio.listar_veiculos()
            if not veiculos:
                print("O estacionamento está vazio.")
            else:
                print("\nVEÍCULOS ESTACIONADOS (Ordenados por Placa):")
                for v in veiculos:
                    print(f"Vaga: {v.vaga:03d} | Placa: {v.placa} | Modelo: {v.modelo}")

        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

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