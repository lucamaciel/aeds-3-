# Exercício — Parte 1: Arquivos e Índices

Objetivo
- Implementar e comparar um índice hash e uma B+ tree simples para busca por chave em arquivos.

Descrição
1. Criar um arquivo de registros (texto ou binário) com N registros (id, nome, outros campos).
2. Implementar um índice por hashing (encadeamento por lista ou bucket) que mapeie chave -> posição no arquivo.
3. Implementar uma B+ tree simplificada que mantenha chaves e ponteiros para registros (apenas operações de busca e inserção obrigatórias).
4. Comparar tempo de busca por chave (média) entre: varredura sequencial, índice hash e B+ tree.

Requisitos
- Linguagem: qualquer (informe na entrega).
- Fornecer scripts para gerar dados de teste (N pelo menos 10000).
- Medir tempos com diferentes tamanhos (N) e documentar resultados.

Entrega
- exercises/pt1/<seunome>/enunciado.md (se quiser subdividir)
- solutions/pt1/<seunome>/ (código e relatório)
- README com instruções de execução e dependências

Arquivo de suporte (opcional)
- starter/pt1/hash_index.py  (se desejar, posso gerar)

Critérios de avaliação
- Correção das buscas
- Documentação das medições
- Organização do código

