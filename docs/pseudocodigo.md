## 🖥️ Algoritmo em Pseudocódigo (Passo 4)

Usaremos uma notação comum para pseudocódigo (similar ao Portugol) e conceitos básicos de listas/vetores para simular a estrutura de Fila.

### Estrutura de Dados:

  * **Fila\_Pacientes:** Lista/Vetor de registros, onde cada registro contém o `Nome` e o `CPF` do paciente.

### Pseudocódigo

```pseudocode
ALGORITMO Controle_Fila_Atendimento
VAR
    Fila_Pacientes : LISTA DE REGISTROS (Nome: TEXTO, CPF: TEXTO) // Simula a Fila
    i : INTEIRO // Contador
    Paciente_Atendido : REGISTRO (Nome: TEXTO, CPF: TEXTO)
    Nome_Entrada : TEXTO
    CPF_Entrada : TEXTO
INICIO

    // 1. Permite inserir 3 pacientes na fila (nome e CPF)
    PARA i DE 1 ATÉ 3 FAÇA
        ESCREVER "--- Inserindo Paciente ", i, " ---"
        ESCREVER "Digite o Nome do Paciente:"
        LER Nome_Entrada
        ESCREVER "Digite o CPF do Paciente:"
        LER CPF_Entrada
        
        // Operação ENQUEUE (Inserir no final da Fila)
        ADICIONAR {Nome: Nome_Entrada, CPF: CPF_Entrada} NA Fila_Pacientes
        ESCREVER Nome_Entrada, " adicionado(a) à fila."
    FIM_PARA

    ESCREVER "--------------------------------"
    ESCREVER "Fila inicial completa. Total de pacientes: ", TAMANHO(Fila_Pacientes)
    
    // 2. Remova o primeiro paciente da fila para atendimento
    SE TAMANHO(Fila_Pacientes) > 0 ENTÃO
        // Operação DEQUEUE (Remover do início da Fila - FIFO)
        Paciente_Atendido = REMOVER_PRIMEIRO(Fila_Pacientes) 
        
        ESCREVER "--------------------------------"
        ESCREVER "INICIANDO ATENDIMENTO:"
        ESCREVER "Paciente atendido (Saiu da fila): ", Paciente_Atendido.Nome, " (CPF: ", Paciente_Atendido.CPF, ")"
    SENÃO
        ESCREVER "A fila está vazia. Nenhum paciente para atender."
    FIM_SE

    // 3. Mostre quem ainda está na fila após o primeiro atendimento
    ESCREVER "--------------------------------"
    ESCREVER "PACIENTES RESTANTES NA FILA:"
    
    SE TAMANHO(Fila_Pacientes) > 0 ENTÃO
        ESCREVER "Total restante: ", TAMANHO(Fila_Pacientes)
        
        PARA CADA Paciente EM Fila_Pacientes FAÇA
            ESCREVER " - Nome: ", Paciente.Nome, " | CPF: ", Paciente.CPF
        FIM_PARA
    SENÃO
        ESCREVER "A fila está vazia."
    FIM_SE

FIM_ALGORITMO
```

-----

### 📝 Descrição das Operações (Conceito de Fila)

| Conceito | Explicação |
| :--- | :--- |
| **ADICIONAR NA Fila\_Pacientes** | Simula a operação **Enqueue**, onde o novo paciente entra no **final** da fila. |
| **REMOVER\_PRIMEIRO(Fila\_Pacientes)** | Simula a operação **Dequeue**, onde o paciente que está no **início** (o primeiro a entrar) é removido e atendido (FIFO). |

