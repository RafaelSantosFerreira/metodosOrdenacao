public class BuscaBinaria {

    public static int busca_binaria(int[] vetor, int valor) {
        int esquerda = 0;
        int direita = vetor.length - 1;

        while (esquerda <= direita) {
            int meio = (esquerda + direita) / 2;

            if (vetor[meio] == valor) {
                return meio;
            } else if (vetor[meio] < valor) {
                esquerda = meio + 1;
            } else {
                direita = meio - 1;
            }
        }

        return -1; // Valor não encontrado
    }

    public static void main(String[] args) {
        int[] vetor = {2, 4, 8, 10, 12, 18, 21};
        int valor = 21;

        int posicao = busca_binaria(vetor, valor);

        if (posicao != -1) {
            System.out.println("Valor " + valor + " encontrado na posição: " + posicao);
        } else {
            System.out.println("Valor " + valor + " não encontrado.");
        }
    }
}
