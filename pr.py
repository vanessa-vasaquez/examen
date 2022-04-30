objetos = []

cantidadObjetos = int(input('Ingrese la cantidad de objetos: '))

for index in range(cantidadObjetos):
    objetos.append(input('Ingrese un objeto: '))

len = len(objetos)

print(objetos)

arrayInvertido = []
print('Array invertido')
for index in range(len):
    arrayInvertido.append(objetos[(len-1) - index])
print(arrayInvertido)