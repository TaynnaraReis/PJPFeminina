while True:
    #if com continue e break
    numero = int(input('Digite um número (0 para sair): '))
    if numero == 0:
        print('Encerrando o programa')
        break
    if numero == 99:
        print('Número 99 encontrado! Continuando para o próximo: ')
        continue
    print(f'Você digitou: {numero}')