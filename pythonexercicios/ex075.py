"""Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""
cont=0

number= (int(input('Informe um número: \n')),
        int(input('Informe um número: \n')),
        int(input('Informe um número: \n')),
        int(input('Informe um número: \n')))
contador=number.count(9)
print(f'você digitou os números : {number} ')
if 3 in number:
    posicao=number.index(3)+1
    print(f'A primeira posição do número 3 é:{posicao}')
else:
    print('O número 3 não foi digitado')
for num in number:
    if num%2==0:
        print(f'os números pares: {num}')
print(f'A quantidade de 9 informados foram: {contador}')
