print("************************************************************")
print()
print("Programación 1 - Práctico 3: Estructuras condicionales")
print("Alumno: Atilano Roberto FERNÁNDEZ")
print()
print("************************************************************")
print("Ejercicio 1")
# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje 
# en pantalla que diga “Es mayor de edad”.
#
edad = int(input("Por favor ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

print()
print("************************************************************")
print("Ejercicio 2")
# 2) Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla 
# un mensaje que diga “Aprobado”; en caso contrario deberá 
# mostrar el mensaje “Desaprobado”.
#
nota = float(input("Por favor ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print()
print("************************************************************")
print("Ejercicio 3")
# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla 
# el mensaje "Ha ingresado un número par"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python 
# para evaluar si un número es par o impar.
#
numero = int(input("Por favor ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print()
print("************************************************************")
print("Ejercicio 4")
# 4) Escribir un programa que solicite al usuario su edad e 
# imprima por pantalla a cuál de las siguientes categorías 
# pertenece:
#   -Niño/a: menor de 12 años.
#   -Adolescente: mayor o igual que 12 años y menor que 18 años.
#   -Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   -Adulto/a: mayor o igual que 30 años.
#
edad = int(input("Por favor ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

print()
print("************************************************************")
print("Ejercicio 5")
# 5) Escribir un programa que permita introducir contraseñas de 
# entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario 
# ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese 
# una contraseña de entre 8 y 14 caracteres". Nota: investigue 
# el uso de la función len() en Python para evaluar la cantidad 
# de elementos que tiene un iterable tal como una lista o un string.
#
contraseña = input("Por favor ingrese una contraseña (entre 8 y 14 caracteres): ")

longitud = len(contraseña)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")

print()
print("************************************************************")
print("Ejercicio 6")
# 6) escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para 
# determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla.
#

# 1.- Se solicita al usuario que ingrese la cantidad de números aleatorios
cantNumAleatorios = int(input("Por favor ingrese la cantidad de números a generar: "))

# 2.- Se importan las funciones que se necesitan de las librería 
#     statistics y random
from random import randint
from statistics import mean, median, mode

# 3.- Se genera una lista con los números aleatorios entre 1 y 100
numeros = [randint(1, 100) for i in range(cantNumAleatorios)]

# 4.- Se calcula la moda, la mediana y la media
media = mean(numeros)
mediana = median(numeros)
moda = mode(numeros)

# 5.- Si imprimen los número aleatorios generados y la moda, 
#     mediana y media.
print("Lista de números aleatorios:")
print(numeros)
print()
print("Parámetros Estadísticos:")
print(f"   Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"  Media: {media}")

# 6.- Se determina el sesgo
if media > mediana and mediana > moda:
    print("\nSesgo positivo o a la derecha")
elif moda > mediana and mediana > media:
    print("\nSesgo negativo o a la izquierda")
else:
    print("\nSin sesgo")

print()
print("************************************************************")
print("Ejercicio 7")
# 7) Escribir un programa que solicite una frase o palabra 
# al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el 
# string resultante por pantalla; en caso contrario, dejar 
# el string tal cual lo ingresó el usuario e imprimirlo 
# por pantalla.
#
# Se solicita al usuario que ingrese una frase o palabra.
texto = input("Por favor ingrese una frase o palabra: ")

# Se verifica que la frase o palabra ingresada termina 
# en vocal. Si el usuario ingresó la palabra o frase en 
# mayúsculas la convertimos en minúscula con el método 
# .lower(). 
# La variable texto la manajamos como una lista y para 
# seleccionar la última letra de la lista utilizamos el
# índice -1, el signo - indica que se empieza a seleccionar
# desde el final de la lista y el 1 indica que se
# selecciona 1 elemento.
#
# Si el elemento seleccionado coincide con una vocal de la
# cadena de caracteres "aeiou" se añade un signo de de
# exclamación ("!") al final de la cadena de caracteres.
# En caso contrario, se deja el string tal cual lo ingresó
# el usuario.
if texto[-1].lower() in "aeiou":
    texto += "!"
    
# Se imprime el resultado
print("Resultado:", texto)

print()
print("************************************************************")
print("Ejercicio 8")
# 8) Escribir un programa que solicite al usuario que ingrese 
# su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#
# El programa debe transformar el nombre ingresado de acuerdo a 
# la opción seleccionada por el usuario e imprimir el resultado 
# por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas 
# y minúsculas.
#
# Solicita el nombre al usuario
nombre = input("Por favor ingrese su nombre: ")

# Solicita la opción deseada
print("\nPor favor seleccione una opción:")
print("1.- Mostrar el nombre en MAYÚSCULAS")
print("2.- Mostrar el nombre en minúsculas")
print("3.- Mostrar el nombre con la primera letra en mayúscula")

opcion = input("Por favor ingrese el número de opción (1, 2 o 3): ")

# Aplica la transformación de acuerdo a la opción elegida
if opcion == "1":
    # Convierte el nombre a mayúsculas
    nombre_transformado = nombre.upper()
elif opcion == "2":
    # Convierte el nombre a minúsculas
    nombre_transformado = nombre.lower()
elif opcion == "3":
    # Convierte el nombre a minúsculas y luego la 
    # primera letra a mayúscula
    nombre_transformado = nombre.title()
else:
    
    nombre_transformado = "Opción no válida."

# Muestra el resultado
print("\nResultado:", nombre_transformado)

print()
print("************************************************************")
print("Ejercicio 9")
# 9) Escribir un programa que pida al usuario la magnitud de un 
# terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado 
# por pantalla:
#   -Menor que 3: "Muy leve" (imperceptible).
#   -Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#   -Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#   -Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#   -Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#   -Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
#
# Solicitar la magnitud y acepta decimales pero redondea a un decimal
magnitud = float(input("Por favor ingrese la magnitud del terremoto: "))
magnitud = round(magnitud, 1)

# Clasificación según la escala de Richter
# La escala Richter es una escala logarítmica, que comienza en 0
# y aunque no tiene un límite superior se toma como límite
# superior a 10 ya que la energía liberada no es posible alcanzarla.
# La mayor magnitud registrada es de 9.5 en Chile en 1960.
if magnitud >= 0 and magnitud <= 10:

    if magnitud < 3:
        clasificacion = "Muy leve (imperceptible)"
    elif magnitud < 4:
        clasificacion = "Leve (ligeramente perceptible)"
    elif magnitud < 5:
        clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
    elif magnitud < 6:
        clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
    elif magnitud < 7:
        clasificacion = "Muy Fuerte (puede causar daños significativos)"
    else:
        clasificacion = "Extremo (puede causar graves daños a gran escala)"

    # Mostrar resultado
    print(f"Clasificación del terremoto: {clasificacion}")

else:
    print("Entrada inválida. Por favor ingrese una magnitud válida (entre 0 y 10)")

print()
print("************************************************************")
print("Ejercicio 10")
# 10) Utilizando la información aportada en la siguiente tabla 
# sobre las estaciones del año:
#
#   +-----------------------------------------+--------------------+--------------------+
#   |             Período del año             |   Estación en el   |  Estación en el    |
#   |               Temperatura               |  hemisferio norte  |  hemisferio sur    |
#   +-----------------------------------------+--------------------+--------------------+
#   | Desde el 21 de diciembre hasta el 20 de |      Invierno      |       Verano       |
#   |             marzo (incluídos)           |                    |                    |
#   +-----------------------------------------+--------------------+--------------------+
#   |Desde el 21 de marzo hasta el 20 de junio|     Primavera      |       Otoño        |
#   |                (incluídos)              |                    |                    |
#   +-----------------------------------------+--------------------+--------------------+
#   |   Desde el 21 de junio hasta el 20 de   |       Verano       |      Invierno      |
#   |          septiembre (incluídos)         |                    |                    |
#   +-----------------------------------------+--------------------+--------------------+
#   |Desde el 21 de septiembre hasta el 20 de |       Otoño        |     Primavera      |
#   |          diciembre (incluídos)          |                    |                    |
#   +-----------------------------------------+--------------------+--------------------+
#
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué 
# mes del año es y qué día es. El programa deberá utilizar esa información para imprimir 
# por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
#
# Esta función valida que la fecha ingresada sea real.
def fecha_valida(anio, mes, dia):
    dias_en_meses = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    if mes < 1 or mes > 12:
        return False

    # Si es febrero y el año es bisiesto
    if mes == 2 and ((anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)):
        max_dia = 29
    else:
        max_dia = dias_en_meses[mes - 1]  # ajustar por índice base 0

    return 1 <= dia <= max_dia

# Se solicita que se ingrese el hemisferio.
# Se utiliza el método .strip() para eliminar espacios en blanco
# al principio y al final de la cadena de caracteres.
# Se utiliza el método .lower() para convertir la cadena de
# caracteres a minúsculas y así evitar errores de comparación
# por el uso de mayúsculas o minúsculas.
hemisferio = input("¿En qué hemisferio te encuentras? (Norte/Sur): ").strip().lower()

# Se verifica que el hemisferio ingresado sea válido.
if hemisferio not in ["norte", "sur"]:
    print("Hemisferio no válido. Debe ser 'Norte' o 'Sur'.")
else:
    # Se solicita que se ingrese el año, mes y día
    anio = int(input("¿En qué año estás?: "))
    mes = int(input("¿En qué mes estás? (1-12): "))
    dia = int(input("¿Qué día del mes es? (1-31): "))

    # Se valida la fecha ingresada
    # Se utiliza la función fecha_valida() para verificar que la
    # fecha ingresada sea válida. Si no es válida se muestra un
    # mensaje de error y se le pide al usuario que ingrese una
    # fecha válida.
    if not fecha_valida(anio, mes, dia):
        print("Fecha no válida. Verifique el mes y el día.")
    else:
        # Se convierte a formato MMDD para facilitar comparación
        fecha = mes * 100 + dia

        # Se determina la estación en base a la información de la tabla.
        if hemisferio == "norte":
            if (fecha >= 1221 and fecha <= 1231) or (fecha >= 101 and fecha <= 320):
                estacion = "Invierno"
            elif fecha >= 321 and fecha <= 620:
                estacion = "Primavera"
            elif fecha >= 621 and fecha <= 920:
                estacion = "Verano"
            else:
                estacion = "Otoño"
        else:  # Hemisferio Sur
            if (fecha >= 1221 and fecha <= 1231) or (fecha >= 101 and fecha <= 320):
                estacion = "Verano"
            elif fecha >= 321 and fecha <= 620:
                estacion = "Otoño"
            elif fecha >= 621 and fecha <= 920:
                estacion = "Invierno"
            else:
                estacion = "Primavera"

        # Se imprime el resultado.
        print(f"En el hemisferio {hemisferio.title()}, el {dia}/{mes}/{anio} es {estacion}.")
