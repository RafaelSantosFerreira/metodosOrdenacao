import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

# Dados iniciais
data = [5, 3, 8, 4, 2]
frames = []

# Criar diretório para os frames se não existir
if not os.path.exists('frames'):
    os.makedirs('frames')

def capture_frame(array, highlight=[], frame_number=0):
    """Captura um quadro da ordenação com círculos e números."""
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # Configurando o plot
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-1, 1)
    ax.axis('off')  # Remove os eixos
    
    # Desenhando círculos com números
    for i, num in enumerate(array):
        circle = plt.Circle((i, 0), 0.3, color='lightblue' if i not in highlight else 'red')
        ax.add_patch(circle)
        # Adicionando o número dentro do círculo
        ax.text(i, 0, str(num), ha='center', va='center', fontsize=14, fontweight='bold')
    
    ax.set_title("Bubble Sort: Ordenação passo a passo", pad=20)
    
    # Salvando o frame como PNG numerado - Corrigindo a formatação da string
    frame_path = os.path.join('frames', f'frame_{frame_number:03d}.png')
    plt.savefig(frame_path, bbox_inches='tight', dpi=100)
    plt.close()
    
    # Lendo a imagem salva para o GIF
    frame = imageio.imread(frame_path)
    frames.append(frame)

# Algoritmo Bubble Sort com captura de quadros
arr = data.copy()
n = len(arr)
frame_count = 0

# Capturando estado inicial
capture_frame(arr, frame_number=frame_count)
frame_count += 1

for i in range(n):
    
    for j in range(0, n  - 1):
        # Destacando elementos sendo comparados
        capture_frame(arr, [j, j+1], frame_number=frame_count)
        frame_count += 1
        
        if arr[j] > arr[j + 1]:
            # Realizando a troca
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # Mostrando após a troca
            #capture_frame(arr, [j, j+1], frame_number=frame_count)
            #frame_count += 1
        print(arr)

# Capturando estado final
capture_frame(arr, frame_number=frame_count)

# Salvando o GIF
imageio.mimsave('bubble_sort.gif', frames, duration=2.5)

print(f"GIF salvo como 'bubble_sort.gif'")
print(f"Frames individuais salvos na pasta 'frames/' (total de {frame_count + 1} frames)")
