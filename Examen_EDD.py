#Actividad 1. (1 punto) Escribir en lenguaje Python un programa que:

#1.- Pida por teclado la duración en minutos (dato entero) del viaje en Acciona (teniendo en cuenta el tiempo según el modo, Standard, Custom o X-tra.

#2.- Calcule el coste total del viaje.

#3.- Muestre por pantalla el resultado (dato real) en euros.

#Nota: El precio por minuto de Acciona es de 0.31cent/min en Standar, 0,36 cent/min en Custom y 0,39€ cent/min en X-tra.

minutos = int(input("Introduzca los minutos del viaje: "))

tipo_viaje = input("Introduzca el tipo de viaje que quieres (los tipos son \n"
                   "Acciona, Standar y Custom o X-tra): ")
resultado = 0
if tipo_viaje=="Acciona":
    resultado = minutos*0.31/100
if tipo_viaje=="Standar":
    resultado = minutos*0.36/100
if tipo_viaje=="Custom" or tipo_viaje=="X-tra":
    resultado = minutos*0.39/100

print(resultado)




#Actividad 2. (1 punto) git. Qué es un repositorio?¿Qué comando es necesario para crear un repositorio?  ¿Cómo configurarías inicialmente git?
"""

"""

#Actividad 3. (1 punto) ¿Qué es una rama?¿Cómo creamos una rama y trabajamos entre ellas?¿Y si queremos unir ramas?
"""


"""

#Actividad 4. (1 punto) 1.¿Cómo observaríamos el estado de nuestro repositorio? 2.¿Cómo comprobamos los commits realizados?
#3.¿Con cuál instrucción prepararíamos el repositorio para pasar de working area a staging area?
"""

"""

#Actividad 5. (1 punto) Haciendo uso del debugger, corrige los errores sintácticos del siguiente programa que dado dos números, devuelve el mayor. 
# Explica el proceso completo de depuración para el siguiente código, incluyendo la inspección de variables desde el inicio hasta el final del proceso.

def max(n1, n2):
    if n2>n1:
        return n2
    else:
        return n1
print(max(100,50))


#Actividad 6. Pseint (1 punto) En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar entre 0 y 500.
# Si el número escogido es menor que 100 el descuento es del 10% sobre el total de la compra, si es mayor o igual a 100 el descuento es del 20%. Además, si el número es par,  
# se le aplicará un 2% adicional. Por el contrario, si es impar, se le aplicará un 3%.
"""

"""

#Actividad 7. Pseint (1 punto) Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso actual. Además, queremos saber si el porcentaje es par o impar.
# En el caso de ser 0, debe visualizar “el número no es par ni impar”  Diseñar un algoritmo para este propósito . 

"""

"""
#Actividad 8. (1 punto) Describe el procedimiento para ver el estado de nuestro código, elegir uno especifico y enviarlo a repositorio local.  ¿Cómo volverías a una versión anterior?
"""

"""



#Actividad 9 (2 puntos) Haciendo uso del debugger, corrige los errores sintácticos del siguiente programa que permite al usuario ingresar números enteros. La repetición termina cuando 
# el usuario ingresa un número para el cual la suma de sus dígitos sea mayor que 1000 ó múltiplo de 5. Finalmente, mostrar cuántos números impares ingresó el usuario antes de cortar la 
# repetición. Explica el proceso completo de depuración para el siguiente código, incluyendo la inspección de variables desde el inicio hasta el final del proceso.

def esPar(numero):
    return numero%3==0

def sumatoriaDigitos(numero):
    total=0
    while total !=0:
        ultimoDigito=numero%10
        total=total+ultimoDigito
        numero=numero/10
    return total

cantidadImpares=0
n=int(input("Escribe un número:"))
while sumatoriaDigitos(n)>1000 and sumatoriaDigitos(n)%3!=0:
    if esPar(n):
        cantidadImpares=cantidadImpares+1
    n=int(input("Escribe un número:"))
print("Cantidad de impares:", cantidadImpares)



#Actividad 10. (1 punto) Describe los pasos para pasar de repositorio local a remoto.
"""
"""


