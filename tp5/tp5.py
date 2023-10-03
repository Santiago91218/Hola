import math
import funciones
# Ejercicio 1
"""def DNI(dni):
    dni_str = str(dni)
    if len(dni) >=7 and len(dni)<=8:
        if dni.isdigit():
            return True
        return False
    else:
        return False

dni = input("Ingrese su DNI: ")
print(funciones.DNI(dni))"""

# Ejercicio 2
"""def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()
    if palabras:
        return len(palabras[-1])
    else:
        return 0
cadena = input("Ingrese una frase: ")
print(f"La longitud de la ultima palabra es: {funciones.longitud_ultima_palabra(cadena)}")"""

# Ejercicio 3
"""def name(name,last_name,dni):
    name_str = name.split()
    if len(name_str) == 1:  
        name1 = name_str[0]
        full_name = name1 + " "
    elif len(name_str) == 2:    
        name1 = name_str[0]
        name2 = name_str[1]
        full_name = name1 + " " + name2 + " "
    else:
        print("Ingreso un dato incorrecto!")
    cant_last_name = len(last_name)
    full_name += last_name
    funciones.DNI(dni)
    if funciones.DNI(dni) == True:
        if len(dni) == 7:
            id = int(dni) // 10000
        else:
            id = int(dni) // 100000 
    name_id = name1+ str(cant_last_name) + str(id)
    print(f"#Nombre: {full_name}")
    print(f"#ID -> {name_id}")

name = input("Ingrese su nombre: ").title()
last_name = input("Ingrese su apellido: ").title()
dni = input("Ingrese su dni: ")
funciones.name(name,last_name,dni)"""

# Ejercicio 4
"""def multiplo(num1,num2):
    if num1 % num2 == 0:
        print(f"{num1} es multiplo de {num2}")
    else:
        print(f"{num1} ni es multiplo de {num2}")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
funciones.multiplo(num1,num2)"""

# Ejercicio 5
"""def cal_temp(temp_max,temp_min):
    temperature_med=(temp_max+temp_min)/2
    return temperature_med

tot_days=int(input("Cuantos dias va a ingresar?: "))
aux=0
while aux<tot_days:
    aux+=1
    print(f"Dia {aux}")
    temperature_max=float(input("Ingrese la temperatura maxima: "))
    temperature_min=float(input("Ingrese la temperatura minima: "))
    print("La temperatura media es: ", cal_temp(temperature_max,temperature_min))"""

# Ejercicio 6 
"""def transform_word(word_space):
    for i in word_space:
        if i != None:
            print(i, end=" ")

word=input("Ingrese una cadena de texto: ")
transform_word(word)"""

# Ejercicio 7
"""def travel_list(list,max,min):
    for i in list:
        if i>max:
            max=i
        elif i<min:
            min=i
    print(f"El numero maximo es: {max}")
    print(f"El numero minimo es: {min}")

list_number=[]
number=maximo=1
while number!=0:
    number=int(input("Ingrese un numero (ingrese 0 para terminar): "))
    if number!=0:
        minimo=number
        list_number.append(number)
travel_list(list_number,maximo,minimo)"""

# Ejercicio 8

"""def funcion8(a):
    area = int(math.pi * (a ** 2))
    perimeter = int(2 * math.pi * a)
    return (f"El área es: {area} y el perimetro {perimeter}.")

number = 0
while number == 0 or number<0:
    number = float(input("Ingrese el radio de la circunferencia: "))
print(funcion8(number))"""


# Ejercicio 9

"""def login(name,password,tryes,maxtryes):
    if tryes != maxtryes:
        if name == "usuario1" and password == "asdasd":
            return True
        else:
            return False
    else:
        return"Se agotaron el número de intentos"
        

attempts = 0
while attempts <100:
    
    user = input("Ingresa el usuario: ")
    passw = input("Ingresa la contraseña: ")
    
    if login(user,passw,attempts,2) == True:
        print("Bienvenido")
        break
    
    elif login(user,passw,attempts,2) == "Se agotaron el número de intentos"  :
        print("Se agotaron el número de intentos")
        break
    
    else:
        print("Datos no válidos, inténtelo de nuevo")
        
    attempts+=1"""


# Ejercicio 10

"""def funcion10(diccionary):
    pryce_of_things = list(diccionary.keys())
    off = list(diccionary.values())
    a = 0
    total = 0
    while a< len(pryce_of_things):
        total =total + pryce_of_things[a] -(pryce_of_things[a]*(off[a]/100))
        a+=1
    return total

dicc_shop = {}
aux = True
while aux== True:
    
    key =float(input("Ingrese el valor de un producto, o 0 para terminar: "))
    while key < 0:
        key = float(input("El valor del producto no puede ser negativo, ingrese un número positivo: "))
        
    if key == 0:
        break
    
    value_of_key = float(input(f"Ingrese el porcentaje de descuento del producto con valor {key}: "))
    
    while value_of_key< 0:
        value_of_key = float(input(f"El porcentaje de descuento no puede ser menor a 0, ingrese un descuento válido para el producto con precio {key}: "))
        
    dicc_shop[key] = value_of_key

print(f"Lo que tiene que pagar es: {funcion10(dicc_shop)}")"""


