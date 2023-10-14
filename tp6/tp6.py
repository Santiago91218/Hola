import funciones
#Ejercicio 1
"""list_number=[]
while True:
    number=int(input("Ingrese un numero(ingrese 0 para terminar): "))
    if number==0:
        break
    else:
        list_number.append(number)
print(list_number)"""

#Ejercicio 2
"""funciones.delet_number(list_number)"""

#Ejercicio 3
"""print(f"La suma de todos los numeros de la lista es: {funciones.sum_numbers(list_number)}")"""

#Ejercicio 4
"""print(funciones.num_minors(list_number))"""

#Ejercicio 5
"""len_list = int(input("Ingrese el tamaño de la lista: "))
list = funciones.fill_list(len_list)

counter = 0
j = 0

list_tuple = []

for i in range(len(list)):
    aux_position = list[i]

    if(aux_position == list[i]):     
        for i in list:
            if(aux_position == i):
                counter += 1

    aux_tuple = (aux_position, counter)

    if (aux_tuple not in list_tuple):
        list_tuple.append(aux_tuple)
    counter = 0

print(f"El array es: {list}")  
print(f"El array de tuplas es: {list_tuple}")"""
#Ejercicio 6
"""aux_bool_secondary = True
aux_bool_primary = True

list_name_secondary = []
list_name_primary = []

while(aux_bool_secondary == True):
    insert_name = input("Ingrese el nombre del alumno de la secundaria o 'x' para salir: ").strip()

    if(insert_name == "X" or insert_name == "x"):
        break

    list_name_secondary.append(insert_name.title())

while(aux_bool_primary == True):
    insert_name = input("Ingrese el nombre del alumno de la primaria o 'x' para salir: ").strip()

    if(insert_name == "X" or insert_name == "x"):
        break

    list_name_primary.append(insert_name.title())

funciones.show_names(list_name_primary, list_name_secondary)
funciones.show_names_repeted_list(list_name_primary, list_name_secondary)
funciones.show_names_repeted_list_primary(list_name_primary, list_name_secondary)"""

#Ejercicio 7
"""num_strings = 0
character_counts = {}

while num_strings < 5:
    string_word = (input("Ingrese una frase: ").strip()).lower()
    num_strings += 1

    for char in string_word:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

for char, count in character_counts.items():
    print(f"'{char}':{count}")"""

#Ejercicio 8
"""print(funciones.final_score(funciones.teams_result()))"""
#Ejercicio 9
"""print(funciones.game_memo(funciones.make_memo()))"""
#Ejercicio 10 
"""matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz ")
for row in matrix:
    row_str = " ".join(map(str, row))
    print(row_str)

print(funciones.matrix_inDiagonal(matrix))"""

#Ejercicio 11
"""dict_coins={"Euro":"€", "Dollar":"$", "Yen":"¥"}
simbol=""
coin=input("Que divisa necesita: ").title()
for i in dict_coins.keys():
    if i==coin:
        simbol=dict_coins[i]
if simbol!="":
    print(f"La moneda {coin} utiliza este simbolo {simbol}")
else:
    print(f"La moneda {coin} no esta disponible")"""

#Ejercicio 12
"""name=input("Ingrese su nombre: ")
years=int(input("Ingrese su edad: "))
address=input("Igrese su domicilio: ")
phone=input("Ingrese su numero de telefono: ")

data_dictionary={"Nombre": name, "Edad":years, "Direccion":address, "Telefono":phone}

print(f"{data_dictionary['Nombre']} tiene {data_dictionary['Edad']} años, vive en {data_dictionary['Direccion']} y su numero de telefono es {data_dictionary['Telefono']}")"""

#Ejercicio 13
"""fruit_dictionary={"Banana": 150, "Manzana":95, "Pera":70, "Durazno":120, "Naranja":110, "Mandarina":85}

fruit=input("Que fruta va a querer?: ").title()
kilos=int(input(f"Cuantos kilos de {fruit} va a querer?: "))

if fruit in fruit_dictionary:
    price_kilo=fruit_dictionary[fruit]
    price_tot=price_kilo*kilos
    print(f"El precio de {kilos} kilo/s de {fruit} es de: {price_tot}")
else:
    print(f"La fruta {fruit} no esta disponible ")"""