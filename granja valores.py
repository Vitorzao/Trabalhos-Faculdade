# Entrada de dados

qnt_frangos = int(input('Digite a quantidade de frangos: '))

# Custos

custo_chip = 8.00
custo_alimento = 5.30

# Processamento

custo_frango = custo_chip + (2 * custo_alimento)
custo_total = qnt_frangos + custo_frango

# Saída de dados

print('Custo por frango: ', custo_frango)
print('Gasto total da granja: ', custo_total)