# Ejercicio 11

"""def funcion11_2(list,funtion):
    aux=0
    list_return = []
    while aux < len(list):
        list[aux] = funtion(list[aux])
        list_return . append(list[aux])
        aux+=1
        
    return (list_return)
def funcion11_lower(b):
    return (b.lower())
def funcion11_title(c):
    return(c.title())
def funcion11_upper(a):
        return(a.upper())

option =1
list_word =[]
while option != "0":
    word = input("Ingrese oracion al azar, si no desea agregar más oraciones ingrese 0(cero): ")
    if word == "0": 
        break
    else: 
        list_word.append(word)
        
option2 = 0
while option2!= "1" and option2 !="2" and option2 != "3":
    option2 = input("Que desea hacer con las oraciones? 1) Ponerlas todas a mayusculas  2) Ponerlas en minúsculas 3)Ponerla solamente la primera en mayúscula: ")
if option2 == "1": 
    print(funcion11_2(list_word,funcion11_upper))
elif option2 =="2":
    print(funcion11_2(list_word,funcion11_lower))
else:
    print(funcion11_2(list_word,funcion11_title))"""

# Ejercicio 12
"""word = input("Ingrese una frase: ")

def diccionario_frases():
    diccionario = word.split()
    #long = len(diccionario)
    return diccionario

def longitud_word():
    long = len(word) - word.count(" ")
    return long

print("Su diccionario es: ",diccionario_frases())
print("La longitud de la frase es de: ",longitud_word())"""

# Ejercicio 13
'''13.Escribir una función que calcule el módulo de un vector.'''
"""def module(v):

    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''

    return sum([x ** 2 for x in v]) ** 0.5

print(module((5, 9)))
print(module((6, 7, 8)))"""

# Ejercicio 14
'''14.Requerir al usuario que ingrese un número entero e informar si es primo o no,
utilizando una función booleana que lo decida.'''

'''
def cousin(num):
    for i in range(2,num):
        if num%i==0:           
            return False
    return True

number=int(input("Por favor, ingrese un numero entero:  "))
if cousin(number):
    print("Es primo")
else:
    print("No es primo")
'''

# Ejercicio 15
'''15.Escribir un programa que pida números al usuario,  motrar el factorial de cada uno y, al finalizar, 
la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

counter_global = 0

def factorial(number):
    if(number == 0):
        return 1
    elif(number == 1):
        return 1
    else:
        return number * factorial(number-1)
    
def counter():
    global counter_global
    counter_global += 1
    return counter_global


num = int(input("Ingrese un número o -1 para salir: "))

while(num != -1):
    counter()
    print(f"El factorial de ese número es: {factorial(num)}")

    num = int(input("Ingrese otro número o cero para salir: "))

    if(num == -1):
        break

print(f"La cantidad de números que se factorizaron fue {counter_global}")'''


# Ejercicio 16
"""def frecuency_number(number):
    number_list = list(str(number))
    counter = 0

    digit_selected = input("Ingrese un número del 0 al 9: ")

    for i in range(len(number_list)):
        if(number_list[i] == digit_selected):
            counter += 1

    return counter

number = int(input("Ingrese un número: "))
result = frecuency_number(number)

print(f"La cantidad de números que se repite el digito es: {result}")"""


# Ejercicio 17

"""global_list = []

def prime_number(number):
    aux = 1
    counter = 0
    while(aux <= number):
        if(number % aux == 0):
            counter += 1
        aux += 1

    if(counter > 2):
        return 1
    else:
        return 0
    

def sum_digits(number):
    sumatory = 0

    while (number > 0):
        aux = number % 10
        number = number // 10
        sumatory += aux
    
    return sumatory

def frecuency_number(number):
    number_list = list(str(number))
    counter = 0

    digit_selected = input("Ingrese un número del 0 al 9: ")

    for i in range(len(number_list)):
        if(number_list[i] == digit_selected):
            counter += 1

    return counter

def factorial_max_number():
    aux = 0
    for i in range(len(global_list)):
        if(aux <= global_list[i]):
            aux = global_list[i]

    return factorial(aux)

def factorial(number):
    if(number == 0):
        return 1
    elif(number == 1):
        return 1
    else:
        return number * factorial(number-1)
    
num = int(input("Ingrese un número no primo: "))


while(prime_number(num) != 0):
    result = frecuency_number(num)

    print(f"La sumatoria de sus digitos es: {sum_digits(num)}")
    print(f"La cantidad de números que se repite el digito es: {result}")

    global_list.append(num)
    num = int(input("Ingrese otro número no primo: "))

print(f"El factorial del número mas grande es: {factorial_max_number()}")"""
