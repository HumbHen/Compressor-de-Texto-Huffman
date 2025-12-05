import heapq
import os

class HuffmanNode:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.left = None
        self.right = None

    # Permite comparar nós pelo heap
    def __lt__(self, other):
        return self.freq < other.freq

def calcular_frequencias(texto):
    palavras = texto.lower().split()
    freq = {}
    for palavra in palavras:
        freq[palavra] = freq.get(palavra, 0) + 1
    return freq

def construir_arvore(freq):
    heap = []

    for palavra, f in freq.items():
        heapq.heappush(heap, HuffmanNode(palavra, f))

    while len(heap) > 1:
        no1 = heapq.heappop(heap)
        no2 = heapq.heappop(heap)
        novo = HuffmanNode(None, no1.freq + no2.freq)
        novo.left = no1
        novo.right = no2
        heapq.heappush(heap, novo)

    return heap[0]

def desenhar_arvore_ascii(no, prefixo="", eh_ultimo=True):
    if no is None:
        return ""

    linha = prefixo
    linha += "└── " if eh_ultimo else "├── "

    if no.word is None:
        linha += f"* ({no.freq})\n"
    else:
        linha += f"{no.word} ({no.freq})\n"

    prefixo += "    " if eh_ultimo else "│   "

    esquerda = desenhar_arvore_ascii(no.left, prefixo, False)
    direita  = desenhar_arvore_ascii(no.right, prefixo, True)

    return linha + esquerda + direita

def gerar_codigos(no, codigo_atual="", codigos={}):
    if no is None:
        return

    if no.word is not None:
        codigos[no.word] = codigo_atual

    gerar_codigos(no.left, codigo_atual + "0", codigos)
    gerar_codigos(no.right, codigo_atual + "1", codigos)

    return codigos

def comprimir(texto, codigos):
    palavras = texto.lower().split()
    comprimido = "".join(codigos[p] for p in palavras)
    return comprimido

def processar():
    caminho = os.path.join("data", "input.dat")
    with open(caminho, "r", encoding="utf-8") as f:
        textos = f.read().strip().split("\n\n")

    saida = ""

    for i, texto in enumerate(textos):
        freq = calcular_frequencias(texto)
        arvore = construir_arvore(freq)
        codigos = gerar_codigos(arvore)
        texto_comprimido = comprimir(texto, codigos)

        saida += f"TEXTO {i+1}:\n"
        saida += f"Árvore de Huffman:\n{ desenhar_arvore_ascii(arvore) }\n"
        saida += f"Frequências: {freq}\n"
        saida += f"Códigos: {codigos}\n"
        saida += f"Comprimido: {texto_comprimido}\n\n"

    with open(os.path.join("data", "output.dat"), "w", encoding="utf-8") as f:
        f.write(saida)

    print("Processamento concluído! Arquivo output.dat gerado em /data.")

if __name__ == "__main__":
    processar()
