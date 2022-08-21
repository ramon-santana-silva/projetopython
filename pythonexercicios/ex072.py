"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""
while True:
    usernumber = int(input('Digite um número entre 0 e 20 :'))
    if usernumber>0 and usernumber<=20:
        numeros=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
                'quatorze','quinze','desesseis', 'desessete','dezoito','dezenove','vinte')        
        break
    print('digite novamente: \n')
    
print(f'o valor de {usernumber} por extenso é: {numeros[usernumber]}')
