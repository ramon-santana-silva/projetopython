"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""
numberlist=[]
for i in range(0,5):
    n=int(input('Informe valor inteiro: '))
    numberlist.append(n)
print(f'lista de número digitados foi:{numberlist}')
#for c,v in enumerate(numberlist):
