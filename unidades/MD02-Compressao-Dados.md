# MD02 — Compressão de Dados

## Objetivos
Aprender algoritmos de compressão sem perda e suas aplicações. Compreender trade-offs entre razão de compressão, velocidade e uso de memória.

## Conteúdo

### 1. Teoria da Compressão
- Entropia de Shannon
- Razão de compressão e limite teórico
- Compressão com perda vs. sem perda
- Aplicações práticas

### 2. Algoritmos de Compressão Simples
- **Run-Length Encoding (RLE)** — Codificação de sequências repetidas
- **Huffman Coding** — Árvore ótima baseada em frequência
- **LZ77/LZ78** — Família de algoritmos dicionário-baseados

### 3. Huffman Coding em Profundidade
- Construção da árvore de Huffman
- Codificação e decodificação
- Casos de uso: JPEG, MP3, DEFLATE
- Complexity: O(n log n)

### 4. Compressão LZ (Lempel-Ziv)
- LZ77: Janela deslizante de referências
- LZ78: Dicionário adaptativo
- DEFLATE: Combinação de LZ77 + Huffman
- Aplicações: ZIP, GZIP, PNG

### 5. Medição de Performance
- Taxa de compressão
- Tempo de compressão/descompressão
- Uso de memória
- Trade-offs práticos

## Trabalhos Práticos Relacionados
- **TP2** — Implementar compressor Huffman ou RLE

## Referências
- Salomon, Motta — "Handbook of Data Compression"
- IEEE standard for data compression
