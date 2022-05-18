import random
from re import X
import time

lista_ordenada = [0]
x=[1]
for i in range(0,19999):
    lista_ordenada.extend(x)
    x[0]=x[0]+1  

lista_inversa = [19999]
x=[19999]
for i in range(0,19999):
    lista_inversa.extend(x)
    x[0]=x[0]-1  

lista_aleatoria = random.sample(range(19999),19999)






def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1
def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

ini_bubble = time.time()
bubble_sort(lista_ordenada)
fim_bubble = time.time()
ini_bubble2 = time.time()
bubble_sort(lista_inversa)
fim_bubble2 = time.time()
ini_bubble3 = time.time()
bubble_sort(lista_aleatoria)
fim_bubble3 = time.time()
print("Tempo bubble Sort: "+ str( fim_bubble - ini_bubble))
print("Tempo bubble Sort: "+ str( fim_bubble2 - ini_bubble2))
print("Tempo bubble Sort: "+ str( fim_bubble3 - ini_bubble3))
"""
ini_inser = time.time()
insertion_sort(lista_ordenada)
fim_inser = time.time()
ini_inser2 = time.time()
insertion_sort(lista_inversa)
fim_inser2 = time.time()
ini_inser3 = time.time()
insertion_sort(lista_aleatoria)
fim_inser3 = time.time()
print("Tempo Insertion Sort: "+ str( fim_inser - ini_inser))
print("Tempo Insertion Sort: "+ str( fim_inser2 - ini_inser2))
print("Tempo Insertion Sort: "+ str( fim_inser3 - ini_inser3))

ini_quicksort = time.time()
quicksort(lista_ordenada)
fim_quicksort = time.time()
ini_quicksort2 = time.time()
quicksort(lista_inversa)
fim_quicksort2 = time.time()
ini_quicksort3 = time.time()
quicksort(lista_aleatoria)
fim_quicksort3 = time.time()
print("Tempo quicksort Sort: "+ str( fim_quicksort - ini_quicksort))
print("Tempo quicksort Sort: "+ str( fim_quicksort2 - ini_quicksort2))
print("Tempo quicksort Sort: "+ str( fim_quicksort3 - ini_quicksort3))"""