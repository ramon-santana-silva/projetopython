#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
numero01=int(input('Digete um numero: \n'))
numero02=int(input('Digite um segundo numero: \n'))

if numero01>numero02:
    print('O {} primeiro número digitado é maior'.format(numero01))
elif numero02>numero01:
    print('O {} segundo numero digitado é maior'.format(numero02))
else:
    print('não existe valor maior, pois os dois são iguais')        