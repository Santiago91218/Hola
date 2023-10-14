import random
#Funcion ejercicio 2
def delet_number(numeros):
    condition=False
    num=int(input("Ingrese un numero el numero que quiere eliminar: "))
    for i in numeros:
        if i==num:
            numeros.remove(i)
            condition=True
        else:
            condition=False
    if condition==True:        
        print(f"Se elimino el numero {num} de la lista")
    else:
        print("No se encontro el numero en la lista") 

#Funcion ejercicio 3
def sum_numbers(numeros):
    sum=0
    for i in numeros:
        sum+=i
    return sum

#Funcion ejercicio 4
def num_minors(numeros):
    list_minors=[]
    num=int(input("Ingrese un numero: "))
    for i in numeros:
        if i<num:
            list_minors.append(i)
    return f"Los elemntos de la lista menores a {num} son: {list_minors}"

#Funcion ejercicio 5
def fill_list(list_len):

    list = []

    for i in range(list_len):
        list.append(random.randint(0, 10))

    return list

#Funciones ejercicio 6
def show_names(list_primary, list_secondary):
    list_aux_primary = []
    list_aux_secondary = []

    for name in list_primary:
        if name not in list_aux_primary:
            list_aux_primary.append(name)
    
    for name in list_secondary:
        if name not in list_aux_secondary:
            list_aux_secondary.append(name)

    print(f" Los nombres sin repetir de la primaria son: {list_aux_primary}")
    print(f" Los nombres sin repetir de la secundaria son: {list_aux_secondary}")

def show_names_repeted_list(list_primary, list_secondary):
    list_aux = []
    list_name_no_repeted = []

    for name in list_primary:
        for name in list_secondary:
            if name in list_primary and name in list_secondary:
                list_aux.append(name)

    for name in list_aux:
        if name not in list_name_no_repeted:
            list_name_no_repeted.append(name)

    print(f" Los nombres que se repiten en ambas listas son {list_name_no_repeted}")

def show_names_repeted_list_primary(list_primary, list_secondary):
    list_name_no_repeted = []

    for name in list_primary:
        if name not in list_secondary and name not in list_name_no_repeted:
            list_name_no_repeted.append(name)

    print(f"Los nombres en nivel primario que no se repiten en los de nivel secundario: {list_name_no_repeted}")

#Funciones ejercicio 8
def final_score(matri):
    i = 0
    n = 0
    o = 0
    r = 0
    while i<4:
        goals_favor = 0
        goals_against = 0
        won = 0
        lost = 0
        tie = 0
        points = 0
        n = 0
        o = 0
        while o <4:
            if matri[i][n] > matri[o][r] and i != n:
                won+=1
                goals_favor+=matri[i][n]
                goals_against += matri[o][r]
                points +=3
            elif matri[i][n] < matri[o][r] and i != n:
                lost +=1
                goals_favor+=matri[i][n]
                goals_against += matri[o][r]
                points+=0
            elif matri[i][n] == matri[o][r] and i != n:
                tie+=1
                goals_favor+=matri[i][n]
                goals_against += matri[o][r]
                points+=1
            o+=1
            n+=1
        if i == 0:
            matrix_team1 = [[f"Ha ganado {won} partidos",f"Ha perdido {lost} partidos",f"Ha empatado {tie}"],[f"Tiene una diferencia de goles de:{goals_favor-goals_against} "],[points]]
        elif i == 1:
            matrix_team2 = [[f"Ha ganado {won} partidos",f"Ha perdido {lost} partidos",f"Ha empatado {tie}"],[f"Tiene una diferencia de goles de:{goals_favor-goals_against} "],[points]]
        elif i == 2:
            matrix_team3 = [[f"Ha ganado {won} partidos",f"Ha perdido {lost} partidos",f"Ha empatado {tie}"],[f"Tiene una diferencia de goles de:{goals_favor-goals_against} "],[points]]
        elif i == 3:
            matrix_team4 = [[f"Ha ganado {won} partidos",f"Ha perdido {lost} partidos",f"Ha empatado {tie}"],[f"Tiene una diferencia de goles de:{goals_favor-goals_against} "],[points]]
        r+=1
        i+=1
    print(f"""Equipo 1: {matrix_team1}
Equipo 2: {matrix_team2}
Equipo 3: {matrix_team3}
Equipo 4: {matrix_team4}""")
    tabla_posicion = {
        "Equipo 1": matrix_team1[2][0],"Equipo 2": matrix_team2[2][0],"Equipo 3": matrix_team3[2][0],"Equipo 4": matrix_team4[2][0]}

    for m,n in tabla_posicion.items():
        print (f"{m}     Puntos: {n}", end= " ")
        print(" ")

