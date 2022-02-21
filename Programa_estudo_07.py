#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#  e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#  sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Exemplo 01')
qkms = float(input(' Total de kilometros percorridos: '))
qdias = int(input('Total de dias: '))
km = 0.15
dia = 60.00
total = (qkms * km) + (qdias * dia)
print('Valor a pagar: R$ {:.2f}'.format(total))

print('Exemplo 02')
kms = float(input('Total de kilometros percorridos: '))
dias = int(input('Total de dias: '))
print('''Quantidade de dias {} valor : R$ {:.2f}.
quantidade de km rodados {} valor : R$ {:.2f}.
valor total a ser pago: R$ {:.2f}.'''.format(dias, dias * 60.00, kms, kms * 0.15, (dias * 60) + (kms * 0.15)))

print('Exemplo 03 ')
km = float(input('Quantos km rodados? '))
dias = int(input(' Quantos dias alugados? '))
pago = (dias * 60.00) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
