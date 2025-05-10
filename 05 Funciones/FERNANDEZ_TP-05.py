print("************************************************************")
print()
print("Programación 1 - Práctico 5.1: Listas")
print("Alumno: Atilano Roberto FERNÁNDEZ")
print()
print("************************************************************")
print("Ejercicio 1")
# 1) Crear una lista con los números del 1 al 100 que sean 
# múltiplos de 4. Utilizar la función range.
#
# La función range(), toma tres argumentos: el número inicial, 
# el número final menos 1 y el incremento. En este caso, 
# comenzamos en 4 y terminamos en 101, con un incremento de 4. 
# Esto generará una lista de números que son múltiplos de 4 
# desde 4 hasta 100. La función list() convierte el objeto 
# range en una lista.
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


print()
print("************************************************************")
print("Ejercicio 2")
# 2) Crear una lista con cinco elementos (colocar los elementos 
# que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo 
# como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos!
#
# La indexación con números negativos permite acceder a los 
# elementos de una lista desde el final. Por ejemplo, -1 se 
# refiere al último elemento, -2 al penúltimo, y así sucesivamente.
# En este caso, -2 se refiere al penúltimo elemento de la lista.
cosas_favoritas = ["música", "libros", "películas", "chocolate", "bicicleta"]
print(cosas_favoritas[-2])



print()
print("************************************************************")
print("Ejercicio 3")
# 3) Crear una lista vacía, agregar tres palabras con append e 
# imprimir la lista resultante por pantalla. Pista: para crear 
# una lista vacía debes colocar los corchetes sin nada en su 
# interior. Por ejemplo: lista_vacia = []
#
lista_vacia = []
lista_vacia.append("Uno")
lista_vacia.append("Dos")
lista_vacia.append("Tres")
print(lista_vacia)


print()
print("************************************************************")
print("Ejercicio 4")
# 4) Reemplazar el segundo y último valor de la lista “animales” 
# con las palabras “loro” y “oso”, respectivamente. Imprimir la 
# lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con 
# números negativos! animales = ["perro", "gato", "conejo", "pez"]
#
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"      # Segundo elemento (índice 1) recordar
                          # que el primer elemento tiene índice 0
animales[-1] = "oso"      # Último elemento con índice negativo
print(animales)


print()
print("************************************************************")
print("Ejercicio 5")
# 5) Analizar el siguiente programa y explicar con tus palabras 
# qué es lo que realiza.
#
# Se crea una lista con 5 elementos numéricos
numeros = [8, 15, 3, 22, 7]

# Se utiliza la función max() para encontrar el valor máximo
# en la lista y después se utiliza el método remove() para
# eliminar ese valor.
numeros.remove(max(numeros))

# Finalmente, se imprime la lista resultante y se verifica que el 
# número máximo, en este caso el 22, ha sido eliminado.
print(numeros)



print()
print("************************************************************")
print("Ejercicio 6")
# 6) Crear una lista con números del 10 al 30 (incluído), haciendo 
# saltos de 5 en 5 y mostrar por pantalla los dos primeros.
# 
# La función range(), toma tres argumentos: el número inicial, 
# el número final menos 1 y el incremento. En este caso, 
# comenzamos en 10 y terminamos en 31, con un incremento de 5. 
# Esto generará una lista de números desde 10 hasta 30. 
# La función list() convierte el objeto  range en una lista.
numeros = list(range(10, 31, 5))

# Muestra los dos primeros elementos de la lista.
# La indexación en Python comienza en 0, por lo que los dos
# primeros elementos de la lista son los que tienen índices 0 y 1.
# El uso de [:2] es una forma de abreviada para obtener
# los elementos desde el índice 0 hasta el índice 2 (sin incluirlo).
# Esto significa que se obtendrán los elementos en las posiciones
# 0 y 1 de la lista, que son los dos primeros elementos.
print(numeros[:2])


print()
print("************************************************************")
print("Ejercicio 7")
# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la 
# lista “autos” por dos nuevos valores cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]
#
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores en los índices 1 y 2
# Los índices de esta lista son 0, 1, 2 y 3
# Por lo tanto, los valores centrales son los que están
# en las posiciones 1 y 2.
# En este caso, se reemplazan por "camioneta" y "coupe".
autos[1:3] = ["camioneta", "coupe"]
print(autos)


print()
print("************************************************************")
print("Ejercicio 8")
# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 
# 10 y 15 usando append directamente. Imprimir la lista resultante 
# por pantalla.
#
# Se inicializa la lista vacía
dobles = []
# La función append() se utiliza para agregar un elemento al final de la lista.
# En este caso, se agregan los dobles de 5, 10 y 15 a la lista "dobles".
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)


print()
print("************************************************************")
print("Ejercicio 9")
# 9) Dada la lista “compras”, cuyos elementos representan los 
# productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#
#   a) Agregar "jugo" a la lista del tercer cliente usando append.
#   b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#   c) Eliminar "pan" de la lista del primer cliente.
#   d) Imprimir la lista resultante por pantalla
#
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

# d) Mostrar resultado
print(compras)


print()
print("************************************************************")
print("Ejercicio 10")
# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#   Posición lista_anidada[0]: 15
#   Posición lista_anidada[1]: True
#   Posición lista_anidada[2][0]: 25.5
#   Posición lista_anidada[2][1]: 57.9
#   Posición lista_anidada[2][2]: 30.6
#   Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.
#
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
