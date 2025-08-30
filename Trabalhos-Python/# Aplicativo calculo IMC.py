# Aplicativo calculo IMC

print('==== APLICATIVO CALCULO IMC ====')
print()

# Entrada de dados

nome = input('Digite o nome do paciente: ')
peso = float(input('Digite o peso do paciente: '))
altura = float(input('Digite a altura do paciente: '))

# Calculo IMC

imc = peso / (altura*altura)

# Processamento

if imc <= 18.4:
    categoria = 'Abaixo do peso'
elif imc <= 24.9:
    categoria = 'Peso nomrmal'
elif imc <= 29.9:
    categoria = 'Sobrepeso'
elif imc <= 34.9:
    categoria = 'Obesidade grau I'
elif imc <= 39.9:
    categoria = 'Obesidade grau II'
else:
    categoria = 'Obesidade grau III'

# Exibição de resultados 

print()
print('=== RESULTADO ===')
print()
print('Nome do paciente::', nome)
print('Peso do paciente:', peso,'kg')
print('Altura do paciente:', altura,'m')
print('IMC do paciente:', imc)
print('Categoria: ', categoria)