def teams_result():
    matrix_result = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    i = 0
    n = 0
    while i <4:
        n = 0
        while n<4:
            if i+1 != n+1:
                matrix_result[i][n] = int(input(f"Cuantos goles hizo el equipo {i+1} contra el equipo {n+1} : "))
            n+=1
        i+=1
    return(matrix_result)

#Funciones ejercicio 9
def game_memo(matrix_memo):
    matriz_encript = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    matriz_aux1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    while matriz_encript != matrix_memo:
            
        matriz_aux1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        fil_option = input("Ingrese el número de la fila que desea (1 al 4): ")
        colum_option = input("Ingrese el número de la columna que desea (1 al 4): ")
        
        while (fil_option != "1" and fil_option != "4" and fil_option != "2" and fil_option != "3" ) or (colum_option != "4" and colum_option != "1" and colum_option != "2" and colum_option != "3"):
            fil_option = input("Ingrese el número de la fila que sea correcto (0 al 3): ")
            colum_option = input("Ingrese el número de la columna que sea correcto (0 al 3): ")
    
            
        fil_option = int(fil_option) -1
        colum_option = int(colum_option) -1
        value_option1 = 0
            
        value_option1 = matrix_memo[fil_option][colum_option]
        
        matriz_aux1[fil_option][colum_option] = value_option1

        for i in matriz_aux1:
            for n in i:
                print(n, end= "     ")
            print(" ")
        
        fil_option2 = input("Ingrese el número de la fila que desea (1 al 4): ")
        colum_option2 = input("Ingrese el número de la columna que desea (1 al 4): ")
        
        while(fil_option2 != "4" and fil_option2 != "1" and fil_option2 != "2" and fil_option2 != "3" ) or (colum_option2 != "4" and colum_option2 != "1" and colum_option2 != "2" and colum_option2 != "3"):
        
            fil_option2 = input("Ingrese el número de la fila que sea correcto (0 al 3): ")
            colum_option2 = input("Ingrese el número de la columna que sea correcto (0 al 3): ")
    
        fil_option2 = int(fil_option2) -1
        colum_option2 = int(colum_option2) -1
        value_option2 = 0
        value_option2 = matrix_memo[fil_option2][colum_option2] 
        matriz_aux1[fil_option2][colum_option2] = value_option2
        for i in matriz_aux1:
            for n in i:
                print(n, end= "     ")
            print(" ")

        if value_option1 == value_option2:
            print("Conseguiste un par")
            matriz_encript[fil_option][colum_option] = value_option1
            matriz_encript[fil_option2][colum_option2] = value_option2
        elif value_option2 != value_option1:
            print("No coinciden las cartas")
        
        for i in matriz_encript:
            for n in i:
                print(n, end = "     ")
            print(" ")
    
    return "Felicidadeees, ganaste el juego!!!!!!" 

def concurrence_memo(matriz, num):
    count1 = 0
    for i in matriz:
        for n in i:
            if n == num:
                count1+=1
    return count1

def make_memo():
    memo =[[],[],[],[]]
    while concurrence_memo(memo,1) != 2:
        num_random=random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(1)
            
    while concurrence_memo(memo,2) != 2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(2)
            
    while concurrence_memo(memo,3)!=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(3)
            
    while concurrence_memo(memo,4) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(4)
            
    while concurrence_memo(memo,5) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(5)
            
    while concurrence_memo(memo,6) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(6)
            
    while concurrence_memo(memo,7) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(7)
            
    while concurrence_memo(memo,8) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(8)
    return memo

#Funcion ejercicio 10
def matrix_inDiagonal(matrixx):
    main_diagonal=[matrixx[i][i] for i in range(len(matrixx))]
    reverse_diagonal=[matrixx[i][len(matrixx) - 1 - i] for i in range(len(matrixx))]
    print(f"La diagonal principal es: {main_diagonal}")
    print(f"La diagonal inversa es: {reverse_diagonal}")