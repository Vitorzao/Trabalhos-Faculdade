#Entrada
peso1 = 1
peso2 = 2
peso3 = 3

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

#Cálculo média ponderada
mediaPond = (n1*peso1 + n2*peso2 + n3*peso3)/(peso1+peso2+peso3)

#Saída
print(mediaPond)
