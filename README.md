# Sistema de Localização de Veículos em Estacionamento

## Integrantes
| Matrícula | Nome |
| :--- | :--- |
| 231027005 | Maria Samara |
| 2310391400 | Marjorie Mitzi |

##  Vídeo da Apresentação
*https://youtu.be/ZjNHZNRCZZs*

---

##  O Problema e a Motivação
Em grandes estacionamentos comerciais, gerenciar a entrada, saída e localização de veículos pode se tornar um gargalo crítico. A busca tradicional em listas desordenadas possui um custo linear de tempo **O(n)**, o que significa que, em um pátio lotado, o sistema precisaria checar placa por placa, gerando lentidão nas catracas e má experiência para o cliente. 

O objetivo deste projeto é otimizar esse controle através de estruturas de dados eficientes, provando na prática o ganho de performance.

##  Estruturas de Busca Implementadas
Para resolver o problema, implementamos duas abordagens simultâneas:
1. **Árvore Binária de Busca (ABB):** É o coração do sistema. As placas são indexadas na árvore, permitindo buscas e remoções extremamente rápidas.
2. **Busca Sequencial (Lista):** Funciona nos bastidores como um *baseline*. Ela mantém uma cópia dos veículos para que possamos comparar o esforço computacional real frente à ABB.

##  Análise de Complexidade e Benchmark
Nosso menu interativo possui um recurso de **Benchmark** (Opção 2). Ao buscar uma placa, o sistema executa a procura em ambas as estruturas e imprime a contagem exata de comparações realizadas.

Isso comprova a seguinte teoria de complexidade:
| Operação | Busca Sequencial | Árvore Binária de Busca (Caso Médio) |
| :--- | :--- | :--- |
| **Busca** | O(n) | O(log n) |
| **Inserção** | O(1) *(append direto)* | O(log n) |
| **Remoção** | O(n) | O(log n) |

*Enquanto a busca sequencial varre os veículos um a um, a nossa ABB descarta metade da subárvore a cada nó visitado, alcançando o carro alvo em pouquíssimos passos.*

## Funcionalidades
- Definição de capacidade máxima e controle de vagas dinâmico.
- Cadastro de veículos (Placa, Vaga, Modelo).
- Busca com relatório de eficiência algorítmica (Benchmark).
- Remoção inteligente mantendo a integridade da árvore (substituição pelo sucessor/menor nó à direita).
- Listagem completa da frota em ordem alfabética (Travessia *Em Ordem*).
- Visualização Gráfica da Árvore: Desenho estrutural da ABB direto no console.
- Histórico de Movimentação: Log completo de todas as entradas e saídas de veículos.

##  Como Rodar
Certifique-se de possuir o Python 3 instalado no seu ambiente. Acesse a raiz do repositório via terminal e execute:

```bash
python3 main.py


##  Demonstração do Sistema

!(assets/Screenshot from 2026-08-31 18-19-29.png)
!(assets/Screenshot from 2026-08-31 18-19-40.png)
!(assets/Screenshot from 2026-08-31 18-19-49.png)
!(assets/Screenshot from 2026-08-31 18-19-55.png)
