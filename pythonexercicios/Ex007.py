#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
nome= 'Digite o nome do aluno: '
nt1=float(input('Digite a nota da Av1: '))
nt2=float(input('digite a nota da Av2: '))
media= (nt1+nt2)/2
#print('Nota da Av1: {} /n Nota da Av2: {} /n').format(nt1,nt2)
print('A nota media do aluno: {:.1f}, é:{:.1f} '.format(nome,media))