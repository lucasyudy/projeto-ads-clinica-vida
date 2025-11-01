# Relatório do Projeto de Sistemas de Informação (Versão 2.0)

## [Nome da Instituição]

### [Seu Nome Completo]

---

**[LOCAL PARA INSERIR: CAPA E FOLHA DE ROSTO PADRÃO DA INSTITUIÇÃO]**

* *Lembre-se de que o trabalho final deve ser em formato Word e seguir as normas da Instituição.*

---

## 1. INTRODUÇÃO (A SER PREENCHIDA AO FINAL DO PROJETO)

\[Espaço reservado para a Introdução.\]

## 2. DESENVOLVIMENTO

### 2.1. PASSO 1: GESTÃO DE PROJETOS COM SCRUM

O Passo 1 utilizou a metodologia ágil Scrum para gerenciar as tarefas do projeto, utilizando o quadro "Desenvolvimento de uma Plataforma de Saúde - Lucas Yudy" no Trello.

#### 2.1.1. Organização Inicial do Quadro Scrum

O quadro foi estruturado com as listas **Backlog**, **Sprint Atual**, **Em Progresso** e **Concluído**.

**[LOCAL PARA INSERIR PRINT 1: Visão Geral do Quadro Trello, mostrando as listas e a organização do Backlog/Sprints iniciais.]**

#### 2.1.2. Relatório e Revisão da Sprint 1 (Base do Sistema)

| Detalhe | Informação |
| :--- | :--- |
| **Sprint** | 1 (Infraestrutura e Cadastro Básico) |
| **Objetivo** | Implementar a estrutura de navegação e as funcionalidades essenciais de Cadastro e Listagem de Pacientes. |

**Entregas Concluídas:** O core do sistema Python foi estabelecido, incluindo Menu em *Loop*, Funcionalidade de Cadastro (com **CPF** adicionado) e Listagem de Pacientes.

**[LOCAL PARA INSERIR PRINT 2: Quadro Trello com os Cartões da SPRINT 1 (001, 002, 003, 004) na lista "CONCLUÍDO"]**

#### 2.1.3. Relatório e Revisão da Sprint 2 (Passo 2 e 3)

| Detalhe | Informação |
| :--- | :--- |
| **Sprint** | 2 (Estatísticas, Busca e Lógica Booleana) |
| **Objetivo** | Entregar as funcionalidades de **Estatísticas e Busca** (completando o Passo 2) e iniciar a **Modelagem da Lógica Booleana** (Passo 3). |

**Entregas Concluídas:**

* Funcionalidade: Calcular e Exibir Estatísticas (Total, Média, Mais Novo/Velho).
* Funcionalidade: Buscar Paciente por Nome (Busca parcial e *case-insensitive*).
* Implementação do Tratamento de Erros de Entrada (idade numérica, *inputs* vazios).
* Modelagem da Lógica Booleana (Expressões e Tabelas Verdade).

**[LOCAL PARA INSERIR PRINT 3: Quadro Trello com os Cartões da SPRINT 2 (005, 006, 007, 008) na lista "CONCLUÍDO"]**

### 2.2. PASSO 2: DESENVOLVIMENTO DE SOFTWARE I - PYTHON

A seguir, é apresentado o código Python do Sistema de Gestão da Clínica Vida+, que engloba as entregas das Sprints 1 e 2.

**[LOCAL PARA INSERIR O CÓDIGO PYTHON COMPLETO (Sprints 1 e 2)]**

**Explicação das Funcionalidades Implementadas:**

\[Descreva como as funções `cadastrar_paciente()`, `ver_estatisticas()`, `buscar_paciente()` e `listar_pacientes()` atendem aos requisitos do projeto.\]

### 2.3. PASSO 3: LÓGICA E ÁLGEBRA BOOLEANA

O sistema de controle de acesso para atendimento foi analisado com base nas variáveis $A$ (Agendamento), $B$ (Documentos OK), $C$ (Médico disponível) e $D$ (Pagamentos em dia).

#### 2.3.1. Expressões Lógicas

**1. Consulta Normal:**
$$\text{Consulta Normal} = (A \land B \land C) \lor (B \land C \land D)$$

**2. Emergência:**
$$\text{Emergência} = C \land (B \lor D)$$

#### 2.3.2. Tabelas Verdade Completas

A tabela verdade de 16 linhas demonstra todas as combinações de variáveis e os resultados de atendimento ($R_N$ para Consulta Normal e $R_E$ para Emergência).

**[LOCAL PARA INSERIR A TABELA VERDADE COMPLETA (as 16 linhas com os resultados finais $R_N$ e $R_E$)]**

#### 2.3.3. Análise de Situações e Situação Prática

**1. Análise de Situações de Atendimento:**
* **Consulta Normal ($R_N$):** O paciente pode ser atendido em **3 situações** distintas (linhas onde $R_N = V$).
* **Emergência ($R_E$):** O paciente pode ser atendido em **5 situações** distintas (linhas onde $R_E = V$).

**2. Situação Prática:** O paciente chega com as condições: $A=F$ (Sem agendamento), $B=V$ (Documentos OK), $C=V$ (Médico disponível), $D=F$ (Pagamentos atrasados).

* **Consulta Normal:** $R_N = (F \land V \land V) \lor (V \land V \land F) = F \lor F = F$
* **Emergência:** $R_E = V \land (V \lor F) = V \land V = V$

**Conclusão:** O paciente **será atendido** em caso de **Emergência**, mas **não será atendido** para Consulta Normal.

---

### 2.4. PASSO 4: ESTRUTURA DE DADOS (FILA)

\[Espaço reservado para o Pseudocódigo do Passo 4 (Sprint 3)\]

### 2.5. PASSO 5: MODELAGEM (DIAGRAMA DE CASOS DE USO)

\[Espaço reservado para o Diagrama do Passo 5 (Sprint 3)\]

## 3. CONCLUSÃO (A SER PREENCHIDA AO FINAL DO PROJETO)

\[...\]
