# TP3 — Implementação de Criptografia AES ou RSA

## Objetivo
Implementar um sistema básico de criptografia simétrica (AES) ou assimétrica (RSA) com entrada/saída em arquivo.

## Descrição
Escolha uma das opções:

### Opção A: Criptografia Simétrica (AES-128)
1. **Implementar (ou usar biblioteca nativa) AES-128-CBC**
   - Função de encriptação com chave e IV fornecidos
   - Função de desencriptação
   - Padding PKCS#7 para dados não-múltiplos de 16 bytes

2. **Ler arquivo de texto**
   - Encriptar com chave gerada aleatoriamente
   - Escrever arquivo encriptado + chave em disco

3. **Desencriptar**
   - Ler arquivo encriptado e chave
   - Recuperar arquivo original
   - Validar que original e desencriptado são idênticos

### Opção B: Criptografia Assimétrica (RSA-2048)
1. **Gerar par de chaves** (pública e privada)
   - Salvar em arquivo PEM (ou formato binário)
   
2. **Encriptar mensagem**
   - Usar chave pública
   - Encriptar arquivo pequeno (<128 bytes de dados)
   - Escrever criptograma em arquivo

3. **Desencriptar**
   - Usar chave privada
   - Recuperar mensagem original
   - Validar integridade

## Restrições
- Máximo 200 linhas de código (pode usar OpenSSL, PyCryptodome, etc.)
- Testar com arquivo real (> 1 KB)
- Documento a chave e IV utilizados

## Entrega
- Código-fonte comentado
- Arquivos de teste (original, encriptado)
- Instruções de uso
- Até fim semana 13

## Avaliação
- Corretude: encriptação/desencriptação funciona 100% (60%)
- Segurança: uso correto de chaves e IV (20%)
- Documentação: código claro e explicado (20%)
