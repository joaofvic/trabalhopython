preco = float(input("|somente numeros e pontos| informe o valor do carro"))

distribuidor = 28

impostos = 45

cfabrica = preco* distribuidor/100 + impostos/100

cconsumidor = preco + cfabrica

print("custo de fabrica:", cfabrica)
print("custo final ao consumidor", cconsumidor)