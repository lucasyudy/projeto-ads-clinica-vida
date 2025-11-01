# **PROJETO INTEGRADO – ANÁLISE E DESENVOLVIMENTO DE SISTEMAS**

## [Nome da Instituição]

### [Seu Nome Completo]
### [Seu RA]

**[LOCAL PARA INSERIR: CAPA E FOLHA DE ROSTO PADRÃO DA INSTITUIÇÃO]**

* *Lembre-se: O trabalho final deve ser formatado em Word e conter capa e folha de rosto padrão da Instituição, seguindo as normas ABNT e as orientações visuais da disciplina.*

---

## 1. INTRODUÇÃO

Este documento apresenta o Projeto Integrado de Análise e Desenvolvimento de Sistemas, com foco na criação de um **Sistema de Gestão para a Clínica Vida+**, localizada na cidade de São Lucas. O projeto visa solucionar os desafios enfrentados pela clínica, como agendamentos manuais, dificuldades no acompanhamento do histórico dos pacientes e erros nos processos de cobrança e relatórios administrativos.

A proposta envolve a aplicação de diversas metodologias e conhecimentos adquiridos nas disciplinas do semestre. Para a gestão do projeto, foi utilizada a metodologia ágil Scrum, com o apoio da ferramenta Trello. O desenvolvimento da lógica de negócio e manipulação de dados foi realizado em Python. Além disso, foram aplicados conceitos de Lógica e Álgebra Booleana para o controle de acesso, Estruturas de Dados (Filas) para gerenciamento de atendimento, e Modelagem UML (Diagrama de Casos de Uso) para a arquitetura de funcionalidades do sistema.

O objetivo principal deste projeto é demonstrar a capacidade de integrar diferentes conhecimentos para conceber, planejar e propor soluções tecnológicas eficientes para problemas reais de negócio.

## 2. DESENVOLVIMENTO

### 2.1. PASSO 1: GESTÃO DE PROJETOS COM SCRUM

O Passo 1 utilizou a metodologia ágil Scrum para gerenciar as tarefas do projeto, utilizando o quadro "Desenvolvimento de uma Plataforma de Saúde - Lucas Yudy" no Trello. A aplicação do Scrum permitiu uma abordagem iterativa e incremental, facilitando a organização das atividades e o acompanhamento do progresso.

#### 2.1.1. Organização Inicial do Quadro Scrum

O quadro foi estruturado com as listas **Backlog**, **Sprint Atual**, **Em Progresso** e **Concluído**, refletindo o fluxo de trabalho ágil.

**[LOCAL PARA INSERIR PRINT 1: Visão Geral do Quadro Trello, mostrando as listas e a organização do Backlog/Sprints iniciais.]**

#### 2.1.2. Relatório e Revisão da Sprint 1 (Base do Sistema)

| Detalhe | Informação |
| :--- | :--- |
| **Sprint** | 1 (Infraestrutura e Cadastro Básico) |
| **Duração** | [Definir Data de Início] a [Definir Data de Fim] |
| **Objetivo** | Implementar a estrutura de navegação e as funcionalidades essenciais de Cadastro e Listagem de Pacientes no sistema Python. |

**Entregas Concluídas:** O core do sistema Python foi estabelecido, incluindo Menu em *Loop*, Funcionalidade de Cadastro (com **CPF** adicionado para futuros requisitos) e Listagem de Pacientes.

**[LOCAL PARA INSERIR PRINT 2: Quadro Trello com os Cartões da SPRINT 1 (001, 002, 003, 004) na lista "CONCLUÍDO"]**

#### 2.1.3. Relatório e Revisão da Sprint 2 (Passo 2 e Início do Passo 3)

| Detalhe | Informação |
| :--- | :--- |
| **Sprint** | 2 (Estatísticas, Busca e Lógica Booleana) |
| **Duração** | [Definir Data de Início] a [Definir Data de Fim] |
| **Objetivo** | Entregar as funcionalidades de **Estatísticas e Busca** (completando o Passo 2 do projeto) e iniciar a **Modelagem da Lógica Booleana** (Passo 3). |

**Entregas Concluídas:**

