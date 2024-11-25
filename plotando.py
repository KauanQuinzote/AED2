from matplotlib import pyplot as plt
import numpy as np

# Exemplo de dados médios para os tempos de execução, assumindo que os tempos já foram calculados
algorithms = ['Selection Sort', 'HeapSort', 'Radix Sort']
input_types = ['ALEATÓRIO', 'QUASE ORDENADO']
sizes = [100, 1000, 10000]

# Dados fictícios de tempos (em segundos) para os gráficos (substitua pelos dados reais)
# Dados no formato (algoritmo, tipo de entrada, tamanho de entrada) -> tempo médio
results = {
    ('Selection Sort', 'ALEATÓRIO', 100): 0.002,
    ('HeapSort', 'ALEATÓRIO', 100): 0.001,
    ('Radix Sort', 'ALEATÓRIO', 100): 0.0005,
    ('Selection Sort', 'QUASE ORDENADO', 100): 0.0018,
    ('HeapSort', 'QUASE ORDENADO', 100): 0.0012,
    ('Radix Sort', 'QUASE ORDENADO', 100): 0.0004,
    
    ('Selection Sort', 'ALEATÓRIO', 1000): 0.12,
    ('HeapSort', 'ALEATÓRIO', 1000): 0.08,
    ('Radix Sort', 'ALEATÓRIO', 1000): 0.02,
    ('Selection Sort', 'QUASE ORDENADO', 1000): 0.10,
    ('HeapSort', 'QUASE ORDENADO', 1000): 0.06,
    ('Radix Sort', 'QUASE ORDENADO', 1000): 0.015,
    
    ('Selection Sort', 'ALEATÓRIO', 10000): 1.2,
    ('HeapSort', 'ALEATÓRIO', 10000): 0.75,
    ('Radix Sort', 'ALEATÓRIO', 10000): 0.1,
    ('Selection Sort', 'QUASE ORDENADO', 10000): 1.1,
    ('HeapSort', 'QUASE ORDENADO', 10000): 0.6,
    ('Radix Sort', 'QUASE ORDENADO', 10000): 0.08,
}

# Função para plotar o gráfico
def plot_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotando os dados
    for input_type in input_types:
        for algo in algorithms:
            times = [results[(algo, input_type, size)] for size in sizes]
            ax.plot(sizes, times, label=f'{algo} - {input_type}')

    ax.set_xlabel('Tamanho do Vetor')
    ax.set_ylabel('Tempo de Execução (s)')
    ax.set_title('Comparação de Desempenho de Algoritmos de Ordenação')
    ax.set_xscale('log')  # Usar escala logarítmica no eixo X para melhor visualização
    ax.set_yscale('log')  # Usar escala logarítmica no eixo Y para melhor visualização
    ax.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

# Chamar a função para gerar o gráfico
plot_comparison()
    