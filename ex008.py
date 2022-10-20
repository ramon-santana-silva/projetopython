#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
metros=float(input('digite uma distancia em metros: '))
cm= float(metros*100)
mm=float(metros*1000)
print('A distância de {} metros em cm é {} e em milimetros é {} '.format(metros,cm,mm))