* Funcionalidade: Calcular e Exibir Estatísticas (Número total, idade média, paciente mais novo e mais velho).
* Funcionalidade: Buscar Paciente por Nome (Busca parcial e *case-insensitive*).
* Implementação do Tratamento de Erros de Entrada (validação de idade numérica e *inputs* vazios).
* Modelagem da Lógica Booleana (Expressões Lógicas e Tabelas Verdade).

**[LOCAL PARA INSERIR PRINT 3: Quadro Trello com os Cartões da SPRINT 2 (005, 006, 007, 008) na lista "CONCLUÍDO"]**

#### 2.1.4. Relatório e Revisão da Sprint 3 (Passos 4 e 5)

| Detalhe | Informação |
| :--- | :--- |
| **Sprint** | 3 (Modelagem de Fila e Casos de Uso) |
| **Duração** | [Definir Data de Início] a [Definir Data de Fim] |
| **Objetivo** | Finalizar a etapa de Modelagem e Algoritmos do projeto, criando o **Pseudocódigo para o controle de Fila (Passo 4)** e o **Diagrama de Casos de Uso (Passo 5)**. |

**Entregas Concluídas:**

* Elaboração do Algoritmo em Pseudocódigo para a Fila de Atendimento (Passo 4).
* Elaboração do Diagrama de Casos de Uso para o Sistema de Gestão de Consultas (Passo 5).

**[LOCAL PARA INSERIR PRINT 4: Quadro Trello com os Cartões da SPRINT 3 (009, 010) na lista "CONCLUÍDO"]**

### 2.2. PASSO 2: DESENVOLVIMENTO DE SOFTWARE I - PYTHON

A seguir, é apresentado o código Python do Sistema de Gestão da Clínica Vida+, que engloba todas as funcionalidades desenvolvidas nas Sprints 1 e 2.

**[LOCAL PARA INSERIR O CÓDIGO PYTHON COMPLETO (das Sprints 1 e 2)]**

**Explicação das Funcionalidades Implementadas:**

* **Menu Principal:** Interface de linha de comando para navegação nas opções do sistema, funcionando em *loop* até o usuário decidir sair.
* **Cadastrar Paciente:** Permite inserir Nome, Idade, CPF e Telefone do paciente. Inclui validação para garantir que a idade seja numérica e positiva, e que o nome não seja vazio.
* **Listar Todos os Pacientes:** Exibe todos os pacientes cadastrados em formato de tabela, incluindo Nome, Idade, CPF e Telefone.
* **Ver Estatísticas:** Calcula e apresenta o número total de pacientes, a idade média, e identifica o paciente mais novo e mais velho na base de dados.
* **Buscar Paciente:** Permite localizar pacientes através de uma busca parcial e *case-insensitive* pelo nome, exibindo todos os dados dos pacientes encontrados.

### 2.3. PASSO 3: LÓGICA E ÁLGEBRA BOOLEANA

O sistema de controle de acesso para atendimento da Clínica Vida+ foi analisado com base em quatro variáveis lógicas: $A$ (Agendamento), $B$ (Documentos OK), $C$ (Médico disponível) e $D$ (Pagamentos em dia).

#### 2.3.1. Expressões Lógicas

**1. Consulta Normal:** O paciente é atendido se (Tem agendamento E documentos OK E médico disponível) OU (Documentos OK E médico disponível E pagamentos em dia).
$$\text{Consulta Normal} = (A \land B \land C) \lor (B \land C \land D)$$

**2. Emergência:** O paciente é atendido se (Há médico disponível) E (Tem documentos OU pagamentos em dia).
$$\text{Emergência} = C \land (B \lor D)$$

#### 2.3.2. Tabelas Verdade Completas

A tabela verdade abaixo demonstra todas as 16 combinações possíveis das variáveis de entrada e os resultados correspondentes para a **Consulta Normal ($R_N$)** e **Emergência ($R_E$)**.

**[LOCAL PARA INSERIR A TABELA VERDADE COMPLETA (as 16 linhas com os resultados finais $R_N$ e $R_E$)]**

#### 2.3.3. Análise de Situações e Situação Prática

**1. Análise de Situações de Atendimento:**
* **Consulta Normal ($R_N$):** O paciente pode ser atendido em **3 situações** distintas, onde a expressão resulta em Verdadeiro.
* **Emergência ($R_E$):** O paciente pode ser atendido em **5 situações** distintas, onde a expressão resulta em Verdadeiro.

