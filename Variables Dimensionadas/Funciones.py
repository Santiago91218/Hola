#Funciones Ejercicio 1
#Funcion para agregar pasajeros -Ejercicio 1
def add_passengers(list_psg):
    passengers=input("Ingrese los datos del pasajero con el siguiente formato (nombre,dni,destino): ").title()
    tupl_passengers=tuple(passengers.split(','))
    tupl_passengers = (tupl_passengers[0], int(tupl_passengers[1]), tupl_passengers[2])
    list_psg.append(tupl_passengers)
    print("Pasajero agregado!! \n",
        list_psg)
    print("----------------------------------")

#Funcion para agregar ciudades -Ejercicio 1
def add_countrys(list_ctry):
    country=input("Ingrese el nombre de la ciudad con el siguiente formato (ciudad,pais): ").title()
    tupl_ctry=tuple(country.split(','))
    list_ctry.append(tupl_ctry)
    print("Ciudad Agregada!! \n",
        list_ctry)
    print("----------------------------------")
    
#Funcion para ver a que ciudad viaja con su dni -Ejercicio 1
def city_togo(list_psg):
    dni_passenger=int(input("Ingrese el DNI del pasajero (sin puntos): "))
    condition=False
    for i in list_psg:
        if i[1]==dni_passenger:
            destination = i[2]
            condition=True
    if condition==True:
        print(f"El pasajero con DNI {dni_passenger} viaja a la ciudad de {destination}")
    else:
        print(f"No se encontro un pasajero con el DNI {dni_passenger} en la lista")
    print("----------------------------------")

#Funcion para ver cuantos pasajero viajan a una ciudad -Ejercicio 1
def tot_tavelerscity(list_psg):
    city=input("Ingrese el nombre de la ciudad: ").title()
    count=0
    for i in list_psg:
        if i[2] == city:
            count+=1
    if count > 0:
        print(f"La cantidad de pasajeros que viajan a {city} es: {count}")
    else:
        print(f"No se encontraron pasajeros que viajen a {city} en la lista")
    print("----------------------------------")

#Funcion para a que pais viaja con el DNI -Ejercicio 1
def country_togo(list_psg,list_ctry):
    dni_passenger=int(input("Ingrese el DNI del pasajero (sin puntos): "))
    condition=False
    for i in list_psg:
        if i[1] ==dni_passenger:
            city=i[2]
            for j,k in list_ctry:
                if j == city:
                    destination = k
                    condition=True
    if condition==True:
        print(f"El pasajero con DNI {dni_passenger} viaja a {destination}")
    else:
        print(f"No se encontro un pasajero con el DNI {dni_passenger} en la lista")
    print("----------------------------------")

#Funcion para ver cuantos pasajero viajan a un pais -Ejercicio 1
def tot_tavelerscountry(list_psg, list_ctry):
    country = input("Ingrese el nombre del país: ").title()
    count = 0
    for i in list_psg:
        city = i[2]
        for j,k in list_ctry:
            if j == city and k == country:
                count += 1
    if count > 0:
        print(f"La cantidad de pasajeros que viajan a {country} es: {count}")
    else:
        print(f"No se encontraron pasajeros que viajen a {country} en la lista")
    print("----------------------------------")

#Funcion Ejercicio 2
#Funcion para ver a que domicilio hay que enviar factura y que no se repitan 
def client_homes(list_purchase):
    homes=[]
    for i in list_purchase:
        home = i[3]
        if home not in homes:
            homes.append(home)
    return f"Se debe enviar Factura a los siguientes Domicilios: \n {homes}" 



#Funciones Ejercicio 3
#Funcion para agregar socio -Ejercicio 3
def add_partner(dic_partners):
    print("Ingrese los datos: ")
    number_partner = int(input('Ingrese el número del socio: '))
    name = input('Ingrese el nombre del socio: ')
    last_name = input('Ingrese el apellido del socio: ')
    admission_date = input('Ingrese la fecha de ingreso (dd/mm/aaaa): ')
    share = input('¿La cuota está al día? (Si/No): ').title() 
    print("----------------------------------")

    if admission_date=="13/03/2018":
        admission_date="14/03/2018"

    if number_partner in dic_partners:
        print("El número de socio ya existe. Use otra clave.")
    else:
        dic_partners[number_partner] = {
            "Nombre": name + " " + last_name,
            "Ingreso": admission_date,
            "Cuota_al_dia": share
        }
        print(f"El socio n°{number_partner} ha sido agregado con éxito.")
    print("----------------------------------")
    
#Funcion para mostrar todos los socios -Ejercicio 3
def show_partners(dic_partners):
    print(dic_partners)
    print("----------------------------------")


#Funcion para contar la cantidad de socios -Ejercicio 3
def number_of_partners(dic_partners):
    count=0
    for i in dic_partners:
        count+=1
    print(f"La cantidad de socios es: {count}")
    print("----------------------------------")


#Funcion para eliminar un socio -Ejercicio 3
def remove_partner(dic_partners):
    number_partner=int(input("Ingrese el numero del socio que quiere eliminar: "))
    del dic_partners[number_partner]
    print(f"Perfecto. Socio n°{number_partner} eliminado")
    print("----------------------------------")

#Funcion para registrar la cuota -Ejercicio 3
def membresy_partner(dic_partners):
    number_partner=int(input("Ingrese el numero del socio: "))
    if number_partner in dic_partners:
        if dic_partners[number_partner]["Cuota_al_dia"] == "Si":
            print(f"El socio n°{number_partner} ya tiene la cuota al dia")
        else:
            dic_partners[number_partner]["Cuota_al_dia"] = "Si"
            print(f"El socio n°{number_partner} ({dic_partners[number_partner]['Nombre']}) ha pagado todas las cuotas adeudadas")
    else:
        print(f"No se encontró un socio con el número {number_partner}")
    print("----------------------------------")