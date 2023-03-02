tempservice = float(input("Informe o tempo de serviço do funcionário em anos: "))
val_bonus = float(input("Informe o valor do bônus por ano trabalhado em reais: "))

bonificacao = tempservice * val_bonus

print(f"A bonificação do funcionário será de R${bonificacao:.2f}")
