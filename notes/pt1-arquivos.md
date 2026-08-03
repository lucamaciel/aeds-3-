# Parte 1 — Arquivos e Estruturas de Índice

Data: 2026-08-03
Tema: Arquivos de dados estruturados em arquivos

## Tipos de arquivo

1. Arquivo sequencial
- Registros armazenados em sequência física.
- Acesso típico: leitura sequencial (varredura).
- Vantagens: simples, eficiente para leituras completas e ordenadas.
- Desvantagens: atualização/insert exige reescrita ou área de overflow; busca por chave é lenta (O(n)) se sem índice.

2. Arquivo indexado
- Mantém estrutura de índice que mapeia chaves para posições no arquivo.
- Permite buscas rápidas por chave sem varrer todo o arquivo.

## Tipos de índice

### 1) Índice por hashing (Hash)
- Usa função de hash sobre a chave para localizar blocos ou buckets.
- Muito eficiente para buscas de igualdade (lookup exato) — tempo O(1) amortizado.
- Problemas: colisões (resolvidas por encadeamento/overflow, rehashing), não adequado para buscas por intervalo.
- Implementações comuns: hashing estático, hashing dinâmico (ex.: extensible hashing, linear hashing).

### 2) Árvore B+ (B+ tree)
- Árvore balanceada com nós internos que apontam para chaves e ponteiros; todas as chaves reais ficam nas folhas.
- Suporta buscas por igualdade e por intervalo (range queries) de forma eficiente (O(log n)).
- Inserções e deleções mantêm a árvore balanceada por split/merge de páginas.
- Muito usada em sistemas de gerência de banco de dados e sistemas de arquivos.

### 3) Lista invertida (Inverted List / Inverted Index)
- Estrutura que mapeia termos (ou valores) para listas de ocorrências (postings) — usada em indexação de texto e recuperação de informação.
- Cada entrada contém a chave/termo e uma lista de referências a registros/documentos onde o termo aparece.
- Eficiente para buscas por termo e combinações booleanas; permite ordenação por frequência, posição, etc.

## Exemplos rápidos
- Buscar um registro por chave exata: usar índice hash ou B+ tree.
- Buscar documentos contendo uma palavra: lista invertida.
- Percorrer registros em ordem: arquivo sequencial ou B+ tree (folhas encadeadas).

## Exercícios sugeridos
1. Implementar um arquivo sequencial simples em arquivo texto; medir tempo de busca por chave com e sem índice.
2. Implementar um índice hash com tratamento de colisões por encadeamento e testar buscas de igualdade.
3. Simular operações de inserção/remoção em uma B+ tree pequena (manual ou código) e mostrar splits/merges.

## Referências
- Silberschatz, Korth e Sudarshan — "Sistemas de Banco de Dados" (capítulo sobre índices).
- Artigos sobre hashing dinâmico e B+ trees.
