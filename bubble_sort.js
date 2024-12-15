const fs = require('fs');
const os = require('os');
const process = require('process');

function bubbleSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; 
      }
    }
  } 
}

function main() {
  // Lendo os números do arquivo
  fs.readFile('arq.txt', 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo', err);
      return;
    }

    const numbers = data.split('\n').map(line => parseInt(line.trim(), 10)).filter(Boolean);

    // Informações do sistema
    console.log("Linguagem: JavaScript (Node.js)");
    console.log("Versão:", process.version);
    console.log("Sistema Operacional:", os.platform());
    console.log("Arquitetura:", os.arch());

    // Monitoramento de desempenho
    const startMemory = process.memoryUsage().rss; 
    const startTime = process.hrtime(); 

    // Ordenando com Bubble Sort
    bubbleSort(numbers);

    const [seconds, nanoseconds] = process.hrtime(startTime);
    const elapsedTime = (seconds * 1000) + (nanoseconds / 1000000); 

    const endMemory = process.memoryUsage().rss; 
    // Gravando o resultado no arquivo
    fs.writeFile('arq-saida.txt', numbers.join('\n'), 'utf8', (err) => {
      if (err) {
        console.error('Erro ao gravar o arquivo', err);
        return;
      }

      const memoryUsed = (endMemory - startMemory) / 1024;

      console.log(`Tempo (ms): ${elapsedTime.toFixed(2)}`);
      console.log(`Memória utilizada (KB): ${memoryUsed.toFixed(2)}`);
    });
  });
}

main();
