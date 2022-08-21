#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram 
# necessários para vencer.
import random
from time import sleep
cont=0
cpunumber=random.randint(1,10)
print('='*5 ,'Processando número pensado pelo computador','='*5)
sleep(1)
humanumber=int(input('Qual número estou pensando'))
while cpunumber!=humanumber:
    humanumber=int(input('Tente novamente até adivinhar o número que eu pensei'))
    cont+=1
print('Depois de {} tentativas, você descobriu que meu número foi:{}'.format(cont,cpunumber))