const fs = require('fs');
const os = require('os');
const process = require('process');

function selectionSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n; i++) {
    let minIdx = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx]) {
        minIdx = j;
      }
    }
    [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]]; 
  }
}

function main() {
  // Lendo os números do arquivo
  fs.readFile('arq.txt', 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo:', err);
      return;
    }

    const numbers = data.split('\n').map(line => parseInt(line.trim(), 10)).filter(Boolean);

    // Informações do sistema
    console.log("Linguagem: JavaScript (Node.js)");
    console.log("Versão:", process.version);
    console.log("Sistema Operacional:", os.platform());
    console.log("Arquitetura:", os.arch());

    // Monitoramento de desempenho
    const startMemory = process.memoryUsage().rss; // Memória inicial
    const startTime = process.hrtime(); // Tempo inicial

    // Ordenando com Selection Sort
    selectionSort(numbers);

    // Tempo final
    const [seconds, nanoseconds] = process.hrtime(startTime);
    const elapsedTime = (seconds * 1000) + (nanoseconds / 1000000); 

    const endMemory = process.memoryUsage().rss; 

    // Gravando o resultado no arquivo
    fs.writeFile('arq-saida.txt', numbers.join('\n'), 'utf8', (err) => {
      if (err) {
        console.error('Erro ao gravar o arquivo:', err);
        return;
      }

      const memoryUsed = (endMemory - startMemory) / 1024;
      console.log(`Tempo (ms): ${elapsedTime.toFixed(2)}`);
      console.log(`Memória utilizada (KB): ${memoryUsed.toFixed(2)}`);
    });
  });
}

main();
