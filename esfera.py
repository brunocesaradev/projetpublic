#ASE = 4 . π . r²
print("Vamos calcular a área de uma esfera")
# dado recebido do usuario
raio = int(input("Digite um número para o raio da esfera > "))
# contante pi
PI = 3.141592
# a variavel ar, armazena a operação realizada
ar = 4 * PI * raio**2
resultado = round(ar,6)
print(f"A área da esfera é {resultado}")