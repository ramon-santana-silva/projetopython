#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando 
# um laço for.
numero=int(input('Digite um númeropara escolher uma tabuada: \n'))

for num in range(0,11):
    multiplicacao=num*numero
    print('{} x {} = {}'.format(num,numero,multiplicacao)) 
       