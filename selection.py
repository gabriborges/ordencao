import random
from re import X
import time

lista_ordenada20k = [0]
x=[1]
for i in range(0,19999):
    lista_ordenada20k.extend(x)
    x[0]=x[0]+1  

lista_inversa20k = [19999]
x=[19999]
for i in range(0,19999):
    lista_inversa20k.extend(x)
    x[0]=x[0]-1  

lista_aleatoria20k = random.sample(range(19999),19999)

#-------------#

lista_ordenada40k = [0]
x=[1]
for i in range(0,39999):
    lista_ordenada40k.extend(x)
    x[0]=x[0]+1  

lista_inversa40k = [39999]
x=[39999]
for i in range(0,39999):
    lista_inversa40k.extend(x)
    x[0]=x[0]-1  

lista_aleatoria40k = random.sample(range(39999),39999)

#-------------#

lista_ordenada60k = [0]
x=[1]
for i in range(0,59999):
    lista_ordenada60k.extend(x)
    x[0]=x[0]+1  

lista_inversa60k = [59999]
x=[59999]
for i in range(0,59999):
    lista_inversa60k.extend(x)
    x[0]=x[0]-1  

lista_aleatoria60k = random.sample(range(59999),59999)

#-------------#

lista_ordenada80k = [0]
x=[1]
for i in range(0,79999):
    lista_ordenada80k.extend(x)
    x[0]=x[0]+1  

lista_inversa80k = [79999]
x=[79999]
for i in range(0,79999):
    lista_inversa80k.extend(x)
    x[0]=x[0]-1  

lista_aleatoria80k = random.sample(range(79999),79999)

#-------------#

lista_ordenada100k = [0]
x=[1]
for i in range(0,79999):
    lista_ordenada100k.extend(x)
    x[0]=x[0]+1  

lista_inversa100k = [79999]
x=[79999]
for i in range(0,79999):
    lista_inversa100k.extend(x)
    x[0]=x[0]-1  

lista_aleatoria100k = random.sample(range(99999),99999)

#-------------#


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

print("Lista de 20k: ")
ini_20K = time.time()
selection_sort(lista_ordenada20k)
fim_20K = time.time()
ini2_20K = time.time()
selection_sort(lista_inversa20k)
fim2_20K = time.time()
ini3_20K = time.time()
selection_sort(lista_aleatoria20k)
fim3_20K = time.time()
print("Tempo bubble Sort ordenada: "+ str( fim_20K - ini_20K))
print("Tempo bubble Sort inversa: "+ str( fim2_20K - ini2_20K))
print("Tempo bubble Sort aleatoria: "+ str( fim3_20K - ini3_20K))

print("Lista de 40k: ")
ini_40K = time.time()
selection_sort(lista_ordenada40k)
fim_40K = time.time()
ini2_40K = time.time()
selection_sort(lista_inversa40k)
fim2_40K = time.time()
ini3_40K = time.time()
selection_sort(lista_aleatoria40k)
fim3_40K = time.time()
print("Tempo bubble Sort ordenada: "+ str( fim_40K - ini_40K))
print("Tempo bubble Sort inversa: "+ str( fim2_40K - ini2_40K))
print("Tempo bubble Sort aleatoria: "+ str( fim3_40K - ini3_40K))


print("Lista de 60k: ")
ini_60K = time.time()
selection_sort(lista_ordenada60k)
fim_60K = time.time()
ini2_60K = time.time()
selection_sort(lista_inversa60k)
fim2_60K = time.time()
ini3_60K = time.time()
selection_sort(lista_aleatoria60k)
fim3_60K = time.time()
print("Tempo bubble Sort ordenada: "+ str( fim_60K - ini_60K))
print("Tempo bubble Sort inversa: "+ str( fim2_60K - ini2_60K))
print("Tempo bubble Sort aleatoria: "+ str( fim3_60K - ini3_60K))

print("Lista de 80k: ")
ini_80K = time.time()
selection_sort(lista_ordenada80k)
fim_80K = time.time()
ini2_80K = time.time()
selection_sort(lista_inversa80k)
fim2_80K = time.time()
ini3_80K = time.time()
selection_sort(lista_aleatoria80k)
fim3_80K = time.time()
print("Tempo bubble Sort ordenada: "+ str( fim_80K - ini_80K))
print("Tempo bubble Sort inversa: "+ str( fim2_80K - ini2_80K))
print("Tempo bubble Sort aleatoria: "+ str( fim3_80K - ini3_80K))

print("Lista de 100k: ")
ini_100K = time.time()
selection_sort(lista_ordenada100k)
fim_100K = time.time()
ini2_100K = time.time()
selection_sort(lista_inversa100k)
fim2_100K = time.time()
ini3_100K = time.time()
selection_sort(lista_aleatoria100k)
fim3_100K = time.time()
print("Tempo ordenada: "+ str( fim_100K - ini_100K))
print("Tempo inversa: "+ str( fim2_100K - ini2_100K))
print("Tempo aleatoria: "+ str( fim3_100K - ini3_100K))