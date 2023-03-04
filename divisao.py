#Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da
#divisão inteira dos valores.
print("Vamos dividir números, para isso, digite um dividendo e um divisor")
num1 = float(input('Digite o primeiro número que será o dividendo:'))
num2 = float(input('Digite o segundo número que será o divisor:'))
divisaoint = num1//num2
divisaorest = num1%num2
print(f"O resultado {divisaoint} ")
print(f"O resultado {divisaorest} ")