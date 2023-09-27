from function import ahorcado
import random
list_number=[]
number=random.randint(0,10)
count=0
options=input("Desea jugar? Si/No: ").lower()
while count != 10 and options!="no":
    #Bucle while para que no se repitan los numeros 
    while number in list_number:
        number=random.randint(0,10)
    list_number.append(number)
    ahorcado(number)
    count+=1
    if count!=10:
        options=input("Desea seguir jugando? Si/No: ").lower()

if count==10:
    print("Ya jugaste con todas las palabras!")
elif count==0:
    print("No has jugado")
else:
    print("Gracias por jugar!")