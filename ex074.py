"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
 mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""
from random import randint
cpunumber=randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
 
print(f'números escolhidos pelo computador: {cpunumber}')
print(max(cpunumber))
print(min(cpunumber))