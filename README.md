# Sistema de Localização de Veículos em Estacionamento

## Integrantes
| Matrícula | Nome |
| --- | --- |
| 231027005 | Maria Samara |
| 2310391400 | Marjorie Mitzi |

## Vídeo:
*(Insira o link aqui)*

## Motivação
Em grandes estacionamentos, localizar rapidamente um veículo e gerenciar as vagas disponíveis é um desafio. Abordagens de armazenamento em listas não ordenadas geram lentidão nas buscas, resultando em filas e má experiência do usuário. Este projeto visa aplicar Estruturas de Dados avançadas para otimizar esse controle.

## Estruturas de busca implementadas
1. **Árvore Binária de Busca (ABB):** Estrutura principal do sistema. Organiza os veículos pela placa, permitindo buscas, inserções e remoções com complexidade de tempo média de **O(log n)**.
2. **Busca Sequencial:** Estrutura auxiliar mantida exclusivamente para fins de benchmark e comparação acadêmica, com complexidade de tempo de **O(n)** no pior caso.

## Organização do repositório
* `src/veiculo.py`: Modelo da entidade Veículo.
* `src/no_arvore.py`: Nó da Árvore Binária.
* `src/arvore_binaria.py`: Implementação da Árvore Binária de Busca.
* `src/busca_sequencial.py`: Implementação da Busca em Lista.
* `src/estacionamento.py`: Classe de negócio que gerencia a capacidade de vagas e integra as buscas.
* `main.py`: Interface de linha de comando (CLI) interativa.

## Como rodar
Certifique-se de ter o Python 3 instalado. Clone o repositório e execute na raiz do projeto:
```bash
python main.py