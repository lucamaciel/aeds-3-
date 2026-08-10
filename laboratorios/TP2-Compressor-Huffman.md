# TP2 — Compressor Huffman

## Objetivo
Implementar um algoritmo de compressão Huffman sem perda, com análise de performance.

## Descrição
Desenvolva um compressor em C, C++, Java ou Python que:

1. **Leia um arquivo de texto**
   - Analisar frequência de cada caractere
   - Construir árvore de Huffman
   - Gerar tabela de códigos

2. **Comprima o arquivo**
   - Escrever arquivo comprimido com formato binário
   - Incluir tabela de códigos no arquivo para descompressão

3. **Descomprima**
   - Ler arquivo comprimido e recuperar original
   - Validar que arquivo original e descomprimido são idênticos

4. **Analise performance**
   - Taxa de compressão: (tamanho_original - tamanho_comprimido) / tamanho_original
   - Tempo de compressão e descompressão (em ms)
   - Teste com arquivos de tamanhos: 1 KB, 100 KB, 1 MB

## Restrições
- Máximo 150 linhas de código
- Sem uso de bibliotecas de compressão prontas
- Suportar alfabeto de 256 caracteres

## Entrega
- Código-fonte comentado
- Arquivos de teste (texto puro)
- Relatório de taxa de compressão
- Até fim semana 8

## Avaliação
- Corretude: compressão/descompressão funciona 100% (60%)
- Eficiência: taxa de compressão razoável (20%)
- Performance: tempo aceitável (<1s para 1MB) (20%)
