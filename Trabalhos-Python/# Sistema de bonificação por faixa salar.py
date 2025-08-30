# Sistema de bonificação por faixa salarial

print('=== SISTEMA DE BONIFICAÇÃO POR FAIXA SALARIAL ===')
print()

funcionarios = []

# Coleta de dados dos 3 funcionarios
for i in range (1, 4):
    print(f'---- FUNCIONÁRIO {i} ----')

    nome = input('Digite o nome do funcionário: ')
    salario = float(input(f'Digite o salário de {nome}: R$ '))

    # Calculo da bonificação
    if salario <= 500.00:
        percentual_bonificacao = 5
        bonificacao = salario * 0.05
    elif salario <= 1200.00:
        percentual_bonificacao = 12
        bonificacao = salario * 0.12
    else:
        percentual_bonificacao = 0
        bonificacao = 0.0

    # Caculo novo salario
    novo_salario = salario + bonificacao

    # Armazenar dados do funcionário
    funcionario_info = {
        'nome': nome,
        'salario_original': salario,
        'percentual_bonificacao': percentual_bonificacao,
        'bonificacao': bonificacao,
        'novo_salario': novo_salario
    }
    funcionarios.append(funcionario_info)
    
    print(f"Salário original: R$ {salario:.2f}")
    print(f"Bonificação ({percentual_bonificacao}%): R$ {bonificacao:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
    print()