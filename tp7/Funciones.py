#Funcion Ejercicio 1
def Bubble_Sort(listt):
    for i in range(len(listt)):
        for j in range(0,len(listt)-i-1):
            if listt[j] > listt[j+1]:
                listt[j], listt[j+1] = listt[j+1], listt[j]
    return listt

#Funcion Ejercicio 2
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

#Funciones Ejercicio 3
def title_Order(list_dic):
    for i in range(len(list_dic)):
        for j in range(0,len(list_dic)-i-1):
            if list_dic[j]["titulo"] > list_dic[j+1]["titulo"]:
                list_dic[j], list_dic[j+1] = list_dic[j+1], list_dic[j]
    return list_dic

def author_Order(list_dic):
    for i in range(len(list_dic)):
        for j in range(0,len(list_dic)-i-1):
            if list_dic[j]["autor"] > list_dic[j+1]["autor"]:
                list_dic[j], list_dic[j+1] = list_dic[j+1], list_dic[j]
    return list_dic

def year_Order(list_dic):
    for i in range(len(list_dic)):
        for j in range(0,len(list_dic)-i-1):
            if list_dic[j]["año_publicacion"] > list_dic[j+1]["año_publicacion"]:
                list_dic[j], list_dic[j+1] = list_dic[j+1], list_dic[j]
    return list_dic

#Funcion Ejercicio 4
def Insert_Sort(list_word):
    for i in range(len(list_word)):
        aux = list_word[i]
        j = i - 1
        while j >= 0 and len(aux) < len(list_word[j]):
            list_word[j + 1] = list_word[j]
            j-=1            
        list_word[j + 1] = aux
    return list_word

#Funcion Ejercicio 5
def Bubble_Sort_Des(listt):
    for i in range(len(listt)):
        for j in range(0,len(listt)-i-1):
            if listt[j] < listt[j+1]:
                listt[j], listt[j+1] = listt[j+1], listt[j]
    return listt

#Funcion Ejercicio 6
def Count_Order(listt):
    if not listt:
        return listt
    min_val = min(listt)
    max_val = max(listt)

    count_arr = [0] * (max_val - min_val + 1)

    for num in listt:
        count_arr[num - min_val] += 1

    sorted_list = []
    for i, count in enumerate(count_arr):
        sorted_list.extend([i + min_val] * count)

    return sorted_list

#Funcion Ejercicio 7
def order_Elements(elements):
    list_num=[]
    list_word=[]
    for i in elements:
        if type(i)==int:
            list_num.append(i)
        elif type(i)==str:
            list_word.append(i)
    print(f"Lista de numeros ordenada: {Selection_Sort(list_num)}")
    print(f"Lista de palabras ordenada alfabeticamente: {Selection_Sort(list_word)}")

#Funcion Ejercicio 8
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