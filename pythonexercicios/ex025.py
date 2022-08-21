# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
cpunumber= random.randrange(5)
humanumber=int(input('digite um número entre 0 e 5'))
if cpunumber==humanumber:
    print('Você venceu!!!')
else:
    print('Você perdeu')

print('o número escolhido pelo computador foi: {}'.format(cpunumber))
