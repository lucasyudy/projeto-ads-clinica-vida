# 🏥 Clínica Vida+ — Sistema de Gerenciamento de Pacientes

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-dependency%20manager-60A5FA?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![ADS](https://img.shields.io/badge/Projeto-ADS%20Anhanguera-orange?style=flat)

> Projeto Integrado desenvolvido para a disciplina de **Análise e Desenvolvimento de Sistemas** — Centro Universitário Anhanguera

---

## 📌 Sobre o Projeto

Sistema de gerenciamento de pacientes para uma clínica fictícia, desenvolvido em **Python 3.12** com boas práticas de programação. O projeto foi estruturado em **3 sprints** seguindo metodologia ágil, evoluindo desde o cadastro básico até funcionalidades avançadas de busca, estatísticas e tratamento de erros.

---

## ✨ Funcionalidades

- 📋 **Cadastrar paciente** — com validação de nome e idade
- 📊 **Ver estatísticas** — total de pacientes, média de idade, mais novo e mais velho
- 🔍 **Buscar paciente** — busca por nome parcial
- 📃 **Listar pacientes** — exibição completa do cadastro
- ⚠️ **Tratamento de erros** — validações robustas em todos os inputs

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|---|---|---|
| Python | 3.12 | Linguagem principal |
| Poetry | latest | Gerenciamento de dependências |

---

## 📁 Estrutura do Projeto

```
projeto-ads-clinica-vida/
├── src/
│   ├── __init__.py
│   └── app.py          # Lógica principal do sistema
├── tests/              # Testes automatizados
├── docs/               # Documentação do projeto
├── pyproject.toml      # Configuração Poetry
├── LICENSE
└── README.md
```

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/lucasyudy/projeto-ads-clinica-vida.git
cd projeto-ads-clinica-vida

# Instale as dependências
poetry install

# Execute o projeto
poetry run python src/app.py
```

---

## 📚 Contexto Acadêmico

Projeto desenvolvido em 3 sprints com metodologia ágil:

| Sprint | Descrição |
|---|---|
| Sprint 1 | Estrutura base e cadastro de pacientes |
| Sprint 2 | Manipulação e análise de dados (estatísticas e busca) |
| Sprint 3 | Refinamentos, tratamento de erros e entrega final |

**Instituição:** Centro Universitário Anhanguera — Tecnologia em ADS  
**Autor:** [Lucas Yudy Okuda](https://github.com/lucasyudy)  
**Licença:** MIT
