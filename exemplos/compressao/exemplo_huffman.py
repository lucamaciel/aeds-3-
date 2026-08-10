# Exemplo: Codificação Huffman em Python
# Autor: AEDS III
# Usar: python3 exemplo_huffman.py

import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    """Construir árvore de Huffman a partir do texto"""
    freq = Counter(text)
    heap = [Node(char=char, freq=count) for char, count in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        parent = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, parent)
    
    return heap[0]

def build_codes(node, prefix="", codes=None):
    """Gerar tabela de códigos a partir da árvore"""
    if codes is None:
        codes = {}
    
    if node.char is not None:
        codes[node.char] = prefix if prefix else "0"
        return codes
    
    if node.left:
        build_codes(node.left, prefix + "0", codes)
    if node.right:
        build_codes(node.right, prefix + "1", codes)
    
    return codes

def compress(text):
    """Comprimir texto usando Huffman"""
    tree = build_huffman_tree(text)
    codes = build_codes(tree)
    compressed = "".join(codes[char] for char in text)
    return compressed, codes, tree

def decompress(compressed, codes):
    """Descomprimir texto usando tabela de códigos"""
    reverse_codes = {v: k for k, v in codes.items()}
    text = ""
    current = ""
    
    for bit in compressed:
        current += bit
        if current in reverse_codes:
            text += reverse_codes[current]
            current = ""
    
    return text

# Teste
if __name__ == "__main__":
    texto_original = "aaabbbcccdde"
    
    compressed, codes, tree = compress(texto_original)
    taxa = (len(texto_original) * 8 - len(compressed)) / (len(texto_original) * 8) * 100
    
    print(f"Original: {texto_original}")
    print(f"Comprimido: {compressed}")
    print(f"Tabela de códigos: {codes}")
    print(f"Taxa de compressão: {taxa:.2f}%")
    
    descomprimido = decompress(compressed, codes)
    print(f"Descomprimido: {descomprimido}")
    print(f"Correto: {texto_original == descomprimido}")
