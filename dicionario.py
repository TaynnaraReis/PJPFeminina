aluna = {"id":1, "nome":"taynnara", "nota": 9.2 }
pessoa = {"nome": "Ana", "idade": 25}
print("Nome da pessoa:", pessoa["nome"])

pessoa["cidade"] = "Florianópolis"
pessoa["idade"] = 26
print("Pessoa atualizada:", pessoa)

removido = pessoa.pop("idade")
print("Valor removido (idade):", removido)
print("Após pop('idade'):", pessoa)

print("Quantidade de chaves em 'aluna':", len(aluna))