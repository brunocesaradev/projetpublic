#Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da
#divisão inteira dos valores.
print("Vamos dividir números, para isso, digite um dividendo e um divisor")
num1 = float(input('Digite o primeiro número que será o dividendo:'))
num2 = float(input('Digite o segundo número que será o divisor:'))
divisaoreal = num1/num2
divisaoint = num1//num2
print(f"O resultado {divisaoreal} ")
print(f"O resultado {divisaoint} ")