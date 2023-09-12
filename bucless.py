"""#1
abecedario="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("Ingrese cuantos espacios desea correr: "))

for i in range(5):
    mensaje_ingresado=input("Ingrese un mensaje: ")
    mensaje_ingresado=mensaje_ingresado.lower()
    mensaje_encriptado=" "
    for letra in mensaje_ingresado:
        if letra in abecedario:
            indice=abecedario.find(letra)
            indice=(indice + corrimiento)%27
            mensaje_encriptado += abecedario[indice]
        else:
            mensaje_encriptado +=letra
    print(mensaje_encriptado)
"""
"""#2
total_impares=total_pares=0
while True:
    num=int(input("Ingrese un numero(ingrese 0 para finalizar): "))
    if num==0:
        break
    pares=impares=0
    while num>0:
        digitos= num % 10
        if digitos % 2==0:
            pares=pares+1
        else:
            impares=impares+1
        num=num//10
    print(f"El numero tiene {pares} digitos pares y {impares} digitos impares")
    total_impares+=impares
    total_pares+=pares
print(f"La cantidad de digitos pares fue: {total_pares}")
print(f"La cantidad de digitos impares fue: {total_impares}")"""
