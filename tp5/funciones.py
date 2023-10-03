def DNI(dni):
    dni_str = str(dni)
    if len(dni) >=7 and len(dni)<=8:
        if dni.isdigit():
            return True
        return False
    else:
        return False
    
def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()
    if palabras:
        return len(palabras[-1])
    else:
        return 0

def name(name,last_name,dni):
    name_str = name.split()
    if len(name_str) == 1:  
        name1 = name_str[0]
        full_name = name1 + " "
    elif len(name_str) == 2:    
        name1 = name_str[0]
        name2 = name_str[1]
        full_name = name1 + " " + name2 + " "
    else:
        print("Ingreso un dato incorrecto!")
    cant_last_name = len(last_name)
    full_name += last_name
    DNI(dni)
    if DNI(dni) == True:
        if len(dni) == 7:
            id = int(dni) // 10000
        else:
            id = int(dni) // 100000 
    name_id = name1+ str(cant_last_name) + str(id)
    print(f"#Nombre: {full_name}")
    print(f"#ID -> {name_id}")
    
    
def multiplo(num1,num2):
    if num1 % num2 == 0:
        print(f"{num1} es multiplo de {num2}")
    else:
        print(f"{num1} ni es multiplo de {num2}")