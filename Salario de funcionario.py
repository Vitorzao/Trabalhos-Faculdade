# Entrada de dados

horario_normal = float(input('Digite quantas horas foram trabalhadas: '))
horario_extra = float(input('Digite quantas horas extras foram trabalhadas: '))


# Valores horarios

valor_normal = 10.00
valor_extra = 22.00

# Processamento

salario_bruto = (horario_normal*valor_normal) + (horario_extra*valor_extra)
desconto = salario_bruto*0.18
salario_liquido = salario_bruto - desconto

# Saída de dados

print('Salario Bruto: R$', salario_bruto)
print('Desconto: R$', desconto)
print('Salario Líquido: R$', salario_liquido)