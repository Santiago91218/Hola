from Clases import Diary
#Ejercicio 1
"""person1 = Persona()
enter_name=input("Ingrese su nombre: ")
person1.name= enter_name
enter_dni=input("Ingrese su dni (sin puntos): ")
while len(enter_dni)<7 or len(enter_dni)>8:
    print("El dni debe ser valido.")
    enter_dni=input("Ingrese otra vez su dni(sin puntos): ")
person1.dni=enter_dni
enter_age=int(input("Ingrese su edad: "))
person1.age=enter_age

person1.Show()
print(person1.isOlder())"""

#Ejercicio 2
"""myAccount=Cuenta()
enter_owner=input("Ingrese el nombre del titular de la cuenta: ")
myAccount. headline=  enter_owner
op=" "
while op!="4":
    op=input("Eliga una opcion: 1)Mostrar datos 2)Depositar 3)Retirar 4)Salir ")
    if op=="1":
        myAccount.Show()
    elif op=="2":
        myAccount.Enter()
    elif op=="3":
        myAccount.Withdraw()
    elif op=="4":
        print("Saliendo...")
        break
    else:
        print("Opcion incorrecta")"""

#Ejercicio 
"""my_triangle=Triangle
side1 = float(input("Ingrese el valor del primer lado del triangulo: "))
side2 = float(input("Ingrese el valor del segundo lado del triangulo: "))
side3 = float(input("Ingrese el valor del tercer lado del triangulo: "))
    
my_triangle = Triangle(side1, side2, side3)
my_triangle.Show_data()"""

#Ejercicio 4
"""my_diary=Diary() 
op=" "
while op!="5":
    print("Menu de opciones  \n"
        "1.Añadir contacto      \n "
        "2.Lista de contactos   \n "
        "3.Buscar contacto      \n "
        "4.Editar contacto      \n "
        "5.Salir                \n ")
    op=input("Eliga una opcion: ")
    if op=="1":
        my_diary.Add_contact()
    elif op=="2":
        my_diary.Show_contact()
    elif op=="3":
        my_diary.Search_contacts()
    elif op=="4":
        my_diary.Edit_contacts()
    elif op=="5":
        print("Saliendo...")
        break
    else:
        print("Opcion incorrecta: ")"""