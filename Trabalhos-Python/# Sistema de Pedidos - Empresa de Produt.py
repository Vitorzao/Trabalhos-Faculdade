# Sistema de Pedidos - Empresa de Produtos Alimentícios

print('==== SISTEMA DE PEDIDOS - PRODUTOS ALIMENTÍCIOS ====')
print()

# Variável para armazenar o preço total de todos os pedidos

preco_total_geral = 0.0

# Lista para armazenar informações dos pedidos 

pedidos = []

# Processamento dos pedidos

for numero_pedido in range (1, 6):
    print(f'--- PEDIDO {numero_pedido} ---')

    # Entrada de dados para cada pedido
    numero_produto = int(input(f'Digite o número do produto (pedido {numero_pedido}): '))
    quantidade = int(input(f'Digite a quantidade do produto (pedido {numero_pedido}): '))
    preco_unitario = float(input(f'Digite o preço unitário R$ (pedido {numero_pedido}): '))

    # Cálculo do preço total do pedido atual
    preco_total_pedido = quantidade * preco_unitario

    # Adição ao preço total geral
    preco_total_geral += preco_total_pedido

    # Armazenar informações do pedido

    pedido_info = {
        'numero_pedido': numero_pedido,
        'numero_produto': numero_produto,
        'quantidade': quantidade,
        'preco_unitario': preco_unitario,
        'preco_total_pedido': preco_total_pedido
    }
    pedidos.append(pedido_info)
    
    print("Preço total do pedido", numero_pedido, ": R$", round(preco_total_pedido, 2))
    print()

# Exibição do resumo final
print("=== RESUMO DOS PEDIDOS ===")
print()

for pedido in pedidos:
    print("Pedido", pedido['numero_pedido'], ":")
    print("  Produto:", pedido['numero_produto'])
    print("  Quantidade:", pedido['quantidade'], "unidades")
    print("  Preço unitário: R$", round(pedido['preco_unitario'], 2))
    print("  Total do pedido: R$", round(pedido['preco_total_pedido'], 2))
    print()

print("=" * 40)
print("PREÇO TOTAL DE TODOS OS PRODUTOS: R$", round(preco_total_geral, 2))
print("=" * 40)