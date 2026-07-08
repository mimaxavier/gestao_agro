# Next

## ✅ Passo finalizado

- Finalizado o `FeedingRecordRepository`.
- Implementados os métodos:
  - [x] save()
  - [x] get_by_id()
  - [x] update()
- Todos os testes passando (`33 passed`).
- Refatorada a validação de datas do `FeedingRecord`.
- Definida a responsabilidade das conversões de data:
  - Model trabalha com objetos `date`.
  - Repository salva com `.isoformat()`.
  - Repository recupera usando `date.fromisoformat()`.

---

## ▶ Próximo passo

- Implementar o método `delete()` do `FeedingRecordRepository`.
- Criar os testes do `delete()`.
- Validar funcionamento diretamente no banco SQLite.
- Fazer commit da implementação.

---

## 📝 Observações

- O objeto precisa receber o `id` gerado após o `save()`.
- Não criar um novo objeto para fazer `update`; atualizar o objeto que possui o `id`.
- Em caso de `database is locked`, verificar conexões abertas e fechar o SQLite.