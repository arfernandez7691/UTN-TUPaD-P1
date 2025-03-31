print("************************************************************")
print()
print("Programación 1 - Práctico 1: Estructuras secuenciales")
print("Alumno: Atilano Roberto FERNÁNDEZ")
print()
print("************************************************************")
print("Ejercicio 1")
#
# Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


print()
print("************************************************************")
print("Ejercicio 2")
# Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla 
# un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, 
# el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo 
# si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}!")


print()
print("************************************************************")
print("Ejercicio 3")
# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar 
# de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el 
# programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión 
# por pantalla.
nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("Por favor ingrese su edad: ")
lugar_residencia = input("Por favor ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")


print()
print("************************************************************")
print("Ejercicio 4")
# Ejercicio 4: Crear un programa que pida al usuario el radio de un círculo 
# e imprima por pantalla su área y su perímetro.
radio = float(input("Por favor ingrese el radio del círculo: "))
pi = 3.14159265359
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area} y el perímetro del círculo es: {perimetro}")


print()
print("************************************************************")
print("Ejercicio 5")
# Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos 
# e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Por favor ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"La cantidad de segundos ingresada equivale a {horas} horas.")


print()
print("************************************************************")
print("Ejercicio 6")
# Ejercicio 6: Crear un programa que pida al usuario un número e imprima por 
# pantalla la tabla de multiplicar de dicho número.
numero = int(input("Por favor ingrese un número: "))

print(f"Tabla de multiplicar del número {numero}")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")


print()
print("************************************************************")
print("Ejercicio 7")
# Ejercicio 7: Crear un programa que pida al usuario dos números enteros 
# distintos del 0 y muestre por pantalla el resultado de sumarlos, 
# dividirlos, multiplicarlos y restarlos.
num1 = int(input("Por favor ingrese un número entero distinto de cero: "))
num2 = int(input("Por favor ingrese otro número entero distinto de cero: "))

print(f"La suma de los números ingresados es: {num1 + num2}")
print(f"La división de los números ingresados es: {num1 / num2}")
print(f"La multiplicación de los números ingresados es: {num1 * num2}")
print(f"La resta de los números ingresados es: {num1 - num2}")


print()
print("************************************************************")
print("Ejercicio 8")
# Ejercicio 8: Crear un programa que pida al usuario su altura y su peso e 
# imprima por pantalla su índice de masa corporal. Tener en cuenta que el 
# índice de masa corporal se calcula del siguiente modo:
# IMC = peso / altura^2
altura = float(input("Por favor ingrese su altura (en m): "))
peso = float(input("Por favor ingrese peso (en kg): "))

print(f"Su índice de masa corporal es: {peso / altura ** 2}")


print()
print("************************************************************")
print("Ejercicio 9")
# Ejercicio 9: Crear un programa que pida al usuario una temperatura en 
# grados Celsius e imprima por pantalla su equivalente en grados 
# Fahrenheit. Tener en cuenta la siguiente equivalencia:
# Temperatura Fahrenheit = Temperatura Celsius * 9/5 + 32
temperatura = int(input("Por favor ingrese la temperatura en grados Celcius: "))

print(f"La temperatura en grados Fahrenheit es: {temperatura * 9/5 + 32}")


print()
print("************************************************************")
print("Ejercicio 10")
# Ejercicio 10: Crear un programa que pida al usuario 3 números e 
# imprima por pantalla el promedio de dichos números.
num1 = int(input("Por favor ingrese un número: "))
num2 = int(input("Por favor ingrese otro número: "))
num3 = int(input("Por favor ingrese otro número: "))
print(f"El promedio de los números ingresados es: {(num1 + num2 + num3) / 3}")
print()
print("************************************************************")