# Parte 2 — Compressão, Criptografia e Casamento de Padrões

Data: 2026-08-03
Tema: Compressão de dados, criptografia e casamento de padrões

## 1. Compressão de dados
Objetivo: reduzir espaço usando redundância e modelos estatísticos.

- Lossless vs Lossy
  - Lossless: recupera os dados exatamente (Huffman, LZ77/LZ78, DEFLATE).
  - Lossy: perda de informação aceitável para ganhos maiores (JPEG, MP3).

- Algoritmos comuns
  - Run-Length Encoding (RLE): bom para dados com repetições longas.
  - Huffman Coding: codificação ótima por símbolos com base em frequências.
  - LZ77 / LZ78 / LZW: dicionário baseado em substrings vistas antes (usado em ZIP, PNG, GIF).
  - Burrows–Wheeler Transform + Move-to-Front + Huffman (BWT pipeline, usado em bzip2).

- Métricas e considerações
  - Taxa de compressão, tempo de compressão/descompressão, memória.
  - Compressão em streaming vs blocos; compressão adaptativa.

## 2. Criptografia
Objetivo: confidencialidade, integridade, autenticação e não repúdio.

- Fundamentos
  - Chave simétrica: mesma chave para cifrar/decifrar (AES, DES). Rápida, exige distribuição segura de chaves.
  - Chave assimétrica (public-key): par (publica, privada) — usado para troca de chaves, assinaturas (RSA, ECC).
  - Hashing: funções unidirecionais para integridade (SHA-2, SHA-3); cuidado com colisões.

- Protocolos e usos
  - Criptografia híbrida: usar RSA/ECC para trocar uma chave simétrica e AES para cifrar dados.
  - Assinaturas digitais: garantir autoria e integridade (RSA-PSS, ECDSA).
  - MACs e HMAC: autenticação de mensagem com chave secreta.

- Boas práticas
  - Use bibliotecas testadas; não invente esquemas.
  - Use modos de operação seguros (AES-GCM, AES-CBC+HMAC quando necessário).
  - Proteja chaves (keystores, hardware) e trate randomização (IVs, nonces) corretamente.

## 3. Casamento de Padrões (Pattern Matching)
Objetivo: localizar ocorrências de um padrão em texto ou sequência.

- Abordagens
  - Força bruta (Naive): comparar em cada posição — O(nm).
  - KMP (Knuth–Morris–Pratt): pré-processa padrão em tabela de prefixos — O(n+m).
  - Boyer–Moore: heurísticas (bad-char, good-suffix) — bom em prática, pulos grandes.
  - Rabin–Karp: hashing de janelas, bom para múltiplos padrões e verificações rápidas (possui colisões a tratar).

- Variantes e aplicações
  - Aho–Corasick: conjunto de padrões simultâneos — ideal para detecção de múltiplos termos.
  - Sufix arrays / sufíx trees: indexação para buscas rápidas e problemas de string avançados.
  - Expressões regulares: engines que combinam automatos e backtracking; desempenho depende da implementação.

## Exemplos rápidos
- Compressão: comprimir um arquivo de logs com gzip (DEFLATE) para reduzir armazenamento.
- Criptografia: cifrar um arquivo com AES-GCM e proteger a chave com RSA.
- Casamento: usar KMP para localizar um padrão em um texto longo.

## Exercícios sugeridos
1. Implementar Huffman coding (freq table, árvore, códigos) e testar com texto.
2. Implementar LZ77 simplificado: buffer deslizante e referências (offset,length,next).
3. Cifrar e decifrar arquivos com AES-GCM usando uma biblioteca; comparar com AES-CBC+HMAC.
4. Implementar KMP e comparar tempo com busca naive em textos grandes.
5. Implementar Aho–Corasick para detectar múltiplas palavras-chave em uma coleção de documentos.

## Referências
- Sayood — "Introduction to Data Compression".
- Katz/Vanstone — "Handbook of Applied Cryptography".
- Gusfield — "Algorithms on Strings, Trees and Sequences".



