"""Crie um programa que vai ler vários números e colocar em uma lista.
   Depois disso, mostre:
   A) Quantos números foram digitados.
   B) A lista de valores, ordenada de forma decrescente.
   C) Se o valor 5 foi digitado e está ou não na lista."""
listnumber=[]
while True:
    """number= int(input('informe valor inteiro: '))
    listnumber.append(number)"""
    listnumber.append(int(input('Informe valor inteiro: ')))
    r=str(input('deseja continuar: [S/N] ')).strip()
    if r in'Nn':
        break
    
listnumber.sort(reverse=True)
print(f'A quantidade de números digitados na lista foi:{len(listnumber)}')
print(f'A lista de números é igual a :{listnumber}')
if 5 in listnumber:
    print('o valor 5 foi adicionado')
else:
    print('Valor 5 não foi adicionado')
