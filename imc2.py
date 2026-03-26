#Entrada de Dados
peso = float(input('Digite seu peso em kg (ex.: 68.5): '))
altura = float(input('Digite sua altura em metros (ex.: 1.65): '))

#Calculo do IMC
imc = peso / (altura ** 2)

#Classificação
if imc < 18.5:
    categoria = 'Magreza'

elif imc < 25:
    categoria = 'Normal'

elif imc < 30:
    categoria = 'Sobrepeso'

else:
    categoria = 'Obesidade'

#Saida formatada
print(f"imc = {imc: .2f} - {categoria}")
