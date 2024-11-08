'''permite al usuario ingresar números enteros. La repetición termina cuando el usuario
ingresa un número para el cual la suma de sus dígitos sea mayor que 1000 ó múltiplo de 5.
Finalmente, mostrar cuántos números impares ingresó el usuario antes de cortar la
repetición. Explica el proceso completo de depuración para el siguiente código, incluyendo
la inspección de variables desde el inicio hasta el final del proceso.'''

def esPar(numeros):
    if numeros %2 == 0:
        return True

def sumatorioDigitos(numeros):
    total = 0
    for i in numeros:
        total += i



