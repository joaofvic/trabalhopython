#informar valores sem pontos, virgulas ou simbolos de porcentagem
boleto = float(input ("|somente ponto| informe o valor do boleto:\n"))

juros = float(input("|somente numeros e pontos| informe o juros cobrado:\n"))

atraso= int(input("numero de dias atrasado:\n"))

op= boleto + (boleto * (juros)/100) * atraso

print("novo valor a ser pago:", op)