#Escreva um programa para aprovar o empréstimo bancário para a
#  compra de uma casa. Pergunte o valor da casa, o salário do comprador
#  e em quantos anos ele vai pagar. A prestação mensal não pode exceder
#  30% do salário ou então o empréstimo será negado.

valordacasa=int(input('Informe o valor da casa:\n'))
salario=int(input('Informe seu salário: \n'))
anos=int(input('Informe em quantos anos pagará: \n'))
prestacao=anos*12
prestacaomensal= valordacasa/prestacao
if prestacaomensal<=(0.30*salario):
    print('emprestimo autorizado, o valor da sua prestação é: {}'.format(prestacaomensal))
else:
    print('emprestimo negado, o valor da sua prestação mensal de {} não é suficiente'.format(prestacaomensal))

