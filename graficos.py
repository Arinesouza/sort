import matplotlib.pyplot as plt
import numpy as np

labels = [
    "Python Bubble Sort", 
    "Python Selection Sort", 
    "JavaScript Bubble Sort", 
    "JavaScript Selection Sort"
]

media_tempo = [157264.76, 53942.334, 6653.836, 2415.148]
media_memoria = [-14868.4, -13638.4, -14432.8, -1496.8]
mediana_tempo = [137229.055, 48908.06, 6294.01, 2208.81]
mediana_memoria = [-14912, -14812, -22548, 924]

x = np.arange(len(labels))

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Gráficos')

# Gráfico 1: Média do Tempo
axs[0, 0].bar(x, media_tempo, color='blue', alpha=0.7)
axs[0, 0].set_title('Média do Tempo')
axs[0, 0].set_xticks(x)
axs[0, 0].set_xticklabels(labels, rotation=15)
axs[0, 0].set_ylabel('Tempo (ms)')

# Gráfico 2: Média da Memória
axs[0, 1].bar(x, media_memoria, color='green', alpha=0.7)
axs[0, 1].set_title('Média da Memória')
axs[0, 1].set_xticks(x)
axs[0, 1].set_xticklabels(labels, rotation=15)
axs[0, 1].set_ylabel('Memória (KB)')

# Gráfico 3: Mediana do Tempo
axs[1, 0].bar(x, mediana_tempo, color='red', alpha=0.7)
axs[1, 0].set_title('Mediana do Tempo')
axs[1, 0].set_xticks(x)
axs[1, 0].set_xticklabels(labels, rotation=15)
axs[1, 0].set_ylabel('Tempo (ms)')

# Gráfico 4: Mediana da Memória
axs[1, 1].bar(x, mediana_memoria, color='orange', alpha=0.7)
axs[1, 1].axhline(0, color='black', linewidth=1, linestyle='--')  
axs[1, 1].set_title('Mediana da Memória')
axs[1, 1].set_xticks(x)
axs[1, 1].set_xticklabels(labels, rotation=15)
axs[1, 1].set_ylabel('Memória (KB)')
axs[1, 1].set_ylim(min(mediana_memoria) - 5000, max(mediana_memoria) + 5000)  


plt.tight_layout(rect=[0, 0, 1, 0.95], h_pad=4.0)
plt.show()
