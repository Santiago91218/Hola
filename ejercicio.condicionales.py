
lista=input("Ingrese la fecha actual en formato (dia,DD/MM): ")
lista=lista.split(",")
dia_sem=lista[0].lower()
lista2=lista[1]
lista2=lista2.split("/")
dia=int(lista2[0])
mes=int(lista2[1])

if (dia_sem !="lunes" and dia_sem !="martes" and dia_sem !="miercoles" and dia_sem !="jueves" and dia_sem !="viernes"):
    print("ERROR")
elif dia<1 or dia>31:
    print("ERROR")
elif mes<1 or mes>12:
    print("ERROR")
else:
    if dia_sem=="lunes" or dia_sem=="martes" or dia_sem=="miercoles":
        examenes=input("Se tomaron examenes? SI/NO: ").lower()
        if examenes=="si":
            alum_aprobados=int(input("Ingrese cuantos alumnos aprobaron: "))
            alum_desaprobados=int(input("Ingrese cuantos alumnos desaprobaron: "))
            total_alumnos=alum_aprobados+alum_desaprobados
            promedio_aprobados=(alum_aprobados/total_alumnos)*100
            print(f"Porcentaje alumnos aprobados: {promedio_aprobados}")
        else:
            print("No se tomaron examenes")
    elif dia_sem=="jueves":
            print("Dia de Practicas habladas")
            asistencia=float(input("Ingrese el porcentaje de asistencia: "))
            if asistencia>50 :
                    print("Asistio la mayoria")
            else:
                    print("No asistio la mayoria")
    elif dia_sem=="viernes":
        print("Ingles para viajeros")
        if (dia==1 and mes==1) or (dia==1 and mes==7):
            print("Comienzo de nuevo ciclo")
            alums_nuevociclo=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel=float(input("Ingrese el arancel por cada alumno: "))
            ingreso_total=arancel*alums_nuevociclo
            print(f"El ingreso total es: {ingreso_total}")
