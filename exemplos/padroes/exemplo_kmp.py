# Exemplo: KMP (Knuth-Morris-Pratt) String Matching em Python
# Autor: AEDS III
# Usar: python3 exemplo_kmp.py

def compute_failure_function(pattern):
    """Computar função de falha (failure function) para KMP"""
    m = len(pattern)
    failure = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        failure[i] = j
    
    return failure

def kmp_search(text, pattern):
    """Buscar padrão em texto usando KMP"""
    n = len(text)
    m = len(pattern)
    failure = compute_failure_function(pattern)
    matches = []
    j = 0
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == m:
            matches.append(i - m + 1)
            j = failure[j - 1]
    
    return matches

def boyer_moore_search(text, pattern):
    """Buscar padrão em texto usando Boyer-Moore (simplificado)"""
    n = len(text)
    m = len(pattern)
    matches = []
    
    # Tabela de último caractere (bad character rule)
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    
    i = m - 1
    j = m - 1
    
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                matches.append(i)
                i += 1
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            shift = max(1, j - last.get(text[i], -1))
            i += m - j + shift - 1
            j = m - 1
    
    return matches

# Teste
if __name__ == "__main__":
    text = "ababcababa"
    pattern = "aba"
    
    print(f"Texto: {text}")
    print(f"Padrão: {pattern}")
    
    kmp_matches = kmp_search(text, pattern)
    bm_matches = boyer_moore_search(text, pattern)
    
    print(f"KMP: encontrou em posições {kmp_matches}")
    print(f"Boyer-Moore: encontrou em posições {bm_matches}")
