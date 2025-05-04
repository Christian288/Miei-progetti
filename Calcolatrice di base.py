def somma(a, b):
    return a + b
def sottrazione(a, b):
    return a - b
def moltiplicazione(a, b):
    return a * b
def divisione(a, b):
    if b != 0:
        return a / b
    else:
        return "Errore: Divisione per zero."
print("la somma tra i due numeri è:", somma(5, 3))
print("La sottrazione fra i due numeri è:", sottrazione(5, 3))
print("La moltiplicazione fra i due numeri è:", moltiplicazione(5, 3))
print("La divisione fra i due numeri è:", divisione(5, 3))