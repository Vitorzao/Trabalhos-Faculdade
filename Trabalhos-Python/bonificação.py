
print('==== SISTEMA DE BONIFICAÇÃO ====')
print()

# Entrada de dados

nome_func = input('Digite seu nome: ')
salario_func = float(input('Digite o seu salário: '))
idade_func = int(input('Digite sua idade: '))

# Processamento

if salario_func >= 1200.00 and idade_func >= 18:
    bonificacao = 500.00
    salario_final = salario_func + bonificacao

    print(f'Funcionário: {nome_func}')
    print(f'Salário atual: R$ {salario_func}')
    print(f'Bonificação: R$ {bonificacao}')
    print(f'Salário com bonificação: R$ {salario_final}')
else:
    print(f'Funcionário: {nome_func}')
    print(f'Não há bonificação')