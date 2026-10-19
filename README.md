# Gestão Agro 🚜🐄

O **Gestão Agro** é um sistema especializado no gerenciamento de propriedades focadas em **pecuária leiteira** (*Dairy Management Software*). Desenvolvido em Python, o projeto utiliza Programação Orientada a Objetos (POO), arquitetura em camadas e testes automatizados determinísticos para garantir uma base de código sólida e escalável.

Este projeto está sendo construído como um ambiente prático para a aplicação de conceitos de engenharia de software backend, evolução de banco de dados e design de APIs.

---

## 📌 Escopo do MVP (Produto Mínimo Viável)

O escopo inicial está concentrado em 4 classes fundamentais que cobrem o ciclo essencial da atividade leiteira:

* **Animal (Entidade Central):** Controla o cadastro individual do rebanho (ID, Espécie, Data de Nascimento e Peso).
* **MilkProductionRecord:** Gerencia o registro diário da produção de leite por animal para análises futuras de médias e curvas de lactação.
* **FeedingRecord:** Controla a alimentação fornecida aos animais, servindo de base para cálculos de eficiência alimentar.
* **VaccineApplicationRecord:** Histórico de aplicações de vacinas e medicamentos, essencial para o controle sanitário e cálculo de período de carência.

---

## 🏗️ Arquitetura do Sistema

O projeto adota uma arquitetura em camadas para separar responsabilidades:

* **Models (Entidades):** classes Python que representam os registros do domínio e validam dados de acordo com as regras definidas.
* **Repositories:** classes responsáveis pela persistência e recuperação dos dados no SQLite, isolando as operações de banco de dados.
* **Services:** camada responsável pelas regras de negócio e pela coordenação das operações entre os Models e os Repositories.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.x
* **Banco de Dados:** SQLite (utilizando o módulo nativo `sqlite3`). As datas são tratadas em formato ISO (`YYYY-MM-DD`) para contornar a ausência de tipo nativo no SQLite.
* **Framework de Testes:** Pytest
* **Controle de Tempo em Testes:** `freezegun` (garante testes determinísticos congelando o relógio do sistema para cálculos de idade e carências).
* **Controle de Versão:** Git e GitHub

---

## 🧪 Estratégia de Testes

A confiabilidade do backend é assegurada por testes automatizados em duas frentes:
1. **Testes de Unidade (Models):** Garantem que as regras de criação de entidades e validações funcionem isoladamente.
2. **Testes de Integração (Repositories):** Utilizam o recurso de banco de dados em memória (`:memory:`) do SQLite, garantindo execuções instantâneas sem poluir o ambiente de desenvolvimento.

---

---

## 🚀 Como executar o projeto

### Pré-requisitos

- Python 3.x
- Git

### 1. Clonar o repositório

```bash
git clone https://github.com/mimaxavier/gestao_agro.git
cd gestao_agro
```

### 2. Criar e ativar o ambiente virtual

No macOS ou Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Executar os testes automatizados

```bash
python -m pytest -v
```