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

O projeto adota uma divisão limpa em camadas para isolar responsabilidades:

* **Models (Entidades):** Classes puras Python que encapsulam os dados e validações estruturais primárias.
* **Repositories:** Abstração da persistência de dados utilizando o padrão *Repository* orientado a interfaces (classes abstratas com o módulo `abc`), garantindo independência da tecnologia de banco de dados.
* **Services:** Camada onde residirão as regras de negócio complexas (cálculo de Dias em Lactação - DEL, médias de produção e alertas de carência sanitária).

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

