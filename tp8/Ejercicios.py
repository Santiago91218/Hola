import Funciones
import random
#Ejercicio 1
"""while True:
    number=int(input("Ingrese un numero entero positivo: "))
    if number>=0:
        print(f"La cantidad de digitos que tiene el numero es: {Funciones.digits_count(number)}")
        break
    else:
        continue"""

#Ejercicio 2
"""number_one=int(input("Ingrese un numero: "))
number_two=int(input("Ingrese otro numero: "))
print(Funciones.power(number_one, number_two))"""

#Ejercicio 3
"""word=input("Ingresa una frase: ")
word_2=input("Ingresa la palabra que quieres buscar: ")
print(f"Posiciones donde se encontro {word_2} en {word}: {Funciones.position(word, word_2)}")"""

#Ejercicio 4
"""number = int(input("Ingrese un numero: "))
if Funciones.pair(number):
    print(f"{number} es un numero par")
else:
    print(f"{number} es un numero impar")"""

#Ejercicio 5
"""array = []

for i in range(10):
    num = int(random.random()*100)
    array.append(num)

print(f"La lista es: {array}")
print(f"El número mas grande de la lista es: {Funciones.max_list_num(array, 0, 0)}")"""

#Ejercicio 6
"""array = []
num = int(input("Ingrese la cantidad de elementos que va a tener el arreglo: "))
repeat_num = int(input("Ingrese la cantidad de veces que desea que se repitan los números: "))

for i in range(num):
    num = int(random.random()*5)
    array.append(num)

print(f"El array original es: {array}")
print(f"El array con los números repetidos es: {Funciones.repeat_num_list(array, repeat_num)}")"""

#Ejercicio 7
"""print(Funciones.sum_recursiv(2,8))"""

#Ejercicio 8
"""print("El valor es: ", Funciones.calculate_pascal_value(7,3))"""

#Ejercicio 9
"""list_characters=["&","?","#","%","!"]
number=3
Funciones.combinations(list_characters,number)"""

#Ejercicio 10
"""number=1
while True:
    number=int(input("Ingrese un numero mayor que 0: "))
    if number>0:
        break
    
width, length = Funciones.sheet_measurement(number)
print(f'Ancho de A{number}: {width} mm, Largo de A{number}: {length} mm')"""