from src.estacionamento import Estacionamento

def exibir_menu():
    print("\n" + "="*40)
    print(" SISTEMA DE ESTACIONAMENTO ".center(40))
    print("="*40)
    print("1. Registrar entrada de veículo")
    print("2. Buscar veículo por placa (com Benchmark)")
    print("3. Registrar saída de veículo")
    print("4. Listar veículos estacionados (Em Ordem)")
    print("5. Visualizar Estrutura da Árvore (Gráfico)")
    print("6. Ver Histórico de Entradas e Saídas")
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

        elif opcao == '5':
            patio.abb.exibir_arvore_grafica()

        elif opcao == '6':
            logs = patio.obter_historico()
            if not logs:
                print("Nenhuma movimentação registrada.")
            else:
                print("\n--- HISTÓRICO DO ESTACIONAMENTO ---")
                for registro in logs:
                    print(registro)

        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()