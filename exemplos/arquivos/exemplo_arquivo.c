// Exemplo: Leitura e Escrita de Registros em Arquivo Binário (C)
// Autor: AEDS III
// Compilar: gcc exemplo_arquivo.c -o exemplo_arquivo

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    char nome[50];
    double valor;
} Registro;

void escrever_registros(const char *arquivo, int quantidade) {
    FILE *f = fopen(arquivo, "wb");
    if (!f) {
        perror("Erro ao abrir arquivo");
        return;
    }
    
    for (int i = 1; i <= quantidade; i++) {
        Registro reg;
        reg.id = i;
        snprintf(reg.nome, 50, "Registro_%d", i);
        reg.valor = i * 10.5;
        
        fwrite(&reg, sizeof(Registro), 1, f);
    }
    
    fclose(f);
    printf("Escritos %d registros em %s\n", quantidade, arquivo);
}

Registro ler_registro_aleatorio(const char *arquivo, int indice) {
    FILE *f = fopen(arquivo, "rb");
    if (!f) {
        perror("Erro ao abrir arquivo");
        exit(1);
    }
    
    fseek(f, indice * sizeof(Registro), SEEK_SET);
    
    Registro reg;
    fread(&reg, sizeof(Registro), 1, f);
    fclose(f);
    
    return reg;
}

int main() {
    const char *arquivo = "dados.bin";
    
    // Escrever 1000 registros
    escrever_registros(arquivo, 1000);
    
    // Ler alguns registros aleatoriamente
    for (int i = 0; i < 5; i++) {
        int idx = (i * 200) % 1000;
        Registro reg = ler_registro_aleatorio(arquivo, idx);
        printf("Registro %d: ID=%d, Nome=%s, Valor=%.2f\n", idx, reg.id, reg.nome, reg.valor);
    }
    
    return 0;
}
