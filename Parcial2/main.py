import Funciones
while True:
    #Pedimos al usuario que eliga una opcion
    option=input("Desea ingresar un ADN? (ingrese el numero de la opcion): \n"
                    "1)Si \n"
                    "2)No \n")
    if option=="1":
        #Incializamos la matriz siempre que se eliga la opcion 1
        matrix_dna=[]
        while True:
            print("--------------------------------")
            print("Condiciones que debe tener el ADN ingresado: \n"
                    "-Letras Permitidas: A,T,C,G                    \n"
                    "-Ingresar 6 letras                             \n")
            
            #Le pedimos al usuario que ingrese el ADN
            enter_dna= input("Ingrese el ADN: ").upper()
            #Llamamos a la funcion para que verifique si el ADN ingresado es valido
            Funciones.complete_dna_matrix(matrix_dna,enter_dna)

            #Condicion de salida si la matriz ya es de 6x6
            if len(matrix_dna) == 6: 
                #Llamamos a la funcion para ver si el ADN es mutante o no
                print(Funciones.is_mutant(matrix_dna))
                break
    elif option=="2":
        #Mostamos por pantalla mensaje de finalizacion del programa
        print("Saliendo...")
        break
    else:
        #Mensaje por si la opcion ingresada no es valida
        print("Opcion incorrecta.Intentelo devuelta")

"""#True
matrix_one=["ATTCAG", "CATTAT", "GCACAC", "GGCAAG", "GGCCCG", "AAATTT"]
print(Funciones.is_mutant(matrix_one))

#False
matrix_two=["ACCCGA","TTGACA","AAGCGA","TCGAGA","GACGTT","CACATT"]
print(Funciones.is_mutant(matrix_two))"""