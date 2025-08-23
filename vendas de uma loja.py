# Entrada de dados

qntd_paes = int(input('Digite a quantidade de pães vendidos hoje: '))
qntd_broas = int(input('Digite a quantidade de broas vendidas hoje: '))

# Preços

preco_pao = 1.10
preco_broa = 2.50

# Processamento

total_paes = qntd_paes*preco_pao
total_broas = qntd_broas*preco_broa
total_vendas = total_paes*total_broas
poupanca = total_vendas*0.10

# Saída de dados

print('O valor arrecadado dos pães: R$ ',total_paes )
print('O valor arrecadado de broas: R$ ',total_broas)
print('O valor arrecadado de vendas no dia: R$ ',total_vendas)
print('O valor a ser guardado na poupança: R$ ', poupanca)