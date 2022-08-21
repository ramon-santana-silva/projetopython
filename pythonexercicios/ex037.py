#Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão: 1 para
#  binário, 2 para octal e 3 para hexadecimal.
numero=int(input('digite um número: '))
binario=bin(numero)
octal=oct(numero)
hexadecimal=hex(numero)
conversao=int(input('Digite 1 para coverter para binário \n Digite 2 para converter para Octal\n Digite 3 para converter para hexadecimal\n '))
if conversao == 1:
    print('o binário do número {} é: {}'.format(numero,binario))
elif conversao==2:
    print('o Octal do número {} é: {}'.format(numero,octal))
elif conversao==3:
    print('o Hexadecimal do número {} é: {}'.format(numero,hexadecimal))