**2. Situação Prática:** Um paciente chega com as seguintes condições: Sem agendamento ($A=F$), Documentos OK ($B=V$), Médico disponível ($C=V$), Pagamentos atrasados ($D=F$).
* **Consulta Normal:** $R_N = (F \land V \land V) \lor (V \land V \land F) = F \lor F = F$
* **Emergência:** $R_E = V \land (V \lor F) = V \land V = V$

**Conclusão:** Nas condições apresentadas, o paciente **será atendido** em caso de **Emergência**, mas **não será atendido** para Consulta Normal.

### 2.4. PASSO 4: ESTRUTURA DE DADOS (FILA)

Este passo aborda a modelagem de um sistema de fila para gerenciar a ordem de atendimento dos pacientes, utilizando o princípio FIFO (Primeiro que Chega, Primeiro a ser Atendido).

#### 2.4.1. Algoritmo em Pseudocódigo

O pseudocódigo abaixo simula as operações de inserção, remoção e visualização de pacientes em uma fila.

**[LOCAL PARA INSERIR O PSEUDOCÓDIGO COMPLETO DO PASSO 4]**

* **Descrição das Operações:**
    * **ADICIONAR NA Fila\_Pacientes:** Equivalente à operação **Enqueue**, adiciona um paciente ao final da fila.
    * **REMOVER\_PRIMEIRO(Fila\_Pacientes):** Equivalente à operação **Dequeue**, remove o paciente do início da fila para atendimento.

### 2.5. PASSO 5: MODELAGEM (DIAGRAMA DE CASOS DE USO)

Este passo finaliza a modelagem do sistema através de um Diagrama de Casos de Uso, que ilustra as funcionalidades principais do Sistema de Gestão de Consultas e suas interações com os atores.

#### 2.5.1. Diagrama de Casos de Uso

**[LOCAL PARA INSERIR A IMAGEM DO DIAGRAMA DE CASOS DE USO]**

**Descrição do Diagrama:**

* **Boundary "Sistema de Gestão de Consultas":** Delimita as funcionalidades do sistema.
* **Atores:** `Secretária`, `Médico` (principais) e `Sistema de Impressão` (secundário/externo).
* **Casos de Uso:** `Cadastrar Paciente`, `Agendar Consulta`, `Confirmar Consulta`, `Cancelar Consulta`, `Gerar Receita`, `Imprimir Receita`.
* **Relacionamentos:**
    * **Associações:** Atores interagem com seus respectivos casos de uso (e.g., Secretária com Agendar Consulta, Médico com Gerar Receita).
    * **Inclusões ($<<\text{include}>>$):** Indicam dependências obrigatórias (e.g., Agendar Consulta inclui Cadastrar Paciente; Gerar Receita inclui Imprimir Receita).
    * **Associação Externa:** O caso de uso `Imprimir Receita` se associa ao `Sistema de Impressão`.

## 3. CONCLUSÃO

O Projeto Integrado de Análise e Desenvolvimento de Sistemas para a Clínica Vida+ demonstrou a aplicação prática de diversas competências essenciais na área. Através da metodologia ágil Scrum, foi possível gerenciar de forma eficaz as diferentes etapas, desde a configuração inicial do ambiente até a modelagem avançada de processos.

O sistema em Python, desenvolvido nas Sprints 1 e 2, atendeu aos requisitos de cadastro, listagem, busca e análise estatística de pacientes, estabelecendo uma base funcional para a gestão da clínica. A exploração da Lógica e Álgebra Booleana no Passo 3 permitiu validar o controle de acesso, enquanto o pseudocódigo (Passo 4) e o Diagrama de Casos de Uso (Passo 5) proporcionaram uma visão clara da arquitetura e do fluxo de trabalho do sistema.

Este projeto reforça a importância da integração de conhecimentos técnicos e de gestão para a concepção de soluções que não apenas resolvam problemas imediatos, mas que também ofereçam uma base sólida para futuras expansões e aprimoramentos. A experiência adquirida em cada etapa do projeto contribuirá significativamente para o desenvolvimento profissional em Análise e Desenvolvimento de Sistemas.
