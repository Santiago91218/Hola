import Funciones
#Ejercicio 1
"""list_number=[]
while True:
    number=int(input("Ingrese numeros (ingrese 0 para terminar): "))
    if number==0:
        break
    else:
        list_number.append(number)
print(f"Lista Ingresada: {list_number}")
print(f"Lista Ordenada: {Funciones.Bubble_Sort(list_number)}")"""

#Ejercicio 2
"""list_word=[]
while True:
    word=input("Ingrese palabras (ingrese 0 para terminar): ")
    if word=="0":
        break
    else:
        list_word.append(word)
print(f"Lista Ingresada: {list_word}")
print(f"Lista Ordenada Alfabeticamente: {Funciones.Selection_Sort(list_word)}")"""

#Ejercicio 3
"""books=[
    {
        "titulo": "Matar un ruiseñor",
        "autor": "Harper Lee",
        "año_publicacion": 1960
    },
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año_publicacion": 1967
    },
    {
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "año_publicacion": 1997
    }
]
while True:
    option=input("Como desea ordenar los libros? (ingrese el numero de la opcion) \n"
                "1) Titulo                       \n"
                "2) Autor                        \n"
                "3) Año de publicacion           \n"
                "--------------------------------\n")
    if option=="1":
        Funciones.title_Order(books)
        print("Titulos Ordenados Alfabeticamente: ")
        for book in books:
            print(book["titulo"])
        break
    elif option=="2":
        Funciones.author_Order(books)
        print("Autores Ordenados Alfabeticamente: ")
        for book in books:
            print(book["autor"])
        break
    elif option=="3":
        Funciones.year_Order(books)
        print("Año de Publicacion Ordenado: ")
        for book in books:
            print(book["año_publicacion"])
        break
    else:
        print("La opcion ingresada no es valida")"""

#Ejercicio 4
"""list_words=[]
while True:
    word=input("Ingrese palabras (ingrese 0 para terminar): ")
    if word=="0":
        break
    else:
        list_words.append(word)
print(f"Lista Ingresada: {list_words}")
print(f"Lista Ordenada Segun el tamaño de las palabras:\n"
    f"{Funciones.Insert_Sort(list_words)} \n")"""

#Ejercicio 5
"""list_number=[]
while True:
    number=int(input("Ingrese numeros (ingrese 0 para terminar): "))
    if number==0:
        break
    else:
        list_number.append(number)
print(f"Lista Ingresada: {list_number}")
print(f"Lista Ordenada en forma Descendente: {Funciones.Bubble_Sort_Des(list_number)}")"""

#Ejercicio 6
"""list_number=[]
while True:
    number=int(input("Ingrese numeros (ingrese 0 para terminar): "))
    if number==0:
        break
    else:
        list_number.append(number)
print(f"Lista Ingresada: {list_number}")
print(f"Lista Ordenada en forma Ascendente: {Funciones.Count_Order(list_number)}")"""

#Ejercicio 7
"""list_elements=["Gallina","Aguila",12,18,"Perro",9,"Paloma",0]
Funciones.order_Elements(list_elements)"""

#Ejercicio 8
"""list_number=[]
while True:
    number=int(input("Ingrese numeros (ingrese 0 para terminar): "))
    if number==0:
        break
    else:
        list_number.append(number)
print(f"Lista Ingresada: {list_number}")
print(f"Lista Ordenada: {Funciones.Merge_Sort(list_number)}")"""