# TP4 — Comparação de Algoritmos de Busca de Padrões (KMP vs Boyer-Moore)

## Objetivo
Implementar dois algoritmos de busca de padrões e comparar desempenho em diferentes cenários.

## Descrição
Desenvolva em C, C++, Java ou Python:

1. **Implemente Boyer-Moore (BM)**
   - Heurística do caractere ruim
   - Heurística do sufixo bom (opcional, mas recomendado)
   - Retornar posição do primeiro match (ou todos os matches)

2. **Implemente Knuth-Morris-Pratt (KMP)**
   - Função de falha (failure function)
   - Busca linear sem backtrack
   - Retornar posição do primeiro match (ou todos os matches)

3. **Teste com diferentes padrões**
   - Padrão curto em texto longo
   - Padrão longo em texto longo
   - Padrão repetitivo
   - Padrão que não ocorre
   - Múltiplas ocorrências

4. **Analise performance**
   - Tempo de pré-processamento (construir tabelas)
   - Tempo de busca
   - Número de comparações
   - Teste com arquivo de texto > 1 MB

5. **Gere relatório**
   - Tabela com tempo (em ms) de cada algoritmo
   - Gráfico de desempenho (opcional)
   - Análise: em que casos cada algoritmo é melhor?

## Restrições
- Máximo 200 linhas por algoritmo
- Sem regex ou bibliotecas prontas de busca
- Testar com arquivo > 100 KB

## Entrega
- Código-fonte comentado (BM e KMP)
- Arquivo(s) de teste
- Relatório de desempenho com tabelas
- Até fim semana 15

## Avaliação
- Corretude: ambos algoritmos funcionam 100% (50%)
- Performance: medições precisas e relatório claro (30%)
- Análise: conclusões sobre quando usar cada algoritmo (20%)
