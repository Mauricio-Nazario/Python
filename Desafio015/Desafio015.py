dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe a quantidade de quilometros: '))

total = (dias * 60) + (km * 0.15)

print('O preço a pagar por {} dias é R$ {:.2f} por {} km rodados'.format(dias, total, km))