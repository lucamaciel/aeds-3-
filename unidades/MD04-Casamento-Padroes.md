# MD04 — Casamento de Padrões

## Objetivos
Implementar e analisar algoritmos eficientes de busca de padrões em textos. Explorar aplicações em bioinformática, recuperação de informação e detecção de plágio.

## Conteúdo

### 1. Conceitos Fundamentais
- Problema: buscar padrão P em texto T
- Complexidade naive: O(n*m)
- Aplicações: busca em arquivos, bioinformática, antivírus
- Métricas: falsos positivos/negativos

### 2. Boyer-Moore (BM)
- Heurística do caractere ruim (bad-character)
- Heurística do sufixo bom (good-suffix)
- Complexidade: O(n/m) no melhor caso, O(n*m) no pior
- Implementação e otimizações

### 3. Knuth-Morris-Pratt (KMP)
- Tabela de falhas (failure function)
- Busca linear sem backtrack
- Complexidade: O(n + m)
- Melhor para padrões com repetições

### 4. Rabin-Karp (RK)
- Hashing de padrão e substrings
- Busca por rolagem de hash
- Complexidade: O(n + m) esperado, O(n*m) pior caso
- Múltiplos padrões simultâneos

### 5. Expressões Regulares
- Definição de padrões flexíveis
- Autômatos finitos (DFA, NFA)
- Engines: Thompson NFA, Pike VM
- Aplicações: validação, extração de dados

### 6. Aplicações Avançadas
- Busca de múltiplos padrões (Aho-Corasick)
- Distância de edição (Levenshtein)
- Detecção de similaridade
- Busca aproximada (fuzzy matching)

## Trabalhos Práticos Relacionados
- **TP4** — Implementar e comparar KMP vs. Boyer-Moore

## Referências
- Cormen, Leiserson, Rivest, Stein — "Introduction to Algorithms"
- Gusfield — "Algorithms on Strings, Trees, and Sequences"
