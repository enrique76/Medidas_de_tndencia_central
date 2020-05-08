import matplotlib
import matplotlib.pyplot as plt


from statistics import mode,median,mean,pstdev,pvariance

import os 

while True:
    
    x = input("Datos: ")
    # Permite la entrada de multiples valores 
    x = x.split(',')
    x = [float(i.strip(''))for i in x]
    
    
    print("\nDatos ordenados: \n")
    # ordena lista 
    x.sort()

    for i in range(len(x)):
        print(x[i],end=' ')

    print("\nTotal de Datos: ",len(x))
    print("\nDato maximo: ", max(x))
    print("\nDato minimo: ", min(x))
    print("\nRango: ", max(x)-min(x))
    print("\nMedia: ",mean(x))
    print("\nMediana: ",median(x))
    print("\nModa: ", mode(x))
    print("\nVarianza: ", pvariance(x))
    print("\nDesviacion estandar: ", pstdev(x))
    # creacios del Histograma
    
    #eje y
    frecuencia = []
    
    #eje x
    eventos = []

    eventos.append(x[0])
    for i in range(len(x)-1):
        if x[i] != x[i+1]:
            eventos.append(x[i+1])

    for i in eventos:
        veces = x.count(i)
        frecuencia.append(veces)
    
    
    # mandar a graficarlo en barras  
    plt.plot(eventos,frecuencia,'ro') # los puntos 
    plt.plot(eventos,frecuencia, color = 'red') # las lineas 
    plt.bar(eventos,frecuencia) # barras
    
    # limitar y/o ampliar el eje x

    if (min(x) > 1):

        plt.axis([0,max(x)+1,min(frecuencia)-1,max(frecuencia)+1])
    elif (min(x) <= 1 ):
        
        plt.axis([min(x)-1,max(x)+1,min(frecuencia)-1,max(frecuencia)+1])

    # Etiquetas

    plt.xlabel('Eventos..')

    plt.ylabel('Frecuencia..')

    plt.show()
    
    
    #repeticion 
    y = input("\nQuieres repetir? ")
    if y == "no" or y =="No" or y=="NO" or y=="nel" :
        os.system('cls')
        break
    else:
        os.system('cls')
