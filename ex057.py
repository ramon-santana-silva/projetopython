#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo=str(input('Informe (M) para sexo masculino e (F) para sexo feminino ').strip().upper())
while sexo!='M' and sexo!='F':
    sexo=str(input('Informe (M) para sexo masculino e (F) para sexo feminino ').upper())
print('sexo informado pelo usuário foi {}'.format(sexo))

