#Desenvolva um programa que leia o comprimento de três retas e
#  diga ao usuário se elas podem ou não formar um triângulo.
reta01=int(input('digite um valor para reta a:\n'))
reta02=int(input('digite um valor para reta b:\n'))
reta03=int(input('digite um valor para reta c:\n'))
if (reta01+reta02)>=reta03 and (reta01+reta03)>=reta02 and (reta02+reta03)>=reta01:
    print('as reta a:{},b:{} e c:{} formam um triangulo'.format(reta01,reta02,reta03))
else:
    print('as reta a:{},b:{} e c:{} formam não um triangulo'.format(reta01,reta02,reta03))