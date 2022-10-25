"""
Crear un algoritmo que muestre los primeros 10 numeros de la
sucesion de fibonacci. La sucecion comienzo con los numeros
0 y 1 y a partir de estos cada elemento es la suma de los dos
numeros anteriors en la secuencia: 
0,1,1,2,3,5,8,13,21,34,55
"""

numero=int(input("Hasta donde desea genera la sucesion de Fibonacci: "))
n1=0
n2=1

print(n1, n2, end=" ")

for i in range(numero - 2):
    n3=n1+n2
    print(n3, end=" ")
    n1=n2
    n2=n3