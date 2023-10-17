import random
#Ejercicio 1
def cage(time):
    option=random.randint(1,3)
    if option==1:
        return cage(time+3)
    elif option==2:
        return cage(time+5)
    elif option==3:
        return time+7
print(f"La rata tardo {cage(0)} minutos")

#Ejercicio 2
#Escriba una funcion recursiva para dar vuelta un numero entero Ej:123 --> 321
def f(n):
    s=str(n) #Convertimos el numero a String
    if len(s)<=1: #Condicion de salida si el numero es menor o igual a 1 digito
        return s
    return s[-1]+f(int(s[:-1])) #Aca se arma el numero final,se usa -1 porque devuelve el numero mas a la derecha
print(f(123))
