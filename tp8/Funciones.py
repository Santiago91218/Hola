#Funcion Ejercicio 1
def digits_count(num):
    dig=0
    if len(str(num))==1:
        return 1
    else:
        return 1+digits_count(num//10)
    
#Funcion Ejercicio 2
def power(a,b):
    if a==1:
        return True
    elif a < 1 or a % b != 0:
        return False
    else:
        return power(a // b, b)
    
#Funcion Ejercicio 3
def position(a,b,pos=0):
    if pos == len(a):
        return []  

    if a.startswith(b, pos):
        return [pos] + position(a, b, pos + 1)
    else:
        return position(a, b, pos + 1)
    
#Funcion Ejercicio 4
def pair(num):
    if num == 0:
        return True  
    else:
        return odd(num - 1)

def odd(num):
    if num == 0:
        return False  
    else:
        return pair(num - 1)
    
#Funcion Ejercicio 5
def max_list_num(array, i, max_num):
    if((len(array)-1) >= i):
        if(array[i] > max_num):
            max_num = array[i]
        return max_list_num(array, i+1, max_num)
    else:
        return max_num

#Funcion Ejercicio 6
def repeat_num_list(array, num_repeats):
    if not array:
        return []
    current_element = array[0]
    repeated_elements = [current_element] * num_repeats
    return repeated_elements + repeat_num_list(array[1:], num_repeats)

#Funcion Ejercicio 7
def sum_recursiv(n,p):
    if (n>1):
        return (p*n) + sum_recursiv(n-1,p)
    elif(n <=0):
        return"n no puede valer ni ser menor a 0"
    elif n == 1: 
        return p

#Funcion Ejercicio 8
def calculate_pascal_value(fil, column):
    if column == 0 or column==fil:
        return 1
    else:
        return calculate_pascal_value(fil - 1, column - 1) + calculate_pascal_value(fil - 1, column)

#Funcion Ejercicio 9
def combinations(char,n,built_chain=""):
    if n==0:
        print(built_chain)
        return  
    else:
        for i in char:
            combinations(char,n-1,built_chain+i)

#Funcion Ejercicio 10
def sheet_measurement(n):
    if n==0:
        return(841,1189)
    previous_width, previous_length = sheet_measurement(n-1)
    if n % 2 == 1:
        return (previous_length, previous_width // 2)
    else:
        return (previous_width // 2, previous_length)