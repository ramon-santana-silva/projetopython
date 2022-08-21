"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
 usuário. O programa será interrompido quando o número solicitado for negativo."""
tabuada=0
cont=0
while True:
        tabuada=int(input('Informe um número inteiro positivo para a tabuada: \n'))
        if tabuada<0:
                break
        else:
                for i in range(1,11):
                    print(f'{tabuada} x {cont} = {tabuada*cont}')
                    cont+=1