frutas = ['cupuaçu', 'açai', 'tapereba', 'graviola']
numeros = [1, 2, 3, 4]
print('Primeira fruta:', frutas[0])
print('Última fruta:', frutas [-1])

frutas[1] = 'bacaba'
print('Após alterar:', frutas)

frutas.append('açai')
frutas.insert(1, 'jaca')
print('Após adicionar:', frutas)

frutas.remove('graviola')
print("Após remover 'graviola':", frutas)

ultima = frutas.pop()
print('Última removida:', ultima)

print("Tamanho da lista 'frutas':", len(frutas))
print('Fatiamento [1:4]:', frutas[1:4])
print("Tem 'jaca'?", "jaca" in frutas)