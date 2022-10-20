#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

fullname=str(input('Digite nome completo: ')).strip()
print('nome com todas as letras maiúsculas: ', fullname.upper())
print('nome com todas as letras minúsculas: ', fullname.lower())
print('total de letras do nome completo é:',len(fullname)-fullname.count(' '))
firstname=fullname.split()
print('o primeiro nome é ', firstname[0],'e a quantidade de letras é igual a ',len(firstname[0]))
