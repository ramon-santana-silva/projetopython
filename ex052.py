#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont=0
numero=int(input('Digite um númro inteiro \n'))
for num in range(0,numero+1):
   cont+=1

if numero%num==0 :
     print('foram analisados: {}, o número digitado{} é primo'.format(cont,numero))
else:
    print('foram analisados: {}, número {} não é primo'.format(cont,numero))