import matplotlib.pyplot as plt
import numpy as np
import imageio.v2 as imageio
import os
import shutil

# Limpar e criar diretório para os frames
if os.path.exists('frames_binary'):
    shutil.rmtree('frames_binary')
os.makedirs('frames_binary')

frames = []

def capture_frame(array, esquerda, direita, meio, valor_busca, encontrado=False, frame_number=0, descricao=""):
    """Captura um quadro da busca binária mostrando apenas o intervalo atual."""
    fig = plt.figure(figsize=(14, 4))
    ax = plt.gca()
    
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    # Desenhando círculos com números
    for i, num in enumerate(array):
        if i >= esquerda and i <= direita:
            if i == meio:
                color = 'red' if not encontrado else 'green'
            else:
                color = 'lightblue'
            circle = plt.Circle((i, 0), 0.3, color=color)
            ax.add_patch(circle)
            ax.text(i, 0, str(num), ha='center', va='center', fontsize=14, fontweight='bold')
        else:
            circle = plt.Circle((i, 0), 0.3, color='gray', fill=False, linestyle='--', alpha=0.3)
            ax.add_patch(circle)
    
    # Título com descrição do passo atual
    title = f"Busca Binária: procurando {valor_busca}\n"
    title += descricao
    ax.set_title(title, pad=20)
    
    # Salvando o frame
    frame_path = f'frames_binary/frame_{frame_number:03d}.png'
    plt.savefig(frame_path, bbox_inches='tight', dpi=100)
    plt.close()
    
    frame = imageio.imread(frame_path)
    frames.append(frame)

def busca_binaria(vetor, valor):
    frame_count = 0
    esquerda = 0
    direita = len(vetor) - 1
    
    # Frame inicial
    capture_frame(vetor, esquerda, direita, -1, valor, frame_number=frame_count,
                 descricao="Estado inicial do vetor com 7 elementos")
    frame_count += 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        # Frame mostrando a comparação atual
        descricao = f"Comparando {valor} com elemento do meio ({vetor[meio]})"
        capture_frame(vetor, esquerda, direita, meio, valor, frame_number=frame_count,
                     descricao=descricao)
        frame_count += 1
        
        if vetor[meio] == valor:
            capture_frame(vetor, esquerda, direita, meio, valor, True, frame_number=frame_count,
                        descricao=f"Valor {valor} encontrado na posição {meio}!")
            return meio, frame_count
        elif vetor[meio] < valor:
            descricao = f"{valor} > {vetor[meio]}, procurando na metade direita"
            esquerda = meio + 1
        else:
            descricao = f"{valor} < {vetor[meio]}, procurando na metade esquerda"
            direita = meio - 1
        
        if esquerda <= direita:
            capture_frame(vetor, esquerda, direita, -1, valor, frame_number=frame_count,
                        descricao=descricao)
            frame_count += 1
    
    capture_frame(vetor, -1, -1, -1, valor, frame_number=frame_count,
                 descricao="Valor não encontrado no vetor")
    return -1, frame_count

# Vetor ordenado para teste
vetor = [2, 4, 8, 10, 12, 18, 21]
valor_busca = 21

# Realizando a busca e gerando frames
posicao, total_frames = busca_binaria(vetor, valor_busca)

# Salvando o GIF
imageio.mimsave('binary_search.gif', frames, duration=2.5)

print(f"\nBusca concluída! Valor {valor_busca} encontrado na posição {posicao}")
print(f"GIF salvo como 'binary_search.gif'")
print(f"Imagens passo a passo salvas na pasta 'frames_binary/'")
print(f"Total de passos: {total_frames}")
print("\nDescrição dos arquivos gerados:")
for i in range(total_frames):
    print(f"frame_{i:03d}.png - Passo {i+1} da busca")