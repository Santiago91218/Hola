#Ejercicio 1 en Ingles 
"""x=0
while x<=30:
    x+=1
    if x==15:
        print("Se rompio la ejecucion del bucle cuando x valia: ",x)
        break       
    elif x==4 or x==6 or x==10:
        print("Se salto el valor de ",x)
    else:
        print(x)"""

#Ejercicio 2
"""word=input("Ingrese una palabra: ")
while word != " ": 
    print (word.upper())
    word=input("Ingrese una palabra: ")"""

#Ejercicio 3
"""binnacle=0
operation=input("Ingrese una operacion: ").upper()
while operation!=" ":
    operation=operation.split(" ")
    operation[1]=float(operation[1])
    if operation[0]=="D":
        binnacle+=operation[1]
    elif operation[0]=="R":
        binnacle-=operation[1]
    operation=input("Ingrese una operacion: ").upper()
print("La bitacora es: ", binnacle)"""

#Ejercicio 4
"""prime_numbers=0
number_entered=1
while True:
    number_entered=int(input("Ingrese un numero: "))
    if number_entered==0:
        break
    dividers=0
    aux=1
    while aux<=number_entered:
        if number_entered%aux==0:
            dividers+=1
        aux += 1
    if dividers==2:
        prime_numbers+=1
print(f"La cantidad de numeros primos ingresados fueron: {prime_numbers}")"""

#Ejercicio 5
"""one_year=int(input("Ingrese un año: "))
two_year=int(input("Ingrese un año: "))
for leap_years in range(one_year,two_year,1):
    if leap_years%4==0  or (leap_years%100==0 and leap_years%400==0) and leap_years%10==0:
        print(leap_years)"""

#Ejercicio 6
"""for i in range(1,21):
    if i%2!=0:
        continue
    else:
        print(i)"""

#Ejercicio 7
"""list_numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
verification=False
search_number=int(input("Ingrese el numero que quiere encontar: "))
for i in range(26):
    if search_number==list_numbers[i]:
        verification=True
        break
if verification==True:
    print(f"El numero {search_number} se enceuntra en la lista")
else:
    print(f"El numero {search_number} no se enceuntra en la lista")"""

#Ejercicio 8
"""option_one="Usted ha elegido la opcion 1"
option_two="Usted ha elegido la opcion 2"
option_theree="Usted ha elegido la opcion 3"
print("Opciones Disponibles: 1,2 o 3")
select_option=1
while select_option!=0:
    select_option=int(input("Eliga una opcion: "))
    if select_option==0:
        break
    elif select_option==1:
        print(option_one)
    elif select_option==2:
        print(option_two)
    elif select_option==3:
        print(option_theree)
    else:
        print("Opcion invalida,seleccione otra")"""