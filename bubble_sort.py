import os
import platform
import psutil 
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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

    # Ordenando com Bubble Sort
    bubble_sort(numbers)

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
