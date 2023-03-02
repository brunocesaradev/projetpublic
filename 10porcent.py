#Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado
#para duas casas decimais.
preco = float(input('Digite o valor do produto para a aplicação do desconto :'))
descont = preco/100 *10
valorcmdesconto = preco - descont
valoround = round(valorcmdesconto,2)
print(f"O valor a pagar é : {valorcmdesconto}")