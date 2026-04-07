def saudacao():
    print('Olá, aluno!')

saudacao()

def print_nara(roxo):
    print(f'Olá, {roxo}!')

print_nara('roxo')

def soma(a, b):
    print(a+b)

soma(3,5)

def soma(a, b, c):
    valor = a + b + c
    print(valor)

soma(5, 8, 10)

#usando lista quando for mais de 5 variaveis
def soma(lista_valores):
    soma_valores = 0
    for valor in lista_valores:
        soma_valores += valor
    print(soma_valores)

lista = [20, 74, 56, 89, 12]

soma(lista)


#exemplo funcao chamar valores de evento
def custo_evento(lista_valores):
    soma_valores = 0
    for valor in lista_valores:
        soma_valores += valor
    return soma_valores

#calcula o percentual do custo do evento
def valor_evento(custo):
    valor = 0
    if custo < 100:
        valor = custo * 0.5
    elif custo < 200:
        valor = custo * 0.7
    else:
        valor = custo * 0.9
    return valor