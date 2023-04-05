dolares_americanos = input("Cuantos dolares americanos tienes? ")
dolares_americanos = float(dolares_americanos)
valor_dolar = 4400
pesos = dolares_americanos*valor_dolar
pesos=round(pesos,2)
pesos = str(pesos)
print("tienes $"+pesos+" pesos colombianos")