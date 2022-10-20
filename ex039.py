#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo 
# do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
anoatual= str(datetime.date.today() ) #datetime.date.today().year
anonascimento=int(input('Digite seu ano de nascimento:\n'))
idade=int(anoatual[0:4])-anonascimento
anominimo=int(anoatual[0:4])-18
anosretorno=anonascimento-anominimo  
if idade==18:
    print('idade {} esta apto ao alistamento militar'.format(idade))
elif idade<18:
    print('idade {} esta inapto ao alistamento militar, retorne daqui a {} anos'.format(idade,anosretorno))
else:
    print('idade {} esta acima do prazo de alistamento militar'.format(idade))
print("o ano atual é: {}".format(anoatual[0:4]))