import os
import platform
import psutil
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    # Lendo os números do arquivo
    with open("arq.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    # Informações do sistema
    print("Linguagem: Python")
    print("Versão:", platform.python_version())
    print("Sistema Operacional:", platform.system())
    print("Arquitetura:", platform.architecture()[0])

    # Monitoramento de desempenho
    process = psutil.Process(os.getpid())
    start_memory = process.memory_info().rss
    start_time = time.time()

    # Ordenando com Selection Sort
    selection_sort(numbers)

    end_time = time.time()
    end_memory = process.memory_info().rss

    # Gravando o resultado no arquivo
    with open("arq-saida.txt", "w") as file:
        for num in numbers:
            file.write(f"{num}\n")

    elapsed_time = (end_time - start_time) * 1000  
    memory_used = (end_memory - start_memory) / 1024 

    print(f"Tempo (ms): {elapsed_time:.2f}")
    print(f"Memória utilizada (KB): {memory_used:.2f}")

if __name__ == "__main__":
    main()
