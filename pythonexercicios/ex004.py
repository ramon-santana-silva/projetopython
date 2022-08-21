#Faça um programa que leia algo pelo teclado e mostre a tela o seu tipo primitivo e todas as informações sobre ele
from ssl import OP_NO_RENEGOTIATION


a=input('digite número ou letra ou os dois: ')
print('A informação digitada é do tipo: ',type(a))
print('informação é alfabetico: ', a.isalpha())
print('A informação tem espaços: ', a.isspace())
print('A informação é um número: ', a.isnumeric())    
print('A informação esta em alphanumerico', a.isalpha)