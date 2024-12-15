import platform
import time
from memory_profiler import memory_usage

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
    start_time = time.time()
    memory_used = memory_usage((bubble_sort, (numbers,)), interval=0.1)[0] * 1024  

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  

    # Gravando o resultado no arquivo
    with open("arq-saida.txt", "w") as file:
        for num in numbers:
            file.write(f"{num}\n")
    
    print(f"Tempo (ms): {elapsed_time:.2f}")
    print(f"Memória utilizada (KB): {memory_used:.2f}")

if __name__ == "__main__":
    main()
