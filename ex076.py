"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
produtos=("arroz",5.3,"feijao",8.9,"macarrao",3.55,"açucar",4.75,"farinha",7.3,"café",9.80,
            "leite",9.5,"Extrato de tomate",3.50)
for i in range(0,len(produtos)):
    if i%2==0:
        print(f'{produtos[i]:<30}', end='' )
    else:
        print(f'R${produtos[i]:>10}')

