# recebe do usuário a quantidade de minutos a ser convertida
minutos = int(input("Digite a quantidade de minutos: "))

# Calcula as horas e minutos 
horas = minutos // 60
minutos_restantes = minutos % 60

# Imprime o resultado para o usuario
print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")
