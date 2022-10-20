#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.



numero=str(input('digite um número entre 0 e 9999:\n'))
unidade=numero[0]
dezena=numero[1]
centena=numero[2]
milhar=numero[3]

print('{}\n {}\n {}\n {}\n'.format(unidade,dezena,centena,milhar))
