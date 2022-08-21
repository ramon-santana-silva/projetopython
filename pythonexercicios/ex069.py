""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""
contIdade=contIdadeFem=contMas=0
while True:
    idade=int(input('Informe sua idade \n'))
    sexo=str(input('informe sexo se Masculino digite M ou F para Feminino \n')).strip().upper()
    encerrar=str(input('Digite S para sair\n')).strip().upper()[0]
    if idade >18:
            contIdade+=1
    if sexo=='M':
        contMas+=1
    elif sexo=='F' and idade<20:
        contIdadeFem+=1        
    if encerrar=='S':
        break
print(f'total de pessoas com mais de 18 anos são: {contIdade},\n total de homens cadastrados{contMas} e\n total de mulheres com menos de 20 anos{contIdadeFem}')
        
    
