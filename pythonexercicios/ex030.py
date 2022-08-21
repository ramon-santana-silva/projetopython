#Crie um programa que leia um número inteiro e mostre na tela se ele é
#  PAR ou ÍMPAR.
numero=int(input('digite um número:'))
if numero%2==0:
    print('número é par')
else:
    print('número é impar')    
print('modulo do número é: {} '.format(numero%2))
