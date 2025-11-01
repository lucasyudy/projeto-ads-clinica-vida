## 📄 Relatório de Revisão da Sprint 2

**Projeto:** Desenvolvimento de uma Plataforma de Saúde - Clínica Vida+
**Time:** Lucas Yudy
**Sprint:** 2 (Estatísticas, Busca e Lógica Booleana)
**Duração da Sprint:** [7dias]

### 1. 🎯 Objetivo da Sprint 2

O objetivo desta Sprint foi **completar integralmente os requisitos do sistema Python (Passo 2)**, entregando as funcionalidades de análise de dados e busca. Adicionalmente, foi iniciada a **modelagem da lógica** do sistema de controle de acesso (Passo 3) para manter o avanço do projeto.

### 2. ✅ Entregas Concluídas (Resultado da Sprint)

Todos os itens planejados para esta Sprint foram concluídos, garantindo que o sistema Python atenda a todas as necessidades iniciais da Sra. Helena.

| ID | Item do Backlog (Cartão Trello) | Status | Observações / Valor Entregue |
| :---: | :--- | :--- | :--- |
| **005** | Funcionalidade: Calcular e Exibir Estatísticas | **Concluído** | Implementação que calcula e exibe o número total, a idade média, e o paciente mais novo/velho, conforme solicitado. |
| **006** | Funcionalidade: Buscar Paciente por Nome | **Concluído** | Função implementada que permite buscar pacientes por nome (busca parcial) e exibe os dados organizados. |
| **007** | Implementar Tratamento de Erros de Entrada | **Concluído** | Aprimoramento do código Python para tratar *inputs* não numéricos (Idade) e entradas vazias, tornando o sistema mais robusto. |
| **008** | Modelagem da Lógica Booleana (Passo 3) | **Concluído** | Tradução das regras de atendimento (Consulta Normal e Emergência) para expressões lógicas e construção das Tabelas Verdade completas (16 linhas). |

### 3. 🚧 Impedimentos e Desafios Encontrados

* **Desafio de Lógica (005):** Garantir que o cálculo de estatísticas não gerasse erros em listas vazias (divisão por zero), o que exigiu a implementação de uma validação inicial na função `ver_estatisticas`.
* **Ajuste de Esforço (008):** A modelagem do Passo 3, embora lógica, demandou tempo considerável devido à complexidade da Tabela Verdade de 16 linhas, validando a decisão de priorizá-la nesta Sprint.

### 4. 📈 Retrospectiva da Sprint (O que aprender/melhorar)

| O que deu Certo? | O que pode ser Melhorado? | Ação para a Próxima Sprint |
| :--- | :--- | :--- |
| **Completude do Passo 2:** O sistema Python (menu, cadastro, listar, estatísticas, busca) está 100% funcional, eliminando dívida técnica do Passo 2. | **Balanceamento de Esforço:** A próxima Sprint foca em modelagem/algoritmos (Passos 4 e 5), o que pode ser menos visível. É preciso garantir que o **Diagrama de Casos de Uso (Passo 5)** seja bem detalhado. | **Refinamento do Passo 5:** Dedicar tempo na próxima Sprint para um refinamento visual e técnico do Diagrama de Casos de Uso. |
| **Antecipação:** A inclusão do CPF na Sprint 1 facilitou a implementação do Passo 2 e 3 (documentos OK). |  |  |

### 5. 🔜 Planejamento para a Próxima Sprint (Sprint 3)

A próxima Sprint se concentrará em modelagem e algoritmos, cobrindo os últimos passos do projeto antes da conclusão.

* **Objetivo da Sprint 3:** Entregar a modelagem do fluxo de atendimento (Fila) e a arquitetura de funcionalidades do sistema (Casos de Uso).
* **Principais Itens do Backlog para a Sprint 3:**
    * Elaborar o **Algoritmo em Pseudocódigo** para a Fila de Atendimento (Passo 4).
    * Elaborar o **Diagrama de Casos de Uso** (Passo 5).
