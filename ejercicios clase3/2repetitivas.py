def potenciaAlCuadrado(n):
    return n ** 2

suma = 0
numero_n = int(input("ingrese un numero n: "))
for x in range(1, numero_n+1):
    print("la variable x tiene: ", x)
    print("resultado : ", potenciaAlCuadrado(x))
    suma = suma + (potenciaAlCuadrado(x))
print("Terminado")
print("suma total: ",suma)