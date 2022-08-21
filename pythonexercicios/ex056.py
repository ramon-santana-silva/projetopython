#56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.



cont=0
soma=0
for people in range(0,4):
    nome=str(input('informe seu nome: \n'))
    idade=int(input('informesua idade: \n'))
    sexo=str(input('informe seu sexo:\n(m) masculino\n(f)feminino\n'))
    if   idade<20 and sexo=='f':
        cont+=1
        #print('quantidade de mulheres com menos de 20 anos é igual a:{}'.format(cont))
    if sexo=='m':
        masculino=nome,idade
        print(masculino)
print('quantidade de mulheres com menos de 20 anos é igual a:{}'.format(cont))


