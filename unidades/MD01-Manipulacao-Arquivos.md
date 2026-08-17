# MD01 — Manipulação de Dados em Arquivos

## Objetivos
Compreender técnicas de leitura, escrita e manipulação eficiente de dados em arquivos. Explorar estruturas de índices e acesso sequencial vs. aleatório.

## Conteúdo

### 1. Conceitos Fundamentais
- Tipos de arquivo: texto vs. binário
- Streams de I/O e buffers
- Modos de abertura: leitura, escrita, append
- Codificação de caracteres (UTF-8, ASCII, etc.)

### 2. I/O Eficiente
- Buffering e suas vantagens
- Leitura em blocos vs. byte-a-byte
- Random Access vs. Sequential Access
- Mapeamento de memória (memory-mapped files)

### 3. Estruturas de Dados em Arquivo
- Serialização de objetos
- Arquivos binários estruturados
- Índices e chaves primárias
- Acesso por offset e tamanho de registro

### 4. Operações Avançadas
- Merge de arquivos
- Classificação externa (quando dados > memória disponível)
- Compactação de arquivos
- Recuperação de dados corrompidos

## Trabalhos Práticos Relacionados
- **TP1** — Implementar leitor/escritor eficiente de arquivos binários

## Referências
- Cormen, Leiserson, Rivest, Stein — "Introduction to Algorithms"
- Knuth — "The Art of Computer Programming"
