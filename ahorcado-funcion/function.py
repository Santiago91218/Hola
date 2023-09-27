import random
def ahorcado(num):
    #Declaracion de variables
    list_word=["microondas","mesa","heladera","computadora","televisor","avion","motocicleta","camioneta","esternocleidomastoideo","fanfarron","farmacia"]
    word=list_word[num]
    secret_word=list(len(word)*"_")
    attempts=5
    list_letter=[]

    while attempts > 0 and "_" in secret_word:
        #Mostramos las letras ingresadas
        print(f"Letras ingresadas: {list_letter}")
        #Mostramos el estado actual de la palabra secreta
        for i in secret_word:
            print(i, end=" ")
        print(" ")
        #Le pedimos al usuario que ingrese una letra
        letter = input("Ingrese una letra: ").lower()
        count=0
        #Condicion para ver si la letra esta en la palabra y no esta en la palabra secreta
        if letter in word and letter not in secret_word:
            print("Adivinaste una letra!!")
            list_letter.append(letter)
            #Comparamos la letra ingresada con la palabra 
            for i in word:
                if letter==i:
                    #Remplazamos la letra en la palabra secreta
                    secret_word[count]=letter
                count+=1
        #Condicion para ver si la letra ya fue ingresada
        elif letter in secret_word:
            attempts-=1
            print("Esa letra ya esta agregada")
            #Mostramos los intentos restantes
            print(f"Te quedan {attempts} intentos")
        else:
            list_letter.append(letter)
            attempts-=1
            #Mostramos los intentos restantes
            print(f"Fallaste.Te quedan {attempts} intentos")

    if "_" not in secret_word :
        print(f"Ganaste!!.La palabra era {word}")
    else:
        print(f"Perdiste.La palabra era {word}")