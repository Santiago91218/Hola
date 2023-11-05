#Funcion para saber si el ADN es mutante
def is_mutant(matrix):
    print(f"El ADN ingresado es: {matrix}")
    count = count_sequences(matrix)
    if  count >= 2:
        return True #Devolvemos True si es mutante
    else:
        return False #Devolvemos False si no es mutante

def count_sequences(matrix_dna):
    count_sequences_mutant=0
    #Juntamos todas las verticales,horizontales y diagonales en una sola lista
    list_dna = vertical(matrix_dna) + horizontal(matrix_dna)+ main_diagonals(matrix_dna)+reverse_diagonals(matrix_dna)
    #Convertir la matriz de ADN en un solo string para iterar mas facil
    dna_chain = ''.join(list_dna)

    #Contamos las secuencias mutantes
    for i in range(len(dna_chain) - 3): #-3 para que al menos cuatro caracteres se verifiquien en cada iteracion
        if dna_chain[i] == dna_chain[i + 1] == dna_chain[i + 2] == dna_chain[i + 3]:
            count_sequences_mutant += 1

    return count_sequences_mutant

def complete_dna_matrix(matrix,dna):
        if len(matrix) < 6:
            #Llamamos funcion para quitar espacio del String
            dna= quit_spaces(dna)
            #Llamamos a las dos funciones que verifican si el ADN es valido
            if validate_letter_dna(dna) and validate_size_dna(dna):
                print(f"ADN valido: {dna}")
                matrix.append(dna) #Si el ADN es valido lo añadimos a la matriz
            else:
                #Si el ADN no es valido, pedimos que lo ingrese nuevamente
                print("ADN invalido.Ingrese otro ADN")
            return

#Funcion para quitar espacios en el String ingresado
def quit_spaces(dna_spaces):
    letters = dna_spaces.split() 
    dna = "".join(letters)
    return dna

#Funcion para ver si las letras ingresadas en el String son validas
def validate_letter_dna(dna):
    condition = True
    for iter in dna:
        if iter not in "ATCG":
            condition = False
            break
    return condition

#Funcion para ver si el String tiene 6 letras
def validate_size_dna(dna):
    return len(dna) == 6

#Implementamos funcion para conseguir las diagonales principales
def main_diagonals(matrix):
    list_main_diagonals=[]
    for k in range(0,6):
        for i in range(0,6):
            if i== k: 
                list_main_diagonals.append(matrix[i][k])

    for i in range(0,5):
        list_main_diagonals.append(matrix[i][i+1])
    
    for i in range(0,4):
        list_main_diagonals.append(matrix[i][i+2])
        
    for i in range(1,6):
        list_main_diagonals.append(matrix[i][i-1])
        
    for i in range(2,6):
        list_main_diagonals.append(matrix[i][i-2])
    return list_main_diagonals

#Implementamos funcion para conseguir las diagonales inversas
def reverse_diagonals(matrix):
    list_reverse_diagonals=[]
    
    aux  = 5
    for i in range(0,6):
        sequence = ""
        sequence+=matrix[i][aux]
        list_reverse_diagonals.append(matrix[i][aux])
        aux-=1

    aux = 4
    for i in range(0,5):
        list_reverse_diagonals.append(matrix[i][aux])
        aux-=1

    aux = 3
    for i in range(0,4):
        list_reverse_diagonals.append(matrix[i][aux])
        aux-=1

    aux=5
    for i in range(1,6):
        list_reverse_diagonals.append(matrix[i][aux])
        aux-=1

    aux = 5
    for i in range(2,6):
        list_reverse_diagonals.append(matrix[i][aux])
        aux-=1

    return list_reverse_diagonals

#Implementamos funcion para conseguir las verticales de la martiz
def vertical(matrix):
    vertical=[]
    for j in range(0, 6):
        for i in range(0, 6):
            vertical.append(matrix[i][j]) 
    return vertical

#Implementamos funcion para conseguir las horizontales de la martiz
def horizontal(matrix):
    horizontal = []
    for i in range(0, 6):
        for j in range(0, 6):
            horizontal.append(matrix[i][j])
    return horizontal