Numeros = []

cantNum = int(input('Ingrese la cantidad de numeros: '))

for index in range(cantNum):
    Numeros.append(input('Ingrese un numero: '))

len = len(Numeros)

print(Numeros)

ListaInvertida = []
print('Lista invertida')
for index in range(len):
    ListaInvertida.append(Numeros[(len-1) - index])
print(ListaInvertida)

