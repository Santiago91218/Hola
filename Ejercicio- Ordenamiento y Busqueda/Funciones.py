#Bubble Sort
def Bubble_Sort(listt):
    for i in range(len(listt)):
        for j in range(0,len(listt)-i-1):
            if listt[j] > listt[j+1]:
                listt[j], listt[j+1] = listt[j+1], listt[j]
    return listt

#Selection Sort
def Selection_Sort(listt):
    for i in range(len(listt)-1):
        minor=listt[i]
        pos=i
        for j in range(i+1,len(listt)):
            if listt[j]<minor:
                minor=listt[j]
                pos=j
        if pos!=i:
            tmp=listt[i]
            listt[i]=listt[pos]
            listt[pos]=tmp
    return listt

#Insert Sort
def Insert_Sort(listt):
    for i in range(len(listt)):
        aux = listt[i]
        j = i - 1
        while ((j >= 0) and (aux < listt[j])):
            listt[j + 1] = listt[j]
            j-=1            
        listt[j + 1] = aux
    return listt

#Merge Sort
def Merge_Sort(listt):
    if len(listt) > 1:
        mid = len(listt) // 2
        left_half = listt[:mid]
        right_half = listt[mid:]

        Merge_Sort(left_half)
        Merge_Sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                listt[k] = left_half[i]
                i += 1
            else:
                listt[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            listt[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            listt[k] = right_half[j]
            j += 1
            k += 1
    return listt

#Busqueda Lineal
def Linear_Search(listt):
    condition=False
    element=int(input("Ingrese el numero que quiere encontar: "))
    for i in listt:
        if i == element:
            condition=True

    if condition==True:
        print(f"El numero {element} se encontro en la lista")
    else:
        print(f"El numero {element} no se encontro en la lista")
        
#Busqueda Binaria
def Binary_Search(listt):
    left=0
    right=len(listt) - 1
    condition=False
    element=int(input("Ingrese el numero que quiere encontar: "))
    while left <= right:
        mid = (left + right) // 2  

        if listt[mid] == element:
            condition=True
            break  
        elif listt[mid] < element:
            left = mid + 1  
        else:
            right = mid - 1 

    if condition==True:
        print(f"El numero {element} se encontro en la lista")
    else:
        print(f"El numero {element} no se encontro en la lista")