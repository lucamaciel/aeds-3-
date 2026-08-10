# MD03 — Criptografia e Segurança

## Objetivos
Compreender conceitos fundamentais de criptografia. Explorar algoritmos simétricos e assimétricos e suas aplicações em proteção de dados.

## Conteúdo

### 1. Fundamentos de Criptografia
- Confidencialidade, integridade, autenticação
- Chaves: simétricas vs. assimétricas
- Força de criptografia e tamanho de chave
- Ataques comuns: brute-force, frequency analysis, etc.

### 2. Criptografia Simétrica
- **DES (Data Encryption Standard)** — 56 bits, histórico
- **AES (Advanced Encryption Standard)** — 128/192/256 bits, padrão atual
- Modos de operação: ECB, CBC, CTR, GCM
- Inicialização vetorial (IV) e suas propriedades

### 3. Criptografia Assimétrica
- **RSA** — Segurança baseada em fatoração
  - Geração de chaves
  - Encriptação e descriptação
  - Assinatura digital
- **Diffie-Hellman** — Acordo de chaves
- Tamanhos de chave: 2048, 4096 bits

### 4. Hash Criptográfico
- Funções hash: MD5, SHA-1, SHA-256, SHA-3
- Propriedades: determinístico, rápido, unidirecional
- Uso: integridade de dados, assinaturas, senhas

### 5. Aplicações Práticas
- HTTPS e certificados digitais
- Criptografia de dados em repouso
- Armazenamento seguro de senhas (bcrypt, argon2)
- Blockchain e assinaturas

## Trabalhos Práticos Relacionados
- **TP3** — Implementar encriptação AES ou RSA básico

## Referências
- Stallings, Brown — "Computer Security: Principles and Practice"
- NIST Cryptographic Standards
