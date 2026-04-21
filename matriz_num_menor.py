matriz = [
    [5, 2, 8],
    [1, 9, 3],
    [4, 7, 6]
]
suma=0
menor = matriz[0][0]
mayor = matriz[0][0]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
          if matriz[i][j]>mayor:
              mayor=matriz[i][j]
print("mayor valor:", mayor)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
          if matriz[i][j]<menor:
            menor=matriz[i][j]
print("menor valor:", menor)

for fila in matriz:
    for num in fila:
        suma+=num
print("suma es :",suma)

promedio=0
cantidad_N=sum(len(fila) for fila in matriz)
promedio=suma/cantidad_N
print("el promedio es :",promedio)


