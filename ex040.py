#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
nota01=float(input('Digite a nota da primeira avaliação\n'))
nota02=float(input('Digite a nota da segunda avaliação\n'))
media=(nota01+nota02)/2
if media<5:
    print('Média abaixo de 5.0: REPROVADO{:2f}'.format(media))
elif media<=5 or media<=6.9:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO{:2f}'.format(media))
else:
    print('Média 7.0 ou superior: APROVADO{:2f}'.format(media))