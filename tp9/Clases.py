#Ejercicio 1
class Persona:
    
    def __init__(self):
        self.__name=None
        self.__age=0
        self.__dni=0

    #Getter
    @property 
    def name(self):
        return self.__name
    @property 
    def age(self):
        return self.__age
    @property 
    def dni(self):
        return self.__dni

    #Setter
    @name.setter 
    def name(self, new_name):
        self.__name = new_name

    @age.setter 
    def age(self, new_age):
        self.__age = new_age

    @dni.setter 
    def dni(self, new_dni):
        self.__dni = new_dni

    def Show(self):
        print(f"El nombre es: {self.__name}")
        print(f"La edad es: {self.__age}")
        print(f"El DNI es: {self.__dni}")

    def isOlder(self):
        if self.age>=18:
            return True
        else:
            return False

#Ejercicio 2
class Cuenta:
    def __init__(self):
        self.__headline= ""
        self.__amount=0.0

    #Getter
    @property 
    def  headline(self):
        return self.__headline
    
    @property 
    def amount(self):
        return self.__amount
    
    #Setter
    @ headline.setter 
    def  headline(self, new_headline):
        self.__headline = new_headline
    
    @amount.setter 
    def amount(self, new_amount):
        self.__amount = new_amount

    def Show(self):
        print(f"El titular de la cuenta es: {self.__headline}")
        print(f"La cantidad de la cuenta es: {self.__amount}")

    def Enter(self):
        cant=float(input("Ingrese la cantidad de dinero: "))
        if cant<=0:
            print("No se puede ingresar una cantidad negativa o igual a 0")
        else:
            print("Operacion realizada con exito!")
            self.__amount+=cant

    def Withdraw(self):
        ret=float(input("Ingrese el dinero que quiere retirar:"))
        if ret<=0:
            print("No se puede retirar una cantidad negativa o igual a 0")
        else:
            print("Operacion realizada con exito!")
            self.__amount-=ret
#Ejercicio 3 
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def longest_side(self):
        lados = [self.side1, self.side2, self.side3]
        long_sid = max(lados)
        return long_sid
    
    def determine_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilatero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Isosceles"
        else:
            return "Escaleno"
        
    def Show_data(self):
        side= self.longest_side()
        typ = self.determine_type()
        print(f"Lado mas largo: {side}")
        print(f"Tipo de triangulo: {typ}")

#Ejercicio 4
class Diary:
    def __init__(self):
        self.list_contacts=[]

    def Add_contact (self):
        enter_name=input("Ingrese el nombre del contacto: ").title()
        enter_phone=input("Ingrese el numero de telefono: ")
        enter_email=input("Ingrese el email: ")
        contac = {
            "Name": enter_name,
            "Phone": enter_phone,
            "Email": enter_email
        }
        self.list_contacts.append(contac)
        print("Contacto Añadido")

    def Show_contact(self):
        print("Lista de contactos")
        print("---------------------------------")
        for contact in self.list_contacts:
            print("Nombre: ", contact["Name"])
            print("Telefono: ", contact["Phone"])
            print("Email: ", contact["Email"])
            print("---------------------------------")


    def Search_contacts(self):
        aux=False
        search_name=input("Ingrese el nombre del contacto que quiere buscar: ").title()
        for contact in self.list_contacts:
            if contact["Name"]==search_name:
                print("---------------------------------")
                print("Los datos de ese contacto son: ")
                print("Nombre: ", contact["Name"])
                print("Telefono: ", contact["Phone"])
                print("Email: ", contact["Email"])
                aux=True

        if aux==False:
            print("No se encontro el contacto en la lista")


    def Edit_contacts(self):
        aux=False
        search_name=input("Ingrese el nombre del contacto que quiere editar: ").title()
        for contact in self.list_contacts:
            if contact["Name"]==search_name:
                print("Los datos de ese contacto son: ")
                print("Nombre: ", contact["Name"])
                print("Telefono: ", contact["Phone"])
                print("Email: ", contact["Email"])
                aux=True
                break

        if aux:
            edit_option = input("Que desea editar? 1)Nombre 2)Telefono 3)Email: ")
            if edit_option == "1":
                new_name = input("Ingrese el nuevo nombre: ").title()
                contact["Name"] = new_name
                print("Nombre actualizado.")
            elif edit_option == "2":
                new_phone = input("Ingrese el nuevo numero de telefono: ")
                contact["Phone"] = new_phone
                print("Telefono actualizado.")
            elif edit_option == "3":
                new_email = input("Ingrese el nuevo correo electronico: ")
                contact["Email"] = new_email
                print("Correo electronico actualizado.")
        else:
            print("No se encontro el contacto en la lista ")