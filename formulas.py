
print("Olá, vamos descobrir o comprimento de uma circunfência?")
raio =  int(input('Digite um número entre 1 e 10 ! > '))   
PI = 3.141592                                                     
compri_circun = 2*raio *PI                                      
resultado = round(compri_circun,6)                                
print (f"O comprimento da circunferência é >{resultado} ")        
print(''' 
Muito rápido né? 
Podemos continuar calculando !
O que acha de tentarmos descobrir a área de um circulo?''')
raio2 = int(input('Para isso, digite um novo valor para o raio >'))      
resultado2 = PI * raio2**2                                              
compress_decimal = round(resultado2,6)                                   
print(f"A área do círculo é > {compress_decimal}")                     
#A = π r²