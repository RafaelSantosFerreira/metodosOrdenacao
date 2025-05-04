public static void bubbleSort(int[] arr) {
        int n = arr.length;
        // Para cada elemento do array
        for (int i = 0; i < n; i++) {
            // Percorre do início até o penúltimo elemento não ordenado
            for (int j = 0; j < n - 1; j++) {
                // Se o elemento atual for maior que o próximo, troca-os
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }