print("************************************************************")
print()
print("Programación 1 - Práctico 4: Estructuras repetitivas")
print("Alumno: Atilano Roberto FERNÁNDEZ")
print()
print("************************************************************")
print("Ejercicio 1")
# 1) Crea un programa que imprima en pantalla todos los números 
# enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden 
# creciente, mostrando un número por línea.
#
# Se usa un bucle for para iterar desde 0 hasta 101.
# La función range() se usa la para definir el rango de valores.
# Por defecto, comienza en 0.
# Como se va a considerar hasta el número 100 y como la función 
# no incluye al último número, se suma 1, de esta forma, el 
# número final es 101 pero la función va a considerar hasta 
# el 100, que es lo que se quería.
for i in range(101):
    print(i)

print()
print("************************************************************")
print("Ejercicio 2")
# 2) Desarrolla un programa que solicite al usuario un número 
# entero y determine la cantidad de dígitos que contiene.
#
# Se solicita al usuario que ingrese un número entero,
# como la entrada es una cadena de caracteres la convierte en 
# un número entero y positivo.
#
numero = int(input("Por favor ingrese un número entero: "))

# El número se vuelve a convertir en una cadena de caracteres y
# se determina su longitud mediante la función len().
print(f"Cantidad de dígitos: {len(str(numero))}")

print()
print("************************************************************")
print("Ejercicio 3")
# 3) Escribe un programa que sume todos los números enteros 
# comprendidos entre dos valores dados por el usuario, excluyendo 
# esos dos valores.
#
#
a = int(input("Por favor ingrese el primer número: "))
b = int(input("Por favor ingrese el segundo número: "))

# Se inicializa la variable suma en 0.
suma = 0

# Se usa un bucle for para iterar desde el número menor
# hasta el número mayor, excluyendo los extremos.
# Se usa la función min() para obtener el número menor
# y la función max() para obtener el número mayor.
# Se usa la función range() para definir el rango de valores.
for i in range(min(a, b) + 1, max(a, b)):
    # Se va sumando el número ingresado a la variable suma
    suma += i

# Se imprime la suma total
print(f"La suma es: {suma}")


print()
print("************************************************************")
print("Ejercicio 4")
# 4) Elabora un programa que permita al usuario ingresar números 
# enteros y los sume en secuencia. El programa debe detenerse 
# y mostrar el total acumulado cuando el usuario ingrese un 0.
#
# Se inicializa la variable total en 0 y la variable sale en True.
total = 0
sale = True

# Se inicia el bucle con la variable sale como True
# para permitir la entrada de números.
# Cuando el usuario ingresa 0, la variable sale se convierte 
# en False
while sale:
    n = int(input("Por favor ingrese un número (0 para salir): "))
    if n == 0:
        sale = False
# Se suma el número ingresado a la variable total    
    total += n

# Se imprime el total acumulado
print(f"Suma total: {total}")

print()
print("************************************************************")
print("Ejercicio 5")
# 5) Crea un juego en el que el usuario deba adivinar un número 
# aleatorio entre 0 y 9. Al final, el programa debe mostrar 
# cuántos intentos fueron necesarios para acertar el número.
#
# Se importa la función randint() del módulo random para
from random import randint

# Se usa la función randint() para generar un número aleatorio 
# entre 0 y 9.
secreto = randint(0, 9)
intentos = 0
acerto = True

while acerto:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto! Lo haz adivinado en {intentos} intento(s).")
        acerto = False



print()
print("************************************************************")
print("Ejercicio 6")
# 6) Desarrolla un programa que imprima en pantalla todos los 
# números pares comprendidos entre 0 y 100, en orden decreciente.
#
# Se usa un bucle for para iterar desde 100 hasta 0,
# decrementando de 2 en 2.
# Se usa la función range() para definir el rango de valores.
# El primer parámetro indica el valor inicial (100),
# El segundo parámetro indica el valor final, 
# en este caso -1 pero no lo incluye, entonces termina en 0.
# El tercer parámetro de range() indica el paso, en este caso -2.
for i in range(100, -1, -2):
    print(i)



print()
print("************************************************************")
print("Ejercicio 7")
# 7) Crea un programa que calcule la suma de todos los números 
# comprendidos entre 0 y un número entero positivo indicado 
# por el usuario.
#
# Se solicita al usuario que ingrese un número entero positivo.
n = int(input("Por favor ingrese un número entero positivo: "))

#
suma = sum(range(n + 1))
print(f"Suma de 0 a {n}: {suma}")


print()
print("************************************************************")
print("Ejercicio 8")
# 8) Escribe un programa que permita al usuario ingresar 100 
# números enteros. Luego, el programa debe indicar cuántos de 
# estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el 
# programa puedes usar una cantidad menor, pero debe estar 
# preparado para procesar 100 números con un solo cambio).
#
# Se definen y inicializan las variables necesarias para el 
# cálculo de la media.
# N = 100  # Valor para que solicita el ejercicio
N = 6  # Valor para probar
# Se inicializan las variables en 0.
pares = impares = positivos = negativos = 0

# N define el rango de valores a ingresar (0 a N-1)
# Se usa un bucle for para iterar N veces.
for i in range(N):
    num = int(input("Por favor ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

print()
print("************************************************************")
print("Ejercicio 9")
# 9) Elabora un programa que permita al usuario ingresar 100 
# números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, 
# pero debe poder procesar 100 números cambiando solo un valor).
#
# Se definen y inicializan las variables necesarias para el 
# cálculo de la media.
# N = 100  # Valor para que solicita el ejercicio
N = 5  # Valor para probar
# Se inicializa la variable suma en 0.
suma = 0

# N define el rango de valores a ingresar (0 a N-1)
# Se usa un bucle for para iterar N veces.
for i in range(N):
    # Se solicita al usuario que ingrese un número entero.
    num = int(input("Por favor ingrese un número: "))
    # Se van sumando los números ingresados.
    suma += num

# Se calcula la media dividiendo la suma total por N.
media = suma / N
# Se usa la función print() para mostrar el resultado.
print(f"Media: {media}")

print()
print("************************************************************")
print("Ejercicio 10")
# 10) Escribe un programa que invierta el orden de los dígitos 
# de un número ingresado por el usuario. Ejemplo: si el usuario 
# ingresa 547, el programa debe mostrar 745.
#
# Se define la variable "inverso" y se inicializa con 0.
# int() devuelve 0 e inicializa la variable como entera.
inverso = int()

# Solicitamos que el usuario ingrese un número.
num = int(input("Por favor ingrese un número entero:"))

while num!=0:
	# Obtiene el último dígito del número ingresado.
	digito = num%10
	# Divide el número entre 10 y trunca el
	# número para eliminar el último dígito.
	num = int(num/10)
	# Construye el número inverso
	inverso = inverso*10+digito
	
 # Presenta el resultado
print("El número inverso es: ",inverso)