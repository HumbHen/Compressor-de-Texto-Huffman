# Implementação do Algoritmo de Huffman para Compressão de Texto

Este projeto implementa o algoritmo de **Huffman** para compressão de pequenos trechos de texto, conforme solicitado na disciplina **Algoritmos e Estruturas de Dados II** (CEFET-MG).

A compressão é realizada considerando **palavras como símbolos**, como especificado no enunciado do trabalho. O programa lê textos de um arquivo, calcula frequências, constrói a árvore de Huffman, gera códigos binários e produz um arquivo de saída contendo todas as informações necessárias para análise e possível decodificação.

---

## Funcionalidades

O programa:

- Lê textos do arquivo `data/input.dat`
- Calcula a frequência de cada **palavra**
- Constrói a **árvore de Huffman**
- Gera o código binário de cada palavra
- Comprime o texto de entrada
- Gera o arquivo `data/output.dat` contendo:
  - Estrutura textual da árvore de Huffman
  - Frequências das palavras
  - Códigos binários gerados
  - Texto comprimido

---

## Estrutura do Projeto

huffman-compressor/  
├── data/  
│   ├── input.dat       # Textos de entrada  
│   └── output.dat      # Resultado da compressão  
├── main.py             # Implementação principal  
└── README.md           # Este arquivo

---

## Como Executar

1. Certifique-se de ter o **Python 3** instalado.  
2. Abra o terminal na pasta do projeto.  
3. Execute:

    python3 main.py

4. O arquivo `data/output.dat` será gerado automaticamente.

---

## Sobre o Algoritmo de Huffman

O algoritmo de Huffman é uma técnica de compressão **sem perdas**, que usa a frequência dos símbolos para gerar códigos binários eficientes.

Características principais:

- Símbolos mais frequentes → códigos menores  
- Símbolos menos frequentes → códigos maiores  
- Os códigos são **prefix-free** (nenhum código é prefixo de outro)  
- A árvore é construída com uma **fila de prioridade (min-heap)**

O resultado final é uma representação mais compacta do texto original.

---

## Exemplo de Saída

TEXTO 1:  
Árvore de Huffman:  
└── * (12)  
    ├── ...  

Frequências: {'dados': 1, 'processa': 1, ...}  
Códigos: {'dados': '000', 'processa': '001', ...}  
Comprimido: 1100101011011001...

---

## Tecnologias Utilizadas

- Python 3  
- Estruturas de Dados: Árvore Binária e Heap  
- Manipulação de Arquivos `.dat`

---

## Autor

Humberto Henrique Lima Cunha  
Disciplina: Algoritmos e Estruturas de Dados II — CEFET-MG  
Data de entrega: 06/12/2025
