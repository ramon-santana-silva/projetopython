"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
 o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma 
 entre elas (desconsiderando o flag)."""
cont=soma=0

number=False

while True:
    number=int(input('Digite um número inteiro\n'))
    if number==999:
        break
    cont+=1
    soma+=number
    
    
   
print(f'A quantidade de numeros digitados foi:{cont} e a soma de todos os numeros digitados foi: {soma}')