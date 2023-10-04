import Funciones
#Ejercicio 1
"""list_passengers=[("Santiago Comeglio", 46236362,"Cordoba"),("Ivan Gonzales", 45679569,"Mendoza")]
list_country=[("Cordoba","Argentina"),("Mendoza","Argentina")]
numMenu=""

while(numMenu != "7"):
    print("Menú de opciones: \n" 
        "1. Agregar pasajero \n"
        "2. Agregar ciudades \n"
        "3. Ingresar D.N.I de pasajero para ver a que ciudad viaja\n"
        "4. Nombre de ciudad para ver cuantos pasajeros viajan \n"
        "5. Ingresar D.N.I de pasajero para ver a que pais viaja\n"
        "6. Nombre del pais para ver cuantos pasajeros viajan  \n"
        "7. Salir del Programa \n")
    numMenu = input("Ingrese una opción: ")
    
    if numMenu=="1":
        Funciones.add_passengers(list_passengers)
    elif numMenu=="2":
        Funciones.add_countrys(list_country)
    elif numMenu=="3":
        Funciones.city_togo(list_passengers)
    elif numMenu=="4":
        Funciones.tot_tavelerscity(list_passengers)
    elif numMenu=="5":
        Funciones.country_togo(list_passengers,list_country)
    elif numMenu=="6":
        Funciones.tot_tavelerscountry(list_passengers,list_country)
    elif numMenu=="7":
        print("Saliendo...")
        print("----------------------------------")
    else:
        print("La opcion ingesada no es valida.Intentelo de vuelta")
        break"""



#Ejercicio 2
"""list_purchase_data=[("Pedro Jimenez", 12, 1250,"Calle Roca - 987"), ("Miguel Vega", 9, 999.99,"Calle Lima - 741"),
                    ("Pedro Jimenez", 15, 700,"Calle Roca - 987"), ("Alberto Rodriguez", 9, 400,"Calle Maderos - 456")]
print(Funciones.client_homes(list_purchase_data))"""



#Ejercicio 3
"""partners={ 
    1: {"Nombre": "Amanda Núñez", "Ingreso": "17/03/2009", "Cuota_al_dia": "Si"},
    2: {"Nombre": "Bárbara Molina", "Ingreso": "17/03/2009", "Cuota_al_dia": "No"},
    3: {"Nombre": "Lautaro Campos", "Ingreso": "17/03/2009", "Cuota_al_dia": "Si"}
}
numMenu=""
while(numMenu != "6"):
    print("Menú de opciones: \n" 
        "1. Agregar Socios \n"
        "2. Cantidad de Socios \n"
        "3. Numero de Socio y ver si ha pagado las cuotas adeudadas \n"
        "4. Eliminar Socio\n"
        "5. Listado de Socios \n"
        "6. Salir del Programa \n")
    print("----------------------------------")
    numMenu = input("Ingrese una opción: ")

    if numMenu=="1":
        Funciones.add_partner(partners)
    elif numMenu=="2":
        Funciones.number_of_partners(partners)
    elif numMenu=="3":
        Funciones.membresy_partner(partners)
    elif numMenu=="4":
        Funciones.remove_partner(partners)
    elif numMenu=="5":
        Funciones.show_partners(partners)
    elif numMenu=="6":
        print("Saliendo...")
    else:
        print("Opcion Invalida.Intentelo de vuelta.")
        break"""