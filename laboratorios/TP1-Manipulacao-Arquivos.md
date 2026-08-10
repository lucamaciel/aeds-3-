# TP1 — Manipulação Eficiente de Arquivos Binários

## Objetivo
Implementar um sistema de leitura e escrita eficiente de dados em arquivos binários, com suporte a índices e acesso aleatório.

## Descrição
Desenvolva uma biblioteca em C, C++, Java ou Python que:

1. **Leia e escreva registros em arquivo binário** com formato estruturado
   - Cada registro: ID (4 bytes), nome (50 bytes), valor (8 bytes double)
   - Escrever 1.000 registros em arquivo

2. **Implemente acesso aleatório**
   - Função para ler registro por índice (sem ler arquivo inteiro)
   - Usar `fseek()` ou equivalente

3. **Crie um índice**
   - Arquivo separado com posições (offset) de cada registro
   - Permitir busca rápida por ID

4. **Compare performance**
   - Leitura sequencial vs. aleatória
   - Com buffer vs. sem buffer
   - Gerar relatório de tempo (em ms)

## Restrições
- Máximo 100 linhas por linguagem
- Sem uso de bibliotecas prontas de serialização
- Testar com arquivo > 10 MB

## Entrega
- Código-fonte comentado
- Arquivo binário de teste
- Relatório de performance
- Até fim semana 5

## Avaliação
- Corretude: registros lidos/escritos corretamente (60%)
- Desempenho: otimizações de I/O implementadas (30%)
- Documentação: código claro e comentado (10%)
