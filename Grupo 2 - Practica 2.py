import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

from datetime import datetime, timedelta
def f(x):
    return x
inicio = datetime(2019,8,1,0,0,0)
fin    = datetime(2019,8,1,0,8,19)

x = [inicio + timedelta(seconds=s) for s in range((fin - inicio).seconds + 1)] 
y=np.random.randint(2000,4000,500)
media=stat.mean(y)

cuadrados = []
for dato in y:
  r = (dato - media)**2
  cuadrados.append(r)
des = (sum(cuadrados)/(500 - 1))**0.5 

print("La media es ")
print(media)
print("La desviacion estandar es ")
print(des)
#1
bmedia=media-des
smedia=media+des
#2
bmedia2=media-(des*2)
smedia2=media+(des*2)
#3
bmedia3=media-(des*3)
smedia3=media+(des*3)
plt.figure(figsize=(300,10))
errorx=[]
errory=[]
posix=[]
posiy=[]
p1=0

toca_menor = False
toca_mayor = False

for j in range(1,499):
    if(y[j]<=bmedia or y[j]>=smedia):
        errorx.append(x[j])
        errory.append(y[j])
    else:
        posix.append(x[j])
        posiy.append(y[j])
        
    #1er patron
    if(y[j]<=bmedia3 or y[j]>=smedia3):
        print("Patron 1 - Fecha: " + str(x[j]))
    #2do patron
    if(y[j]<=bmedia or y[j]>=smedia):
        p1=p1+1
    else:
        p1=0
    if(p1==9):
        print("Patron 2 - Fecha: " + str(x[j]))
    #3er patron
    valor_actual = y[j]
    valor_anterior = y[j - 1]
    incrementando = 0
    decrementando = 0

    if(valor_actual > valor_anterior):
        incrementando += 1
    else:
        incrementando = 0
    if(incrementando == 6):
        print("Patron 3 Incrementando - Fecha: " + str(x[j]))

    if(valor_actual < valor_anterior):
        decrementando += 1
    else:
        decrementando = 0
    if(decrementando == 6):
        print("Patron 3 Decrementando - Fecha: " + str(x[j]))

    #4to patron
    es_mayor_que_anterior = (y[j] > y[j-1])
    es_menor_que_anterior = (y[j] < y[j-1])

    if(es_mayor_que_anterior & toca_mayor):
        contador += 1
    elif(es_menor_que_anterior & toca_menor):
        contador += 1
    else:
        contador = 0

    if(es_mayor_que_anterior):
        toca_menor = True
        toca_mayor = False
    if(es_menor_que_anterior):
        toca_menor = False
        toca_mayor = True

    if(contador == 14):
        print("Patron 4 - Fecha: " + str(x[j]))



plt.plot(x,y)
plt.plot(errorx,errory,'o', color='r',markersize=2)
plt.plot(posix,posiy,'o', color='g',markersize=2)

plt.plot(x,[f(media) for i in x],label='LC')
plt.plot(x,[f(bmedia) for i in x],label='LCS',color='y')
plt.plot(x,[f(smedia) for i in x],label='LCI',color='y')

plt.plot(x,[f(bmedia2) for i in x],label='LCS',color='m')
plt.plot(x,[f(smedia2) for i in x],label='LCI',color='m')

plt.plot(x,[f(bmedia3) for i in x],label='LCS',color='r')
plt.plot(x,[f(smedia3) for i in x],label='LCI',color='r')

#plt.legend(loc='upper left')
plt.ylim(1000, 5000)
plt.figure(figsize=(300,10))
plt.show()