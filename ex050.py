#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.
soma=0
cont=0
for l in range(0,6):
    numero=int(input('Digite um número inteiro e se ele for par sera somado \n'))
    cont+=1
    if numero%2==0:
        soma+= numero 
print('foram lidos {}, A soma dos pares é igual a: {}'.format(cont,soma))    
