#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²
largura=float(input('Digite a largura da parede: '))
altura=float(input('Digite a altura da parede '))
area= largura*altura
tinta=area/2
print('será necessario {} litros de tinta para pintar uma area de {} m² '.format(tinta,area))
