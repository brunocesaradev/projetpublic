# C = 2πr
print("Olá, vamos descobrir o comprimento de uma circunfência?")  # convite ao usuario
raio =  int(input('Digite um número entre 1 e 10 ! > '))          #rece a informação do usuario
PI = 3.141592                                                     # declara uma constante
compri_circun = 2*raio *PI                                        # realiza a operação
resultado = round(compri_circun,6)                                # define numero de casas decimais
print (f"O comprimento da circunferência é >{resultado} ")        # imprime o resultado para o usuario 4
print(''' 
 Muito rápido né? 

Podemos continuar calculando !

O que acha de tentarmos descobrir a área de um circulo?''')


raio2 = int(input('Para isso, digite um novo valor para o raio >'))      # recebe um novo valor de raio para a 2 operação  
resultado2 = PI * raio2**2                                               # realiza a operação
compress_decimal = round(resultado2,6)                                   # define o numero de casas
print(f"A área do círculo é > {compress_decimal}")                       #imprimi o resultado
#A = π r²