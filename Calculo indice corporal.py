nomecli = input('Digite seu nome: ')
pesocli = float(input('Digite seu peso: '))
alturacli = float(input('Digite sua altura: '))

IMC = pesocli/(alturacli*alturacli)

print('Nome do cliente:', nomecli)
print('Peso do cliente: ', pesocli)
print('Altura do cliente: ', alturacli)
print('IMC do cliente', IMC)