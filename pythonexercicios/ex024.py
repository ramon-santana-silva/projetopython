#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
santacity=str(input('digite o nome de uma cidade\n')).upper().lstrip()

print('A resposta é: {}'.format(santacity.startswith('SANTO ')))
  