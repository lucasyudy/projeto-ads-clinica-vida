## Relatório de Revisão da Sprint 1

**Projeto:** Desenvolvimento de uma Plataforma de Saúde - Clínica Vida+
**Time:** Lucas Yudy
**Sprint:** 1 (Infraestrutura e Cadastro Básico)
**Duração da Sprint:** [7dias]

### 1. Objetivo da Sprint 1

O objetivo desta Sprint foi estabelecer a **infraestrutura de gestão (Trello)** e construir a **espinha dorsal do sistema Python**, implementando o menu de navegação e as funcionalidades essenciais de cadastro e listagem de pacientes.

### 2. ✅ Entregas Concluídas (Resultado da Sprint)

Nesta Sprint, todos os itens planejados foram movidos para a coluna **"Concluído"**.

| ID | Item do Backlog (Cartão Trello) | Status | Observações / Valor Entregue |
| :---: | :--- | :--- | :--- |
| **001** | Configuração Inicial do Projeto | **Concluído** | Configuração do ambiente Python e criação do quadro Scrum no Trello. |
| **002** | Implementar Menu Principal (Loop) | **Concluído** | O sistema inicia com um menu interativo e funciona em *loop*, permitindo a navegação entre as opções. |
| **003** | Funcionalidade: Cadastrar Paciente | **Concluído** | Implementação da função que armazena Nome, Idade, Telefone e **CPF** (inclusão para requisitos futuros)  utilizando estruturas de dados (listas e dicionários). |
| **004** | Funcionalidade: Listar Todos os Pacientes | **Concluído** | A secretária pode visualizar todos os pacientes cadastrados de forma organizada. |

### 3. Impedimentos e Desafios Encontrados

* **Desafio:** Inicialmente, houve uma dúvida sobre a melhor estrutura de dados para armazenar múltiplos pacientes de forma eficiente e acessível. (Solução: Optou-se por uma **Lista de Dicionários** para simular um registro mais complexo).
* **Decisão de Escopo:** O campo **CPF** foi adicionado ao cadastro (Cartão 003) para prever as necessidades de identificação de pacientes citadas nos Passos futuros do projeto.

### 4. Retrospectiva da Sprint (O que aprender/melhorar)

| O que deu Certo? | O que pode ser Melhorado? | Ação para a Próxima Sprint |
| :--- | :--- | :--- |
| **Clareza do Backlog:** O detalhamento dos cartões com Histórias de Usuário facilitou a codificação. | **Tempo Estimado:** A estimativa para o Cartão 003 (Cadastro) foi subestimada devido à inclusão do tratamento inicial de *input* (ainda que não completo). | **Melhorar Estimativa:** Alocar tempo extra para tarefas que envolvam validação e tratamento de entrada de dados (Passo 2, requisito técnico). |
| **Foco:** A limitação do escopo permitiu que as tarefas essenciais fossem entregues com qualidade. | **Próximo Passo:** É vital **priorizar a funcionalidade de Estatísticas** (Passo 2) para atender à solicitação de relatórios da Sra. Helena. |

### 5. Planejamento para a Próxima Sprint (Sprint 2)

A próxima Sprint se concentrará em completar os requisitos do Passo 2 do projeto, que envolvem a lógica de manipulação de dados.

* **Objetivo da Sprint 2:** Entregar as funcionalidades de **Estatísticas** e **Busca de Paciente** no sistema Python, além de iniciar o trabalho de modelagem do projeto.
* **Principais Itens do Backlog para a Sprint 2:**
    * Desenvolver a funcionalidade de Cálculo de Estatísticas (Idade média, Paciente mais novo e mais velho, Total).
    * Desenvolver a funcionalidade para Buscar um Paciente pelo Nome.
    * Implementar o tratamento de erros de entrada (requerido tecnicamente).

---

**Conclusão:** A Sprint 1 foi um sucesso na construção da base do sistema. O sistema agora pode cadastrar e listar pacientes, o que permite o início da fase de manipulação de dados na Sprint 2.